
import re
from collections import Counter

# Membaca teks dari file
try:
    with open("teks.txt", "r", encoding="utf-8") as file:
        teks = file.read()
except FileNotFoundError:
    print("File teks.txt tidak ditemukan.")
    raise SystemExit

# 1. STRING: mengubah teks menjadi huruf kecil
teks_bersih = teks.lower()

# 2. LIST: memisahkan teks menjadi daftar kata
kata = re.findall(r"\b\w+\b", teks_bersih)

# 3. SET: mendapatkan kata-kata unik
kata_unik = set(kata)

# 4. DICTIONARY: menyimpan frekuensi setiap kata
frekuensi = dict(Counter(kata))

# Menampilkan 10 kata yang paling sering muncul
kata_teratas = Counter(kata).most_common(10)

# Mengidentifikasi kata yang hanya muncul satu kali
hapax = sorted(
    [k for k, jumlah in frekuensi.items() if jumlah == 1]
)

# Menghitung type-token ratio
jumlah_token = len(kata)
jumlah_tipe = len(kata_unik)

if jumlah_token > 0:
    ttr = jumlah_tipe / jumlah_token
else:
    ttr = 0

# Menampilkan hasil analisis
print("=== HASIL ANALISIS TEKS ===")
print("Jumlah seluruh kata (token):", jumlah_token)
print("Jumlah kata unik (tipe)    :", jumlah_tipe)

print("\n=== 10 KATA PALING SERING MUNCUL ===")
for nama_kata, jumlah in kata_teratas:
    print(f"{nama_kata}: {jumlah}")

print("\n=== HAPAX LEGOMENA ===")
print("Kata yang muncul sekali:", hapax)
print("Jumlah hapax:", len(hapax))

print("\n=== TYPE-TOKEN RATIO ===")
print("TTR desimal :", round(ttr, 4))
print("TTR persen  :", round(ttr * 100, 2), "%")
