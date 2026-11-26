---
name: research
description: Cari berita, riset, atau data, lalu ringkas hasilnya beserta sumbernya.
metadata:
  author: ai-agent-skills
  version: "1.0.0"
  license: UNLICENSED
---

# Research

Cari informasi topik tertentu, lalu ringkas poin penting dengan sumber.

## Kapan dipakai

- Menemukan informasi terbaru
- Membandingkan opsi atau harga
- Mengumpulkan data untuk laporan / keputusan

## Cara kerja

1. Tentukan topik / kata kunci.
2. Cari dengan tool riset (`web_search`).
3. Baca halaman kunci (`web_extract`) bila perlu.
4. Ringkas: inti, bukti, dan sumber.
5. Catat URL agar bisa diceklai kembali.

## Pengecekan

- Semua klaim punya sumber.
- Data khusus mencantumkan tahun / sumber.
- Hindari opini yang dipakai sebagai fakta.

## Dependencies

- Tool riset (web_search / web_extract)
