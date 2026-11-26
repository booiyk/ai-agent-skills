# AI Agent Skills

Koleksi **skill AI agent** — file `SKILL.md` + contoh pakai, siap dipakai oleh
agen AI (Claude, custom agent, dsb) sebagai unit kerja yang mandiri.

## Struktur

```
ai-agent-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .github/
│   └── workflows/
│       └── validate-skills.yml   # CI otomatis (push / pull request)
├── .pre-commit-config.yaml       # pre-commit: validasi loket sebelum commit
├── scripts/
│   ├── validate-skills.py        # validasi skema SKILL.md (exit 0 kalau all OK)
│   └── schema/
│       └── skills-schema.json    # JSON Schema format SKILL.md
└── skills/
    ├── TEMPLATE.md               # Template skill baru
    ├── INDEX.md                  # Daftar semua skill + ringkasan
    ├── make-fun/                 # Entri bounty make.fun
    ├── research/                 # Cari + ringkas berita/riset/harga
    ├── web-check/                # Ambil & ringkas halaman web
    ├── compile/                  # Bangun / proses project
    ├── hold/                     # Jaga proses di luar sesi terminal
    ├── pdf-reader/               # Baca dokumen PDF
    └── summarize/                # Ringkasan teks → poin (contoh lengkap)
```

## Cara pakai

1. Salin `skills/TEMPLATE.md` menjadi `skills/<nama-skill>/SKILL.md`.
2. Isi `name`, `description`, `instructions`, `dependencies`.
3. Skill hanya menyertakan kode yang bisa diinstal; tidak menyimpan data
   sensitif. Hasil generate (kalau ada) tidak di-commit.

## Kontribusi

- Baca `CONTRIBUTING.md` — panduan menambah skill, aturan, dan validasi.
- Daftar skill: `skills/INDEX.md`
- Lisensi: MIT — file `LICENSE`

## Quality gates (otomatis)

Repo ini punya tiga lapisan validasi:

1. **Pre-commit** — `python scripts/validate-skills.py` dijalankan saat
   `git commit` (pasang pre-commit dulu).
2. **CI** — `.github/workflows/validate-skills.yml` jalan di GitHub atas
   push ke `main` dan pull request.
3. **Schema** — `scripts/schema/skills-schema.json` memaknai format SKILL.md
   (bisa diperiksa alat lint / editor bila tersedia).

```bash
python3 scripts/validate-skills.py
```
