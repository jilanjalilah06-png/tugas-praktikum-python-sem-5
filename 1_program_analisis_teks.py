
import string

# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Menghitung jumlah huruf
jumlah_huruf = sum(1 for karakter in kalimat if karakter.isalpha())

# Menghitung jumlah kata
jumlah_kata = len(kalimat.split())

# Menghitung jumlah tanda baca
jumlah_tanda_baca = sum(
    1 for karakter in kalimat
    if karakter in string.punctuation
)

# Mengubah kalimat menjadi title case
kalimat_title = kalimat.title()

# Menampilkan hasil
print("\n=== HASIL ANALISIS TEKS ===")
print("Kalimat asli       :", kalimat)
print("Jumlah huruf       :", jumlah_huruf)
print("Jumlah kata        :", jumlah_kata)
print("Jumlah tanda baca  :", jumlah_tanda_baca)
print("Title case         :", kalimat_title)
