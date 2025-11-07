# 🧾 PDF Page Counter (Total Halaman Otomatis)

Script Python sederhana untuk menghitung **total jumlah halaman dari semua file PDF** di dalam sebuah folder.
Cocok buat kamu yang sering arsip, laporan, atau scanning dokumen 📚

---

## 🚀 Fitur

* Hitung jumlah halaman dari **banyak file PDF sekaligus**
* Minta lokasi folder secara **interaktif** saat dijalankan
* Tampilkan hasil total file dan total halaman secara otomatis
* Deteksi error kalau ada file PDF yang rusak atau tidak bisa dibaca

---

## 🛠️ Cara Penggunaan

### 1. Instalasi Dependensi

Pastikan kamu sudah menginstal [Python 3](https://www.python.org/downloads/).
Lalu install library yang dibutuhkan:

```bash
pip install PyPDF2
```
Karena kadang `pip` itu gak dikenali, bisa coba install pakai perintah ini:

```bash
py -m pip install PyPDF2
```
### 2. Jalankan Script

Jalankan program di terminal / PowerShell:

```bash
py hitunghalamanpdf.py
```

### 3. Masukkan Lokasi Folder

Saat diminta, ketik atau paste lokasi folder tempat file PDF kamu disimpan. Contoh:

`Masukkan lokasi folder yang berisi file PDF:`
```
D:\Arsip\Dokumen\Laporan Oktober 2025
```

---

## 📊 Contoh Output

```
🔍 Sedang menghitung jumlah halaman setiap file...

laporan1.pdf: 2 halaman
laporan2.pdf: 3 halaman
laporan3.pdf: 1 halaman
----------------------------------------
Total file PDF: 3
Total seluruh halaman: 6
```

---

## 🧩 Teknologi yang Digunakan

* Python 3.9+
* Library: [PyPDF2](https://pypi.org/project/PyPDF2/)

---

## 📁 Struktur Folder

```
PDF-Page-Counter/
│
├── hitunghalamanpdf.py       # Script utama
├── README.md           # Dokumentasi proyek
└── requirements.txt    # (opsional) daftar library yang dibutuhkan
```

---

## 💡 Catatan

* Jalankan script dengan izin akses ke folder tujuan.
* File PDF yang rusak atau terenkripsi mungkin tidak bisa dihitung.
* Bisa dimodifikasi agar hasilnya disimpan ke file `.txt` atau `.csv`.

---

## 🧑‍💻 Pembuat

**Aldi Setiadi Putra**
💬 SMK Negeri 3 Kota Tangerang Selatan
✨ “Setiap halaman adalah cerita, dan setiap hitungan adalah makna.”

---
