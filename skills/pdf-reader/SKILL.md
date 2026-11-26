---
name: "pdf-reader"
version: "1.0.0"
description: "Baca isi dokumen PDF (teks, tabel, struktur halaman)."
---

## Kapan
Membaca laporan, kontrak, atau modul.
Menyalin isi tabel / teks ke berkas lain.
Memeriksa isi sebelum tindakan lanjutan.

## Langkah
1. Lokasikan file PDF.
2. Baca isi (read_file atau tool ekstraksi PDF).
3. Ringkas: jumlah halaman, bagian teks / tabel.
4. Tulis ke file / ringkasan sesuai kebutuhan.

## CLI

## Contoh
Baca laporan.pdf -> ekstrak teks + judul halaman -> simpan ke ringkasan.txt.

## Batasan
File PDF harus valid (bukan corrupt).
- Jika PDF tidak punya teks (hanya gambar), OCR diperlukan.

## Referensi
read_file atau tool ekstraksi PDF.
