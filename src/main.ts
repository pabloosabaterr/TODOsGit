import { Cli } from "./cli.ts";
import { Git } from "./git.ts";
import { Grep } from "./grep.ts";
import { Scanner } from "./scanner.ts";

const git = new Git(Cli.parseArgs());
const grep = new Grep(git);
const sc = new Scanner(git, grep);

sc.scan();


