import os
from datetime import datetime
from PyPDF2 import PdfReader
def show_banner():
    print("=" * 60)
    print("💀  A L D I   W A S   H E R E  💀".center(60))
    print("=" * 60)
    print()
show_banner()
folders=[]
while True:
    folder_path=input("Masukkan lokasi folder yang berisi file PDF: ").strip('"').strip("'")
    if not folder_path:
        if folders:break
        else:print("🚫 Harus masukkan minimal satu folder!");continue
    if not os.path.isdir(folder_path):print(f"🚫 Folder tidak ditemukan: {folder_path}");continue
    if folder_path in folders:print("⚠️ Folder ini sudah dimasukkan sebelumnya.")
    else:folders.append(folder_path);print("✅ Folder ditambahkan!")
    tambah=input("Masukkan lokasi folder lain (tekan ENTER jika sudah semua): ").strip('"').strip("'")
    if not tambah:break
    else:
        if os.path.isdir(tambah):
            if tambah not in folders:folders.append(tambah);print("✅ Folder ditambahkan!")
            else:print("⚠️ Folder ini sudah dimasukkan sebelumnya.")
        else:print(f"🚫 Folder tidak ditemukan: {tambah}")
print("\n🔍 Sedang menghitung jumlah lembar setiap file...\n")
results=[];grand_files=0;grand_pages=0
for folder in folders:
    total_pages=0;file_count=0;folder_name=os.path.basename(folder.rstrip("/\\"))
    print(f"\n📁 {folder_name}");print("\\")
    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            file_path=os.path.join(folder,filename)
            try:
                reader=PdfReader(file_path);num_pages=len(reader.pages)
                print(f"{filename}: {num_pages} lembar")
                total_pages+=num_pages;file_count+=1
            except Exception as e:print(f"Gagal membaca {filename}: {e}")
    results.append({"folder":folder_name,"file_count":file_count,"total_pages":total_pages})
    grand_files+=file_count;grand_pages+=total_pages
print("\n\n🔥 HASIL AKHIR 🔥\n")
for r in results:
    print(f"{r['folder']}");print("-"*50)
    print(f"Total file PDF: {r['file_count']}");print(f"Total seluruh lembar: {r['total_pages']}")
    print("-"*50);print()
print("📊 REKAP AKHIR")
print("-"*50)
print(f"Total semua file PDF: {grand_files}")
print(f"Total semua lembar: {grand_pages}")
print("-"*50)
print("📅 Dihitung otomatis oleh script legendaris: ALDI WAS HERE 💪")
print(f"🕓 {datetime.now().strftime('%A, %d %B %Y')}")
