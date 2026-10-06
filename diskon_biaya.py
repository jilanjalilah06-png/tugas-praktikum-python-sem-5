print("=" * 60)
print("PROGRAM HITUNG DISKON BIAYA KULIAH")
print("=" * 60)

# Input data
spp = float(input("Masukkan biaya SPP       : Rp "))

anak_karyawan = input("Anak karyawan? (y/n)    : ").lower()
ipk = float(input("Masukkan IPK             : "))
tepat_waktu = input("Bayar tepat waktu? (y/n) : ").lower()

# Konstanta diskon
DISKON_ANAK_KARYAWAN = 0.25
DISKON_PRESTASI_TINGGI = 0.20
DISKON_PRESTASI_BAIK = 0.15
DISKON_MEMUASKAN = 0.10
DISKON_TEPAT_WAKTU = 0.05

# Menentukan diskon utama
diskon_utama = 0
nama_diskon = "Tidak ada"

if anak_karyawan == "y":
    diskon_utama = DISKON_ANAK_KARYAWAN
    nama_diskon = "Anak Karyawan"
elif ipk >= 3.8:
    diskon_utama = DISKON_PRESTASI_TINGGI
    nama_diskon = "Prestasi Tinggi"
elif ipk >= 3.5:
    diskon_utama = DISKON_PRESTASI_BAIK
    nama_diskon = "Prestasi Baik"
elif ipk >= 3.0:
    diskon_utama = DISKON_MEMUASKAN
    nama_diskon = "IPK Memuaskan"

# Diskon tambahan tepat waktu
diskon_tambahan = 0

if tepat_waktu == "y":
    diskon_tambahan = DISKON_TEPAT_WAKTU

# Total diskon
total_diskon = diskon_utama + diskon_tambahan

# Menghitung nominal diskon
jumlah_diskon = spp * total_diskon

# Menghitung biaya akhir
biaya_akhir = spp - jumlah_diskon

# Menampilkan hasil
print("\n" + "=" * 60)
print("HASIL PERHITUNGAN")
print("=" * 60)

print(f"Biaya SPP          : Rp {spp:,.0f}")
print(f"Diskon utama       : {diskon_utama * 100:.0f}% ({nama_diskon})")
print(f"Diskon tepat waktu : {diskon_tambahan * 100:.0f}%")
print(f"Total diskon       : {total_diskon * 100:.0f}%")
print(f"Jumlah diskon      : Rp {jumlah_diskon:,.0f}")
print(f"Biaya akhir        : Rp {biaya_akhir:,.0f}")

print("=" * 60)