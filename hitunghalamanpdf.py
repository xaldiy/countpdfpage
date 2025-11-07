import os
from PyPDF2 import PdfReader

# Minta input lokasi folder dari user
folder_path = input("Masukkan lokasi folder yang berisi file PDF: ").strip('"').strip("'")

# Cek apakah folder valid
if not os.path.isdir(folder_path):
    print(f"Folder tidak ditemukan: {folder_path}")
    exit()

total_pages = 0
file_count = 0

print("\n🔍 Sedang menghitung jumlah halaman setiap file...\n")

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        try:
            reader = PdfReader(file_path)
            num_pages = len(reader.pages)
            print(f"{filename}: {num_pages} halaman")
            total_pages += num_pages
            file_count += 1
        except Exception as e:
            print(f"Gagal membaca {filename}: {e}")

print("-" * 40)
print(f"Total file PDF: {file_count}")
print(f"Total seluruh halaman: {total_pages}")
