# CONTRIBUTING

Panduan menambah dan mengelola skill di repo ini.

## Cara menambah skill

1. Salin `skills/TEMPLATE.md` menjadi `skills/<nama>/SKILL.md`.
2. Isi `name` (unik, lowercase, pakai dash atau dot), `description`,
   `instructions`, `dependencies`.
3. Jangan simpan hasil generate / `dist` / `node_modules` / file sensitif.
4. Jalankan validasi: `python scripts/validate-skills.py` (harus exit 0).
5. Commit & push ke main: `git add -A && git commit -m "Add <nama> skill" && git push`.

## Aturan

- **Nama skill** unik. Format `lowercase`, boleh menggunakan dash atau dot.
- **Setiap SKILL.md** wajib punya frontmatter `name` dan `description`.
- Bahasa konsisten (Indonesia).
- Skill hanya boleh memuat kode yang bisa diinstal (npm / pip / yarn).
  Tidak boleh menyertakan file sensitif, kunci, atau data pribadi.
- `README.md` dan `skills/INDEX.md` selalu diperbarui kalau skill baru masuk.

## Format SKILL.md

Setiap skill berisi:

- `name` — identitas unik skill
- `description` — kapan skill ini dipakai
- `instructions` — langkah-langkah konkret
- `dependencies` — hal yang harus ada di environment

Frontmatter (YAML antarfase) utama:

```yaml
---
name: namaAksi
description: Kapan skill ini dipakai
metadata:
  author: nama-pembuat
  version: "1.0.0"
  license: UNLICENSED
---
```

## Validasi

Jalankan dari root repo:

```bash
python scripts/validate-skills.py
```

Script ini memastikan setiap `SKILL.md` punya frontmatter yang ditutup dan
memiliki kunci `name` + `description`.

## Lihat juga

- `README.md` — ringkasan repo
- `skills/INDEX.md` — daftar semua skill
