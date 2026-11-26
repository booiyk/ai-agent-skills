# CONTRIBUTING

Panduan menambah dan mengelola skill di repo ini.

## Cara menambah skill

1. Salin `skills/TEMPLATE.md` menjadi `skills/<nama>/SKILL.md`.
2. Isi `name` (unik, lowercase, pakai dash atau dot), `description`,
   `instructions`, `dependencies`.
3. Jangan simpan hasil generate / `dist` / `node_modules` / file sensitif.
4. Jalankan validasi lokal: `python scripts/validate-skills.py` (harus exit 0).
5. Pasang pre-commit, lalu commit: `pre-commit install && git add -A && git commit`.
6. Push & tunggu CI: `git push`.

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

Format frontmatter ini didefinisikan pakai JSON Schema di
`scripts/schema/skills-schema.json`. Tool lint / editor dapat memanfaatkannya.

## Validation lokal

Jalankan dari root repo:

```bash
python scripts/validate-skills.py
```

Script ini memastikan setiap `SKILL.md` punya frontmatter yang ditutup dan
memiliki kunci `name` + `description`.

## Quality gates otomatis

- **Pre-commit** (lokal): `pre-commit run --all-files`
- **CI** (pusher): `.github/workflows/validate-skills.yml`

## Lihat juga

- `README.md` — ringkasan repo
- `skills/INDEX.md` — daftar semua skill
- `scripts/schema/skills-schema.json` — schema frontmatter SKILL.md
