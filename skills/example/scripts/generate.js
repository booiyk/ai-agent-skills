#!/usr/bin/env node
/**
 * Contoh generator untuk skill `example`.
 * Ganti placeholder `#NAME#` dan `#DATE#` di berkas template, tulis hasilnya ke dist/.
 */
const fs = require("fs");
const path = require("path");

const name = (() => {
  const i = process.argv.indexOf("--name");
  return i >= 0 ? process.argv[i + 1] : undefined;
})();
const date = (() => {
  const i = process.argv.indexOf("--date");
  return i >= 0 ? process.argv[i + 1] : undefined;
})();

const optsName = name || "contoh";
const optsDate = date || new Date().toISOString().slice(0, 10);

const template = "#NAME# — #DATE#\n";
const out = template
  .replace(/#NAME#/g, optsName)
  .replace(/#DATE#/g, optsDate);

fs.mkdirSync(path.join(__dirname, "..", "dist"), { recursive: true });
fs.writeFileSync(path.join(__dirname, "..", "dist", "out.txt"), out, "utf8");

console.log("Tulis ke dist/out.txt:", out.trim());
