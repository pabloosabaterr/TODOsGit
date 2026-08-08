import type { Git } from "./git.ts";
import type { Grep, GrepHit } from "./grep.ts";

export class Scanner {

  constructor(
    private readonly git: Git,
    private readonly grep: Grep,
  ) {}

  async scan(): Promise<void> {
    const hits: Map<string, Map<number, string>> = await this.grep.find();
    console.log(hits);
  }
}
