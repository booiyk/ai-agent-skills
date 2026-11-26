# CONTRIBUTING

Panduan menambah dan mengelola skill di repo ini.

## Cara menambah skill

1. Salin `skills/TEMPLATE.md` menjadi `skills/<nama-skill>/SKILL.md`.
2. Isi `name`, `version`, `description` di frontmatter, lalu isi
   `Kapan`, `Langkah`, `CLI`, `Contoh`, `Batasan`, `Referensi` di body.
3. Jangan simpan hasil generate / `dist` / `node_modules` / file sensitif.
4. Jalankan validasi lokal: `python scripts/validate-skills.py` (harus exit 0).
5. Pasang pre-commit, lalu commit: `pre-commit install && git add -A && git commit`.
6. Push & tunggu CI: `git push`.

## Aturan

- **Nama skill** unik. Format `lowercase`, boleh menggunakan dash atau dot.
- **Setiap SKILL.md** wajib punya frontmatter `name`, `version`, `description`.
- Bahasa konsisten (Indonesia).
- Skill hanya boleh memuat kode yang bisa diinstal (npm / pip / yarn).
  Tidak boleh menyertakan file sensitif, kunci, atau data pribadi.
- `README.md` dan `skills/INDEX.md` selalu diperbarui kalau skill baru masuk.

## Format SKILL.md

Setiap skill berisi:

- `name` — identitas unik skill
- `version` — versi skill (SemVer)
- `description` — kapan skill ini dipakai
- Body: `Kapan`, `Langkah`, `CLI`, `Contoh`, `Batasan`, `Referensi`

Frontmatter (YAML antarfase):

```yaml
---
name: namaAksi
version: "1.0.0"
description: Kapan skill ini dipakai
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
memiliki kunci `name`, `version`, `description`.

## Quality gates otomatis

- **Pre-commit** (lokal): `pre-commit run --all-files`
- **CI** (pusher): `.github/workflows/validate-skills.yml`

## Lihat juga

- `README.md` — ringkasan repo
- `skills/INDEX.md` — daftar semua skill
- `scripts/schema/skills-schema.json` — schema frontmatter SKILL.md
