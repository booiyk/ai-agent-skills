---
name: example
description: Contoh skill terisi. Gunakan sebagai acuan format SKILL.md sebelum membuat skill baru.
metadata:
  author: ai-agent-skills
  version: "1.0.0"
  license: UNLICENSED
---

# Example — Templating file dari folder sumber

Skill ini menghasilkan file dari template, mengganti placeholder dengan nilai
dari environment atau dari input yang diberikan.

## Kapan dipakai

- Membuat banyak berkas dengan isi seragam
- Mengganti placeholder `#DATE#`, `#NAME#` secara otomatis

## Instruksi

1. Baca `scripts/generate.js`.
2. Jalankan: `node scripts/generate.js --name <nama> --date <tanggal>`.
3. Hasilnya muncul di `dist/`.

## Dependencies

- Node.js >= 18
- npm (bundled dengan Node.js)

## Lihat juga

- `TEMPLATE.md` — template untuk skill baru
