# markers

Finds `NEEDSWORK`, `TODO`, `FIXME` and `XXX` markers in a git repository and
writes a Markdown report, with the date each line was last touched and a link
to it on GitHub.

Needs Python 3.8+ and `git`. No dependencies.

## Usage

Point `REPO` at a local clone:

```
make REPO=/path/to/repo     # writes markers.csv and MARKERS.md
make clean
```

Or run the two steps directly:

```
REPO=/path/to/repo python3 markers.py scan     # git grep + git blame -> markers.csv (slow)
REPO=/path/to/repo python3 markers.py report   # markers.csv -> MARKERS.md
```

`report` only reads the CSV, so you can rerun it freely to tweak the output.

`REPO` is the only knob. Everything else lives in the constants at the top of
`markers.py`, including the GitHub URL the report links against set it to
match the repository you scan. Links point at the tip of a branch rather than
the scanned commit, since your local HEAD may not exist on the remote.

---

*Built with the help of AI.*
