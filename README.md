# AI Agent Skills

Koleksi **skill AI agent** — file `SKILL.md` + contoh pakai, siap dipakai oleh
agen AI (Claude, custom agent, dsb) sebagai unit kerja yang mandiri.

## Struktur

```
ai-agent-skills/
├── README.md
└── skills/
    ├── TEMPLATE.md          # Template SKILL baru
    └── example/             # Contoh skill yang sudah terisi
        ├── SKILL.md
        └── scripts/
```

## Cara pakai

1. Salin `skills/TEMPLATE.md` menjadi `skills/<nama-skill>/SKILL.md`.
2. Isi `name`, `description`, dan isi inti skill.
3. Unduhan/dependency ditulis di `SKILL.md` (bukan di repo) supaya skill tetap
   ringan.

## Kontribusi

Tambah folder di `skills/`. Setiap skill wajib punya `SKILL.md` yang memuat:

- `name` — identitas unik skill
- `description` — kapan skill ini dipakai
- `instructions` — langkah-langkah konkret
- `dependencies` — apa yang harus ada di environment
