---
name: web-check
description: Ambil dan ringkas isi halaman web (teks, judul, gambar, struktur).
metadata:
  author: ai-agent-skills
  version: "1.0.0"
  license: UNLICENSED
---

# Web Check

Ambil konten halaman web dan ringkas: judul, poin utama, gambar/video,
link penting, dan halaman terkait.

## Kapan dipakai

- Memeriksa isi halaman sebelum disimpan atau dirangkum
- Memverifikasi data dari situs
- Menyiapkan ringkasan untuk laporan

## Cara kerja

1. Masukkan URL.
2. Ambil konten laman (`web_extract`).
3. Tandai judul, poin utama, media, dan link penting.
4. Catat asal / URL.

## Pengecekan

- URL valid.
- Konten cocok dengan URL yang diminta.
- Konten dinamis (script, menu, iklan) tidak diperlakukan sebagai isi utama.

## Dependencies

- Tool ekstraksi web (web_extract)
