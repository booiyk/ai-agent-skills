---
name: "hold"
version: "1.0.0"
description: "Jaga proses tetap berjalan di luar sesi terminal (nohup / tmux / bg + disown)."
---

## Kapan
Proses panjang (build, ekstraksi, download, simulasi).
Ingin keluar terminal tanpa mematikan proses.

## Langkah
1. Pilih salah satu metode:
   - nohup: nohup <cmd> > log.txt 2>&1 &
   - tmux: tmux new -s nama && <cmd>; lanjut tmux attach, tmux detach, tmux kill-session
   - bg + disown: <cmd> & disown
2. Pastikan proses masih berjalan.
3. Simpan log ke file.

## CLI
nohup python3 long-task.py > task.log 2>&1 &
tmux new -s build && npm run build
<cmd> & disown

## Contoh
Jalankan scrape data 1 jam tanpa mengunci terminal.

## Batasan
Proses tidak boleh bergantung pada shell yang mati.
Cek log secara berkala.

## Referensi
Terminal (bash / zsh).
