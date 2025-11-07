import os
from PyPDF2 import PdfReader

def show_banner():
    print("=" * 50)
    print("💀  A L D I   W A S   H E R E  💀".center(50))
    print("=" * 50)
    print()

show_banner()

folder_path = input("Masukkan lokasi folder yang berisi file PDF: ").strip('"').strip("'")

if not os.path.isdir(folder_path):
    print(f"\n🚫 Folder tidak ditemukan: {folder_path}")
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

print("-" * 50)
print(f"Total file PDF: {file_count}")
print(f"Total seluruh halaman: {total_pages}")
print("-" * 50)
print("\n🔥 Selesai! Terhitung oleh skrip legendaris milik ALDI 💪")
