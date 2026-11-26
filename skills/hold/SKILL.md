---
name: hold
description: Jaga proses tetap berjalan di luar sesi terminal (nohup / tmux / bg + disown).
metadata:
  author: ai-agent-skills
  version: "1.0.0"
  license: UNLICENSED
---

# Hold

Cara menjaga proses tetap berjalan meskipun terminal ditutup atau session
diakhiri.

## Kapan dipakai

- Proses panjang (build, ekstraksi, download, simulasi, dst)
- Ingin keluar terminal tanpa mematikan proses

## Cara kerja

Pilih salah satu:

- **nohup**: `nohup <cmd> > log.txt 2>&1 &`
- **tmux**: `tmux new -s nama && <cmd>`; lanjut `tmux attach`, `tmux detach`, `tmux kill-session`
- **bg + disown**: `<cmd> & disown`

## Pengecekan

- Proses terlihat di `ps` atau `jobs -l`.
- Log tertulis ke file.
- Tidak ada shell yang mati mematikan proses.

## Dependencies

- Terminal (bash / zsh)
