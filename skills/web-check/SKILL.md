---
name: "web-check"
version: "1.0.0"
description: "Ambil dan ringkas isi halaman web (teks, judul, gambar, struktur)."
---

## Kapan
Memeriksa isi halaman sebelum disimpan atau dirangkum.
Memverifikasi data dari situs.
Menyiapkan ringkasan untuk laporan.

## Langkah
1. Masukkan URL.
2. Ambil konten laman (web_extract).
3. Tandai judul, poin utama, media, dan link penting.
4. Catat asal / URL.

## CLI

## Contoh
URL: https://contoh.com/laporan.
Output: judul, poin utama, link terkait.

## Batasan
URL harus valid.
Konten dinamis (script, menu, iklan) tidak diperlakukan sebagai isi utama.
Konten yang diakses harus sesuai URL.

## Referensi
web_extract - alat ekstraksi halaman.
