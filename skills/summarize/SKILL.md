---
name: summarize
description: Buat ringkasan singkat berbentuk poin (bullet) dari teks, dokumen, atau laporan apa pun.
metadata:
  author: ai-agent-skills
  version: "1.0.0"
  license: UNLICENSED
---

# Summarize

Buat ringkasan singkat berbentuk poin-poin dari teks, dokumen, atau laporan
apa pun, sambil menjaga fakta dan menyisakan inti saja.

## Kapan dipakai

- Ringkasan laporan, email panjang, atau dokumentasi
- Meringkas hasil riset / web-check sebelum dilanjutkan
- Menyusun poin aksi dari catatan

## Cara kerja

1. Ambil teks sumber (salin, baca file, atau ambil dari web-check / research).
2. Pisahkan bagian: inti, detail, dan hal yang tidak jelas.
3. Buat ringkasan berbentuk poin singkat:
   - Kalimat pertama = inti utama
   - Setiap poin = satu ide
   - Hapus pengulangan dan opini yang tidak jelas
4. Catat sumber / bagian asal (tanggal, URL, atau hash) untuk fakta.

## Pengecekan

- Semua poin berisi fakta, bukan opini.
- Setiap poin berdiri sendiri (satu ide per poin).
- Menyisakan inti, bukan salinan panjang.
- Sumber dicatat kalau materi berisi klaim atau angka.

## Dependencies

- Agen AI (membaca, meringkas, menulis) — pengerjaan inti
- Teks sumber (file, URL, atau teks yang diberikan)
