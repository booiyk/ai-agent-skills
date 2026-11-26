---
name: "compile"
version: "1.0.0"
description: "Bangun atau proses project (JavaScript, Python, web, dan lain-lain) sampai berhasil."
---

## Kapan
Menjalankan npm run build.
Menginstall dependensi (npm install / pip install).
Menjalankan test / lint.
Memproses berkas (minifikasi, konversi).

## Langkah
1. Lihat konfigurasi build (package.json, pyproject.toml).
2. Install dependensi jika belum ada.
3. Jalankan perintah build dari repo.
4. Periksa output: tidak ada error, output ada.
5. Cek hasil (browser / console) kalau perlu.

## CLI
npm install
npm run build
pip install -r requirements.txt
python -m pytest

## Contoh
Project web -> npm run build menghasilkan folder dist/.
Project Python -> pip install -e . lalu pytest.

## Batasan
Exit code 0 / tidak ada error di log.
Output harus dapat diakses (file, URL, atau console).

## Referensi
Terminal (bash / zsh).
Node/npm, Python, atau tool lain yang dibutuhkan.
