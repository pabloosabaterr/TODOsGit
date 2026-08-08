import type { Git } from "./git.ts";

const KEYWORDS = ["TODO", "NEEDSWORK", "FIXME", "XXX"];

export interface GrepHit {
  file: string;
  line: number;
  text: string;
}

export class Grep {

  constructor (
    private readonly git: Git,
  ) {}

  buildGrepHit(file: string, rest: string): GrepHit | null {
    const sep = rest.search(/[\0:]/);
    if (sep < 0) return null;

    const line = Number(rest.slice(0, sep));
    if (!Number.isInteger(line) || line <= 0) return null;

    return { file, line, text: rest.slice(sep + 1).trim() };
  }

  async find(): Promise<Map<string, Map<number, string>>> {
    const stdout = await this.git.doCommand("grep -z -nIw -E", `"${KEYWORDS.join("|")}"`);
    const hits = new Map<string, Map<number, string>>();

    for (const record of stdout.split("\n")) {
      const hit = this.git.parseOutput(record, this.buildGrepHit)
      if (!hit)
        continue;

      let lines = hits.get(hit.file);
      if (!lines)
        hits.set(hit.file, lines = new Map());

      lines.set(hit.line, hit.text);
    }

    return hits;
  }
}
