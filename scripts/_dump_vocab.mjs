
import fs from 'fs';
import vm from 'vm';
const dir = new URL('../website/js/', import.meta.url);
const extra = fs.readFileSync(new URL('vocab-extra.js', dir), 'utf8');
const words = fs.readFileSync(new URL('words.js', dir), 'utf8');
const ctx = { MORE_VOCAB: [], VOCABULARY: [] };
vm.runInContext(extra, vm.createContext(ctx));
const wctx = { ...ctx, MORE_VOCAB: ctx.MORE_VOCAB };
vm.runInContext(words, vm.createContext(wctx));
console.log(JSON.stringify(wctx.VOCABULARY));
