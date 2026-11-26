# AI Agent Skills

Koleksi **skill AI agent** — file `SKILL.md` + contoh pakai, siap dipakai oleh
agen AI (Claude, custom agent, dsb) sebagai unit kerja yang mandiri.

> Setiap skill berisi file `SKILL.md` yang dibaca agent. Formatnya:
> YAML frontmatter (`name`, `version`, `description`) + body berisi
> `Kapan`, `Langkah`, `CLI`, `Contoh`, `Batasan`, `Referensi`.

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
    ├── makefun/                  # Entri bounty make.fun
    ├── research/                 # Cari + ringkas berita/riset/harga
    ├── web-check/                # Ambil & ringkas halaman web
    ├── compile/                  # Bangun / proses project
    ├── hold/                     # Jaga proses di luar sesi terminal
    ├── pdf-reader/               # Baca dokumen PDF
    └── summarize/              # Ringkasan teks → poin (contoh lengkap)
```

## Cara pakai

1. Agent (misal Muse) membaca daftar skill dari `skills/INDEX.md` (nama + deskripsi).
2. Ketika tugas cocok dengan satu skill, agent membaca `SKILL.md` penuh.
3. Ikuti instruksi di dalamnya: `Kapan`, `Langkah`, `CLI`, `Contoh`, `Batasan`, `Referensi`.
4. Hasil dikirim kembali.

## Kontribusi

- Baca `CONTRIBUTING.md` — panduan menambah skill, aturan, dan validasi.
- Daftar skill: `skills/INDEX.md`
- Lisensi: MIT — file `LICENSE`

## Quality gates (otomatis)

Repo ini punya tiga lapisan validasi:

1. **Pre-commit** — `python3 scripts/validate-skills.py` dijalankan saat
   `git commit` (pasang pre-commit dulu).
2. **CI** — `.github/workflows/validate-skills.yml` jalan di GitHub atas
   push ke `main` dan pull request.
3. **Schema** — `scripts/schema/skills-schema.json` memaknai format SKILL.md
   (bisa diperiksa alat lint / editor bila tersedia).

```bash
python3 scripts/validate-skills.py
```
