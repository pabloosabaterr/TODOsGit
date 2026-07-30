#!/usr/bin/env python3

import collections
import csv
import datetime
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(os.environ.get("REPO", "")).expanduser()
GITHUB = "https://github.com/git/git/blob"
REF = "master"
MARKERS = ("NEEDSWORK", "TODO", "FIXME", "XXX")
CSV_FILE = Path("markers.csv")
MD_FILE = Path("MARKERS.md")

CSV_FIELDS = ("date", "commit", "author", "file", "line", "text")


def git(*args):
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True, text=True, errors="replace",
    ).stdout


def find_markers():
    hits = collections.defaultdict(dict)
    for row in git("grep", "-nIw", "-E", "|".join(MARKERS)).splitlines():
        path, lineno, text = (row.split(":", 2) + ["", ""])[:3]
        if lineno.isdigit():
            hits[path][int(lineno)] = text.strip()
    return hits


def blame(path, linenos):
    args = ["blame", "-w", "--line-porcelain"]
    for n in linenos:
        args += ["-L", f"{n},{n}"]

    result, current = {}, {}
    for line in git(*args, "--", path).splitlines():
        if re.match(r"^[0-9a-f]{40} ", line):
            sha, _, lineno = line.split()[:3]
            current = {"commit": sha[:8], "lineno": int(lineno)}
        elif line.startswith("author "):
            current["author"] = line[len("author "):]
        elif line.startswith("author-time "):
            when = int(line.split()[1])
            current["date"] = datetime.date.fromtimestamp(when).isoformat()
        elif line.startswith("\t") and current:
            result[current.pop("lineno")] = current
            current = {}
    return result


def scan():
    rows = []
    for path, lines in sorted(find_markers().items()):
        blamed = blame(path, sorted(lines))
        for lineno, text in sorted(lines.items()):
            info = blamed.get(lineno, {})
            rows.append({
                "date": info.get("date", ""),
                "commit": info.get("commit", ""),
                "author": info.get("author", ""),
                "file": path,
                "line": lineno,
                "text": text,
            })

    with CSV_FILE.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} markers -> {CSV_FILE}")


def table(headers, rows):
    if not rows:
        return ["_(none)_", ""]
    lines = ["| " + " | ".join(headers) + " |",
             "|" + " --- |" * len(headers)]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return lines + [""]


def top_level(path):
    return path.split("/", 1)[0] if "/" in path else "(root)"


def build_report(rows):
    head = git("rev-parse", "HEAD").strip()
    version = git("describe", "--tags", "--always").strip()

    out = [
        f"# {' / '.join(MARKERS)} markers in {REPO.resolve().name}",
        "",
        f"{len(rows)} lines in total, at HEAD `{head[:8]}` ({version}). "
        f"Collected on {datetime.date.today().isoformat()}.",
        "",
        "Dates come from `git blame -w` and refer to the last time the line was "
        "touched, which is not necessarily when the marker was added.",
        "",
        f"Links point at the tip of `{REF}` on GitHub, so line numbers may drift "
        "as that branch moves ahead of the commit scanned here.",
        "",
        "This file is generated. Run `make` to rebuild it; do not edit it by hand.",
        "",
    ]

    out += ["## Count by marker", ""]
    counts = collections.Counter(
        m for row in rows for m in MARKERS if re.search(rf"\b{m}\b", row["text"]))
    out += table(["Marker", "Count"], [(m, counts.get(m, 0)) for m in MARKERS])

    out += ["## Count by top-level directory", ""]
    counts = collections.Counter(top_level(row["file"]) for row in rows)
    out += table(["Directory", "Count"], sorted(counts.items()))

    out += ["## Count by year of last modification", ""]
    counts = collections.Counter(row["date"][:4] for row in rows if row["date"])
    out += table(["Year", "Count"], sorted(counts.items()))

    out += ["## Full listing", ""]
    grouped = collections.defaultdict(lambda: collections.defaultdict(list))
    for row in rows:
        grouped[top_level(row["file"])][row["file"]].append(row)

    for directory in sorted(grouped):
        files = grouped[directory]
        total = sum(len(entries) for entries in files.values())
        out += ["<details>",
                f"<summary><b>{directory}</b> &mdash; {total} markers</summary>",
                ""]
        for path in sorted(files):
            entries = sorted(files[path], key=lambda r: int(r["line"]))
            out += [f"`{path}` ({len(entries)})", ""]
            for r in entries:
                url = f"{GITHUB}/{REF}/{r['file']}#L{r['line']}"
                text = r["text"][:70].replace("`", "'")
                out.append(f"- {r['date']} `{r['commit']}` "
                           f"[L{r['line']}]({url}) `{text}`")
            out.append("")
        out += ["</details>", ""]

    return "\n".join(out).rstrip() + "\n"


def report():
    with CSV_FILE.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    MD_FILE.write_text(build_report(rows), encoding="utf-8")
    print(f"{len(rows)} markers -> {MD_FILE}")


COMMANDS = {"scan": scan, "report": report}

if __name__ == "__main__":
    command = COMMANDS.get(sys.argv[1] if len(sys.argv) > 1 else "")
    if not command:
        sys.exit(f"usage: REPO=/path/to/repo {sys.argv[0]} "
                 f"{{{'|'.join(COMMANDS)}}}")
    if not os.environ.get("REPO"):
        sys.exit("REPO is not set: point it at the git repository to scan")
    command()
