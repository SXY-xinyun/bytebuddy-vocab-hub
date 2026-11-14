import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import vm from "vm";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");
const jsDir = path.join(root, "website/js");
const extra = fs.readFileSync(path.join(jsDir, "vocab-extra.js"), "utf8");
let words = fs.readFileSync(path.join(jsDir, "words.js"), "utf8");
words = words.replace(
  /if \(typeof MORE_VOCAB !== "undefined"\) \{\s*VOCABULARY\.push\(\.\.\.MORE_VOCAB\);\s*\}/,
  "VOCABULARY.push(...MORE_VOCAB);"
);
const code = `${extra}\n${words}\nVOCABULARY;`;
const list = vm.runInNewContext(code, {}, { timeout: 5000 });
const outPath = path.join(root, "vocab_dump.json");
fs.writeFileSync(outPath, JSON.stringify(list, null, 2), "utf8");
console.log("Wrote", list.length, "entries to", outPath);
