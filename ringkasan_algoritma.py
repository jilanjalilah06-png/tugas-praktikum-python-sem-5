# ringkasan_algoritma.py

print("=" * 60)
print("RINGKASAN ALGORITMA SISTEM INFORMASI MAHASISWA")
print("=" * 60)


# ==========================================================
# A. PERSENTASE MAHASISWA AKTIF VS TIDAK AKTIF
# ==========================================================

print("\n1. DATA STATUS MAHASISWA")

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

aktif = 0
tidak_aktif = 0

for i in range(jumlah_mahasiswa):
    print(f"\nData mahasiswa ke-{i + 1}")

    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    sks = int(input("SKS: "))

    if ipk >= 2.0 and sks >= 18:
        status = "Aktif"
        aktif += 1
    elif 1.5 <= ipk < 2.0:
        status = "Peringatan"
    else:
        status = "Tidak Aktif"
        tidak_aktif += 1

    print(f"Nama   : {nama}")
    print(f"Status : {status}")


total_mahasiswa = jumlah_mahasiswa

if total_mahasiswa > 0:
    persentase_aktif = (aktif / total_mahasiswa) * 100
    persentase_tidak_aktif = (tidak_aktif / total_mahasiswa) * 100
else:
    persentase_aktif = 0
    persentase_tidak_aktif = 0


# ==========================================================
# B. RATA-RATA DISKON YANG DIBERIKAN
# ==========================================================

print("\n" + "=" * 60)
print("2. DATA DISKON BIAYA")
print("=" * 60)

jumlah_data_diskon = int(input("Masukkan jumlah data mahasiswa: "))

total_diskon = 0

for i in range(jumlah_data_diskon):
    print(f"\nData mahasiswa ke-{i + 1}")

    biaya_spp = float(input("Biaya SPP: Rp "))
    ipk = float(input("IPK: "))

    anak_karyawan = input("Anak karyawan? (y/n): ").lower()
    tepat_waktu = input("Bayar tepat waktu? (y/n): ").lower()

    diskon = 0

    # Menentukan diskon utama
    if anak_karyawan == "y":
        diskon = 25
    elif ipk >= 3.8:
        diskon = 20
    elif ipk >= 3.5:
        diskon = 15
    elif ipk >= 3.0:
        diskon = 10

    # Tambahan diskon tepat waktu
    if tepat_waktu == "y":
        diskon += 5

    total_diskon += diskon

    jumlah_diskon = biaya_spp * diskon / 100
    biaya_akhir = biaya_spp - jumlah_diskon

    print(f"Diskon        : {diskon}%")
    print(f"Jumlah diskon : Rp {jumlah_diskon:,.0f}")
    print(f"Biaya akhir   : Rp {biaya_akhir:,.0f}")


if jumlah_data_diskon > 0:
    rata_rata_diskon = total_diskon / jumlah_data_diskon
else:
    rata_rata_diskon = 0


# ==========================================================
# C. PERSENTASE ITEM YANG MEMBUTUHKAN RESTOCK
# ==========================================================

print("\n" + "=" * 60)
print("3. DATA PERINGATAN STOK")
print("=" * 60)

jumlah_item = int(input("Masukkan jumlah item: "))

butuh_restock = 0

for i in range(jumlah_item):
    print(f"\nItem ke-{i + 1}")

    nama_item = input("Nama item: ")
    stok = int(input("Jumlah stok: "))

    if stok == 0:
        status = "HABIS"
        butuh_restock += 1
    elif stok <= 10:
        status = "RENDAH"
        butuh_restock += 1
    elif stok <= 20:
        status = "PERINGATAN"
    else:
        status = "AMAN"

    print(f"Item   : {nama_item}")
    print(f"Status : {status}")


if jumlah_item > 0:
    persentase_restock = (butuh_restock / jumlah_item) * 100
else:
    persentase_restock = 0


# ==========================================================
# D. TABEL RINGKASAN HASIL
# ==========================================================

print("\n")
print("=" * 70)
print("                    TABEL RINGKASAN ALGORITMA")
print("=" * 70)

print(f"{'No':<5}{'Ringkasan':<45}{'Hasil':>15}")
print("-" * 70)

print(
    f"{'1':<5}"
    f"{'Persentase Mahasiswa Aktif':<45}"
    f"{persentase_aktif:>12.2f}%"
)

print(
    f"{'2':<5}"
    f"{'Persentase Mahasiswa Tidak Aktif':<45}"
    f"{persentase_tidak_aktif:>12.2f}%"
)

print(
    f"{'3':<5}"
    f"{'Rata-rata Diskon yang Diberikan':<45}"
    f"{rata_rata_diskon:>12.2f}%"
)

print(
    f"{'4':<5}"
    f"{'Persentase Item yang Membutuhkan Restock':<45}"
    f"{persentase_restock:>12.2f}%"
)

print("=" * 70)