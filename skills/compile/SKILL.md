---
name: compile
description: Bangun atau proses project (JavaScript, Python, web, dan lain-lain) sampai berhasil.
metadata:
  author: ai-agent-skills
  version: "1.0.0"
  license: UNLICENSED
---

# Compile

Bangun atau proses sebuah project sampai menghasilkan output yang dapat
dijalankan / didistribusikan.

## Kapan dipakai

- Menjalankan `npm run build`
- Menginstall dependensi (npm install / pip install)
- Menjalankan test / lint
- Memproses berkas (minifikasi, konversi, dst)

## Cara kerja

1. Lihat konfigurasi build (package.json, pyproject.toml, dst).
2. Install dependensi jika belum ada.
3. Jalankan perintah build dari repo.
4. Periksa output: tidak ada error, output ada.
5. Cek hasil (browser / console) kalau perlu.

## Pengecekan

- Exit code 0 / tidak ada error di log.
- Output dapat diakses (file, URL, atau console).
- Laporkan langkah build + hasil.

## Dependencies

- Terminal (bash / zsh)
- Node/npm, Python, atau tool lain yang dibutuhkan
