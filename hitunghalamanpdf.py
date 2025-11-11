import os
import re
import shutil
import math
from datetime import datetime, date
from PyPDF2 import PdfReader
def color_text(text, fg=None, bg=None, style=None):
    colors = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37
    }
    styles = {"bold": 1, "dim": 2, "underline": 4}
    reset = "\033[0m"
    seq = ""
    if style in styles:
        seq += f"\033[{styles[style]}m"
    if fg in colors:
        seq += f"\033[{colors[fg]}m"
    if bg in colors:
        seq += f"\033[{colors[bg] + 10}m"
    return f"{seq}{text}{reset}"
def show_banner():
    print(color_text("""
========================================
📄 HITUNG JUMLAH HALAMAN PDF OTOMATIS 📄
========================================
""", "yellow", style="bold"))
    print(color_text("Dibuat oleh: Aldi Setiadi Putra", "cyan"))
    print(color_text("----------------------------------------\n", "yellow"))
def extract_candidate_number(filename):
    if re.search(r"[a-f0-9]{8}-[a-f0-9]{4}", filename.lower()):
        return None
    matches = re.findall(r"\d{3,6}", filename)
    if not matches:
        return None
    for m in matches:
        try:
            val = int(m)
        except ValueError:
            continue
        if 100 <= val <= 300000:
            return val
    return None
def build_clusters(numbers, max_gap=200):
    nums = sorted(set(numbers))
    clusters = []
    if not nums:
        return clusters
    cur = [nums[0]]
    for n in nums[1:]:
        if n - cur[-1] <= max_gap:
            cur.append(n)
        else:
            clusters.append(cur)
            cur = [n]
    clusters.append(cur)
    return clusters
def pick_main_cluster(numbers):
    clusters = build_clusters(numbers)
    if not clusters:
        return []
    main = max(clusters, key=len)
    if len(main) < 3:
        return []
    return main
def safe_missing_from_cluster(cluster, max_gap=200):
    missing = []
    for a, b in zip(cluster, cluster[1:]):
        gap = b - a
        if 1 < gap <= max_gap:
            missing.extend(range(a + 1, b))
    return missing
def detect_duplicates(filenames):
    base_map = {}
    for f in filenames:
        m = re.search(r"(\d{4,6})", f)
        if m:
            k = m.group(1)
            base_map.setdefault(k, []).append(f)
    duplicates = []
    total_dup = 0
    for k, files in base_map.items():
        if len(files) > 1:
            duplicates.append({k: files})
            total_dup += len(files) - 1
    return duplicates, total_dup
def detect_anomalies(filenames, main_cluster):
    anomalies = []
    if not main_cluster:
        for f in filenames:
            n = extract_candidate_number(f)
            if n is None:
                anomalies.append(f)
        return anomalies, len(anomalies)
    min_c, max_c = min(main_cluster), max(main_cluster)
    for f in filenames:
        n = extract_candidate_number(f)
        if n is None:
            anomalies.append(f)
        elif n < (min_c - 50) or n > (max_c + 50):
            anomalies.append(f)
    return anomalies, len(anomalies)
def print_table(data, columns=3, padding=4, vertical=True):
    if not data:
        print(color_text("  (Tidak ada file PDF ditemukan)", "red"))
        return
    try:
        terminal_width = shutil.get_terminal_size((120, 20)).columns
    except Exception:
        terminal_width = 120
    col_width = max(20, (terminal_width - padding * (columns - 1)) // columns)
    if vertical:
        rows_count = math.ceil(len(data) / columns)
        cols = [data[i*rows_count:(i+1)*rows_count] for i in range(columns)]
        for i in range(rows_count):
            line = ""
            for j in range(columns):
                if i < len(cols[j]):
                    line += cols[j][i].ljust(col_width)
                else:
                    line += "".ljust(col_width)
            print(color_text(line, "white"))
    else:
        rows = [data[i:i+columns] for i in range(0, len(data), columns)]
        for row in rows:
            line = "".join(cell.ljust(col_width) for cell in row)
            print(color_text(line, "white"))
def input_folder():
    print(color_text("╔═══════════════════════════════════════════════╗", "cyan"))
    print(color_text("║ Masukkan lokasi FOLDER ROOT yang berisi subfolder: ║", "cyan"))
    print(color_text("╚═══════════════════════════════════════════════╝", "cyan"))
    folder = input(color_text("   ➡️  ", "green", style="bold")).strip('"').strip("'")
    return folder
def parse_date_string(s):
    s = s.strip()
    if not s:
        raise ValueError("empty")
    if s.lower() in ("today", "hari ini", "hariini", "now"):
        return datetime.now().date()
    formats = ["%d-%m-%Y", "%d-%m-%y", "%d %B %Y", "%d %b %Y", "%d %m %Y"]
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt).date()
        except Exception:
            continue
    s2 = s.replace("/", "-").replace(".", "-")
    try:
        return datetime.strptime(s2, "%d-%m-%y").date()
    except Exception:
        pass
    raise ValueError(f"Unsupported date format: {s}")
