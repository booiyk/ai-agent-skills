# AI Agent Skills

Koleksi **skill AI agent** — file `SKILL.md` + contoh pakai, siap dipakai oleh
agen AI (Claude, custom agent, dsb) sebagai unit kerja yang mandiri.

## Struktur

```
ai-agent-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── scripts/
│   └── validate-skills.py      # validasi skema SKILL.md (exit 0 kalau all OK)
└── skills/
    ├── TEMPLATE.md             # Template skill baru
    ├── INDEX.md                # Daftar semua skill + ringkasan
    ├── make-fun/               # Entri bounty make.fun
    ├── research/               # Cari + ringkas berita/riset/harga
    ├── web-check/              # Ambil & ringkas halaman web
    ├── compile/                # Bangun / proses project
    ├── hold/                   # Jaga proses di luar sesi terminal
    ├── pdf-reader/             # Baca dokumen PDF
    └── summarize/              # Ringkasan teks → poin (contoh lengkap)
```

## Cara pakai

1. Salin `skills/TEMPLATE.md` menjadi `skills/<nama-skill>/SKILL.md`.
2. Isi `name`, `description`, `instructions`, `dependencies`.
3. Skill hanya menyertakan kode yang bisa diinstal; tidak menyimpan data
   sensitif. Hasil generate (kalau ada) tidak di-commit.

## Kontribusi

- Baca `CONTRIBUTING.md` — panduan menambah skill, aturan, dan validasi.
- Validasi skema semua skill: `python scripts/validate-skills.py`
- Daftar skill: `skills/INDEX.md`
- Lisensi: MIT — file `LICENSE`

## Validasi singkat

```bash
python3 scripts/validate-skills.py
```

> Harus exit 0, dan menampilkan `7/7 skill valid` (sesuai jumlah skill saat ini).
