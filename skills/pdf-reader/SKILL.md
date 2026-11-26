---
name: pdf-reader
description: Baca isi dokumen PDF (teks, tabel, struktur halaman).
metadata:
  author: ai-agent-skills
  version: "1.0.0"
  license: UNLICENSED
---

# PDF Reader

Baca dokumen PDF dan ekstrak teks serta struktur halamannya.

## Kapan dipakai

- Membaca laporan, kontrak, atau modul
- Menyalin isi tabel / teks ke berkas lain
- Memeriksa isi sebelum tindakan lanjutan

## Cara kerja

1. Lokasikan file PDF.
2. Baca isi (read_file, atau tool ekstraksi PDF tertentu).
3. Ringkas: jumlah halaman, bagian tabel / teks.
4. Tulis ke file / ringkasan sesuai kebutuhan.

## Pengecekan

- File valid (bukan corrupt).
- Teks cocok dengan isi yang diharapkan.
- Jika PDF tidak punya teks (hanya gambar), catat bahwa OCR diperlukan.

## Dependencies

- read_file atau tool ekstraksi PDF
