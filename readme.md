
# 🧾 PDF Page Counter (Total Halaman Otomatis)

Script Python canggih untuk menghitung **jumlah halaman dari semua file PDF** di dalam folder dan subfolder secara otomatis.  
Cocok buat kamu yang sering arsip dokumen, laporan, atau scanning data besar 📚  

![Screenshot](https://upld.zone.id/uploads/sriqd61iq/screenshot-2025-11-11-091918.webp)

---

## 🚀 Fitur Terbaru

✅ Hitung jumlah halaman dari semua PDF (termasuk dalam subfolder)  
✅ Filter berdasarkan **tanggal pembuatan (created date)**  
✅ Rekap tambahan untuk file yang **dimodifikasi** di tanggal yang sama  
✅ Deteksi otomatis file **hilang, duplikat, dan anomali nama**  
✅ Output hasil **berwarna dan terformat rapi di terminal**  
✅ Menampilkan **total per folder + total keseluruhan di bagian akhir**

---

## 🧠 Cara Kerja Singkat

1. Script akan menanyakan **folder root utama** yang berisi subfolder PDF atau folder utama yang berisi file pdf.  
2. Kamu bisa pilih untuk **scan semua subfolder** atau hanya folder utama.  
3. Pilih **filter tanggal**:
   - Hari ini, atau  
   - Tanggal tertentu (misal: `07-11-2025`)  
4. Script akan menampilkan hasil:
   - Total file PDF berdasarkan **tanggal pembuatan**
   - Total file yang **dimodifikasi**
   - Total halaman
   - File hilang, duplikat, dan anomali  

---

## 🛠️ Instalasi

Pastikan kamu sudah punya [Python 3](https://www.python.org/downloads/).  
Lalu install dependensi:

```bash
pip install PyPDF2
````

Jika `pip` tidak terdeteksi:

```bash
py -m pip install PyPDF2
```

---

## ▶️ Cara Menjalankan

Jalankan di **Terminal / PowerShell / CMD**:

```bash
py hitunghalamanpdf.py
```

Lalu ikuti instruksi interaktif di layar 👇

### Contoh Input

```
╔═══════════════════════════════════════════════╗
║ Masukkan lokasi FOLDER ROOT yang berisi subfolder: ║
╚═══════════════════════════════════════════════╝
➡️  D:\Arsip\Dokumen

Scan semua subfolder juga? (default: Y) [Y/n]:
➡️  (tekan Enter)

Pilih filter tanggal file PDF:
1. Hanya yang diubah HARI INI
2. Berdasarkan tanggal tertentu (contoh: 03-11-2025)
➡️  2

Masukkan tanggal (contoh: 07-11-2025):
➡️  07-11-2025
```

---

## 📊 Contoh Output

```
🗂️  Folder: Laporan Bulanan (Filter: 2025-11-07)
──────────────────────────────────────────────
- laporan1.pdf                      3 lembar
- laporan2.pdf                      5 lembar
✅ Tidak ada file yang hilang.
✅ Tidak ada file duplikat terdeteksi.
✅ Semua file konsisten dengan pola awal.
✅ Pola numerik konsisten.

📊 REKAP AKHIR
--------------------------------------------------
Total semua file PDF berdasarkan pembuatan: 140
Total modified file PDF: 15
Total semua lembar: 275
Total file hilang: 3
Total file duplikat: 0
Total file anomali: 0
--------------------------------------------------
📅 Dihitung otomatis oleh script legendaris: **ALDI WAS HERE 💪**
🕓 Tuesday, 11 November 2025
```

---

## 💡 Catatan Penting

* Filter tanggal menggunakan **tanggal pembuatan (created date)**
  → File yang hanya dimodifikasi di tanggal itu **tidak dihitung di total utama**, tapi masuk **rekap tambahan**.
* File PDF rusak atau terenkripsi bisa dilewati otomatis.
* Gunakan terminal yang mendukung warna ANSI untuk tampilan berwarna 🌈
* Dapat dijalankan di **Windows, macOS, dan Linux**.

---

## 🧩 Teknologi yang Digunakan

* **Python 3.9+**
* **Library:** [PyPDF2](https://pypi.org/project/PyPDF2/)
* **ANSI Colors** untuk tampilan interaktif di terminal

---

## 🧑‍💻 Pembuat

**Aldi Setiadi Putra**
📍 SMK Negeri 3 Kota Tangerang Selatan
✨ “Setiap halaman adalah cerita, dan setiap hitungan adalah makna.”

---