def input_date_filter():
    print(color_text("\nPilih filter tanggal file PDF:", "cyan"))
    print(color_text("1. Hanya yang diubah HARI INI", "green"))
    print(color_text("2. Berdasarkan tanggal tertentu (contoh: 03-11-2025 atau 3 November 2025)", "yellow"))
    print(color_text("Tekan ENTER untuk skip filter (semua file akan discan)", "magenta"))
    choice = input(color_text("   ➡️  ", "green", style="bold")).strip()
    if choice == "1":
        return datetime.now().date()
    elif choice == "2":
        date_str = input(color_text("Masukkan tanggal (contoh: 03-11-2025 atau 3 November 2025): ", "cyan")).strip()
        try:
            d = parse_date_string(date_str)
            return d
        except ValueError:
            print(color_text("❌ Format tanggal tidak dikenali. Gunakan format DD-MM-YYYY atau '3 November 2025'.", "red"))
            return None
    elif choice == "":
        return None
    else:
        try:
            d = parse_date_string(choice)
            return d
        except Exception:
            print(color_text("⚠️ Pilihan tidak dikenali, akan discan semua file.", "yellow"))
            return None
def find_pdf_folders(root_folder, recursive=True):  # 🆕
    """
    Returns list of folder paths that contain at least one .pdf file.
    If recursive=True: walk through subfolders (os.walk).
    If recursive=False: only immediate child folders are checked.
    """
    folders = []
    root_folder = os.path.abspath(root_folder)

    if recursive:
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for f in filenames:
                if f.lower().endswith(".pdf"):
                    folders.append(dirpath)
                    break
    else:
        try:
            for name in os.listdir(root_folder):
                path = os.path.join(root_folder, name)
                if os.path.isdir(path):
                    has_pdf = any(fn.lower().endswith(".pdf") for fn in os.listdir(path))
                    if has_pdf:
                        folders.append(path)
        except Exception:
            pass
    unique = sorted(set(folders))
    return unique
def process_folder(folder, date_filter=None):
    try:
        filenames = sorted([f for f in os.listdir(folder) if f.lower().endswith(".pdf")])
    except Exception as e:
        print(color_text(f"🚫 Gagal membaca folder {folder}: {e}", "red"))
        return {
            "folder": os.path.basename(folder),
            "total_files": 0,
            "total_pages": 0,
            "modified_match": 0,
            "missing": [], "missing_count": 0,
            "duplicates": [], "dup_count": 0,
            "anomalies": [], "anom_count": 0,
            "notes": color_text("Gagal akses folder.", "red")
        }
    file_page_list = []
    total_pages = 0
    filtered_files = []
    modified_match = 0 
    for fn in filenames:
        path = os.path.join(folder, fn)
        try:
            ctime = datetime.fromtimestamp(os.path.getctime(path)).date()
            mtime = datetime.fromtimestamp(os.path.getmtime(path)).date()
        except Exception:
            continue
        if date_filter is not None:
            if ctime != date_filter:
                if mtime == date_filter:
                    modified_match += 1
                continue
        filtered_files.append(fn)
        try:
            reader = PdfReader(path)
            pages = len(reader.pages)
        except Exception:
            pages = None
        file_page_list.append((fn, pages))
        if pages:
            total_pages += pages
    folder_name = os.path.basename(folder.rstrip("/\\"))
    if date_filter:
        print(color_text(f"\n🗂️  Folder: {folder_name} (Filter created at: {date_filter.isoformat()})", "blue", style="bold"))
    else:
        print(color_text(f"\n🗂️  Folder: {folder_name}", "blue", style="bold"))
    print(color_text("──────────────────────────────────────────────", "blue"))
    if not filtered_files:
        print(color_text("⚠️ Tidak ada file PDF dengan tanggal pembuatan yang cocok.", "yellow"))
        return {
            "folder": folder_name,
            "total_files": 0,
            "total_pages": 0,
            "modified_match": modified_match,
            "missing": [], "missing_count": 0,
            "duplicates": [], "dup_count": 0,
            "anomalies": [], "anom_count": 0,
            "notes": color_text("Tidak ada data sesuai tanggal.", "yellow")
        }
    formatted_files = []
    for fn, pages in file_page_list:
        page_text = (color_text(f"{pages} lembar", "green") if pages else color_text("❌ gagal baca", "red"))
        formatted_files.append(f"- {fn:<40}{page_text}")
    print_table(formatted_files)
    candidates = [extract_candidate_number(fn) for fn, _ in file_page_list if extract_candidate_number(fn)]
    main_cluster = pick_main_cluster(candidates)
    if not main_cluster or len(main_cluster) < 3:
        missing, missing_count = [], 0
        notes = color_text("ℹ️  Folder ini tidak memiliki pola numerik berurutan.", "yellow")
    else:
        missing = safe_missing_from_cluster(main_cluster)
        missing_count = len(missing)
        notes = color_text("✅ Pola numerik konsisten.", "green")
    duplicates, dup_count = detect_duplicates(filtered_files)
    anomalies, anom_count = detect_anomalies(filtered_files, main_cluster)
    return {
        "folder": folder_name,
        "total_files": len(filtered_files),
        "total_pages": total_pages,
        "modified_match": modified_match,
        "missing": missing, "missing_count": missing_count,
        "duplicates": duplicates, "dup_count": dup_count,
        "anomalies": anomalies, "anom_count": anom_count,
        "notes": notes
    }
