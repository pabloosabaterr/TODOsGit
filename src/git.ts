const decoder = new TextDecoder("utf-8");

export class Git {

  constructor(private gitPath: string) {
    this.open(gitPath);
  }

  private open(path: string): string {
    if (path === "~" || path.startsWith("~/"))
      path = (Deno.env.get("HOME") ?? "~") + path.slice(1);

    return this.gitPath = path;
  }

  parseOutput<T>(
    output: string,
    build: (head: string, rest: string) => T | null,
  ): T | null {
    const nul = output.indexOf("\0");
    if (nul < 0)
      return null;

    return build(output.slice(0, nul), output.slice(nul + 1));
  }

  async doCommand(command: string, pattern?: string): Promise<string> {
    const args = ["-C", this.gitPath, ...command.split(" ").filter(Boolean)];
    if (pattern)
      args.push(pattern);

    const {code, stdout, stderr}: Deno.CommandOutput = await new Deno.Command("git", {
      args: args,
    }).output();

    if (code !== 0)
      throw new Error(decoder.decode(stderr));

    return decoder.decode(stdout);
  }
}