def pretty_print_results(results):
    print(color_text("\n\n🔥 HASIL AKHIR 🔥\n", "magenta", style="bold"))
    total_files = total_pages = total_missing = total_dup = total_anom = 0
    for r in results:
        print(color_text(r['folder'], "cyan", style="bold"))
        print(color_text("--------------------------------------------------", "blue"))
        print(color_text(f"Total file PDF: {r['total_files']}", "white"))
        print(color_text(f"Total seluruh lembar: {r['total_pages']}", "white"))
        if r['missing']:
            print(color_text("📉 FILE TIDAK ADA:", "yellow", style="bold"))
            for m in r['missing']:
                print(color_text(f"- {m}.pdf", "yellow"))
            print(color_text(f"Total file hilang: {r['missing_count']}", "yellow"))
        else:
            print(color_text("✅ Tidak ada file yang hilang.", "green"))

        if r['dup_count']:
            print(color_text(f"⚠️ Total file duplikat: {r['dup_count']}", "yellow"))
        else:
            print(color_text("✅ Tidak ada file duplikat terdeteksi.", "green"))

        if r['anom_count']:
            print(color_text(f"🌀 Total file anomali: {r['anom_count']}", "red"))
            if r['anomalies']:
                for a in r['anomalies']:
                    print(color_text(f"- {a}", "red"))
        else:
            print(color_text("✅ Semua file konsisten dengan pola awal.", "green"))
        print(r["notes"])
        print(color_text("--------------------------------------------------\n", "blue"))
        total_files += r['total_files']
        total_pages += r['total_pages']
        total_missing += r['missing_count']
        total_dup += r['dup_count']
        total_anom += r['anom_count']
    print(color_text("📊 REKAP AKHIR", "magenta", style="bold"))
    print(color_text("--------------------------------------------------", "blue"))
    print(color_text(f"Total semua file PDF berdasarkan pembuatan: {total_files}", "white"))
    total_modified = sum(r.get('modified_match', 0) for r in results)
    print(color_text(f"Total modified file PDF di tanggal filter: {total_modified}", "yellow"))
    print(color_text(f"Total semua lembar: {total_pages}", "white"))
    print(color_text(f"Total file hilang: {total_missing}", "yellow"))
    print(color_text(f"Total file duplikat: {total_dup}", "yellow"))
    print(color_text(f"Total file anomali: {total_anom}", "red"))
    print(color_text("--------------------------------------------------", "blue"))
    print(color_text("📅 Dihitung otomatis oleh script legendaris: ALDI WAS HERE 💪", "cyan"))
    print(color_text(f"🕓 {datetime.now().strftime('%A, %d %B %Y')}", "white"))
if __name__ == "__main__":
    show_banner()
    while True:
        root = input_folder()
        if not root:
            print(color_text("🚫 Masukkan folder root minimal satu kali!", "red"))
            continue
        if not os.path.isdir(root):
            print(color_text(f"🚫 Folder tidak ditemukan: {root}", "red"))
            continue
        break
    ans = input(color_text("Scan semua subfolder juga? (default: Y) [Y/n]: ", "cyan")).strip().lower()
    recursive = False if ans == "n" else True
    date_filter = input_date_filter()
    pdf_folders = find_pdf_folders(root, recursive=recursive)  # 🆕
    if not pdf_folders:
        print(color_text("⚠️ Tidak ditemukan file PDF di dalam folder root/subfolder yang dipilih.", "yellow"))
    else:
        print(color_text(f"\n🔎 Ditemukan {len(pdf_folders)} folder berisi PDF. Akan diproses satu per satu...", "magenta"))
    results = []
    for f in pdf_folders:
        res = process_folder(f, date_filter)
        results.append(res)
    pretty_print_results(results)
