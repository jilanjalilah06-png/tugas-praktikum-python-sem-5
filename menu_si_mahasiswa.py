print("=" * 60)
print("SISTEM INFORMASI MAHASISWA")
print("=" * 60)


# ============================================================
# FUNGSI 1 - STATUS MAHASISWA
# ============================================================

def cek_status_mahasiswa():
    print("\n" + "=" * 60)
    print("CEK STATUS MAHASISWA")
    print("=" * 60)

    try:
        nim = input("NIM  : ")
        nama = input("Nama : ")
        ipk = float(input("IPK  : "))
        sks = int(input("SKS  : "))

        if ipk < 0 or ipk > 4:
            print("IPK harus berada di antara 0.0 sampai 4.0.")
            return

        if sks < 0:
            print("SKS tidak boleh kurang dari 0.")
            return

        if ipk >= 2.0 and sks >= 18:
            status = "Aktif"
        elif 1.5 <= ipk < 2.0:
            status = "Peringatan"
        else:
            status = "Tidak Aktif"

        print("\nHasil:")
        print(f"NIM    : {nim}")
        print(f"Nama   : {nama}")
        print(f"IPK    : {ipk:.2f}")
        print(f"SKS    : {sks}")
        print(f"Status : {status}")

    except ValueError:
        print("Input IPK dan SKS harus berupa angka.")


# ============================================================
# FUNGSI 2 - HITUNG DISKON
# ============================================================

def hitung_diskon():
    print("\n" + "=" * 60)
    print("HITUNG DISKON BIAYA")
    print("=" * 60)

    try:
        spp = float(input("Biaya SPP       : Rp "))
        anak_karyawan = input("Anak karyawan? (y/n)    : ").lower()
        ipk = float(input("IPK             : "))
        tepat_waktu = input("Bayar tepat waktu? (y/n) : ").lower()

        if spp < 0:
            print("Biaya SPP tidak boleh negatif.")
            return

        if ipk < 0 or ipk > 4:
            print("IPK harus berada di antara 0.0 sampai 4.0.")
            return

        if anak_karyawan == "y":
            diskon_utama = 0.25
            nama_diskon = "Anak Karyawan"
        elif ipk >= 3.8:
            diskon_utama = 0.20
            nama_diskon = "Prestasi Tinggi"
        elif ipk >= 3.5:
            diskon_utama = 0.15
            nama_diskon = "Prestasi Baik"
        elif ipk >= 3.0:
            diskon_utama = 0.10
            nama_diskon = "IPK Memuaskan"
        else:
            diskon_utama = 0
            nama_diskon = "Tidak ada"

        if tepat_waktu == "y":
            diskon_tambahan = 0.05
        else:
            diskon_tambahan = 0

        total_diskon = diskon_utama + diskon_tambahan
        jumlah_diskon = spp * total_diskon
        biaya_akhir = spp - jumlah_diskon

        print("\nHasil:")
        print(f"Biaya SPP          : Rp {spp:,.0f}")
        print(f"Diskon utama       : {diskon_utama * 100:.0f}%")
        print(f"Jenis diskon       : {nama_diskon}")
        print(f"Diskon tepat waktu : {diskon_tambahan * 100:.0f}%")
        print(f"Total diskon       : {total_diskon * 100:.0f}%")
        print(f"Jumlah diskon      : Rp {jumlah_diskon:,.0f}")
        print(f"Biaya akhir        : Rp {biaya_akhir:,.0f}")

    except ValueError:
        print("Input biaya SPP dan IPK harus berupa angka.")


# ============================================================
# FUNGSI 3 - PERINGATAN STOK
# ============================================================

def cek_peringatan_stok():
    print("\n" + "=" * 60)
    print("CEK PERINGATAN STOK")
    print("=" * 60)

    inventaris = [
        {"kode": "BRG001", "nama": "Laptop", "stok": 25, "harga": 7500000},
        {"kode": "BRG002", "nama": "Mouse", "stok": 15, "harga": 150000},
        {"kode": "BRG003", "nama": "Keyboard", "stok": 8, "harga": 250000},
        {"kode": "BRG004", "nama": "Monitor", "stok": 5, "harga": 1800000},
        {"kode": "BRG005", "nama": "Flashdisk", "stok": 20, "harga": 100000},
        {"kode": "BRG006", "nama": "Headset", "stok": 12, "harga": 300000},
        {"kode": "BRG007", "nama": "Webcam", "stok": 0, "harga": 500000},
        {"kode": "BRG008", "nama": "Kabel HDMI", "stok": 3, "harga": 75000}
    ]

    total_nilai = 0
    perlu_restock = 0

    for barang in inventaris:

        if barang["stok"] == 0:
            status = "HABIS"
            prioritas = "CRITICAL"
        elif barang["stok"] <= 10:
            status = "RENDAH"
            prioritas = "HIGH"
        elif barang["stok"] <= 20:
            status = "PERINGATAN"
            prioritas = "MEDIUM"
        else:
            status = "AMAN"
            prioritas = "LOW"

        nilai = barang["stok"] * barang["harga"]
        total_nilai += nilai

        if barang["stok"] <= 20:
            perlu_restock += 1

        print(
            f"{barang['kode']} | "
            f"{barang['nama']} | "
            f"Stok: {barang['stok']} | "
            f"{status} | "
            f"{prioritas}"
        )

    persentase = (perlu_restock / len(inventaris)) * 100

    print("\nRingkasan:")
    print(f"Total nilai inventaris : Rp {total_nilai:,.0f}")
    print(f"Perlu restock          : {perlu_restock} barang")
    print(f"Persentase restock     : {persentase:.2f}%")


# ============================================================
# MENU UTAMA
# ============================================================

while True:

    print("\n" + "=" * 60)
    print("MENU SISTEM INFORMASI MAHASISWA")
    print("=" * 60)
    print("1. Cek Status Mahasiswa")
    print("2. Hitung Diskon Biaya")
    print("3. Cek Peringatan Stok")
    print("0. Keluar")
    print("=" * 60)

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        cek_status_mahasiswa()

    elif pilihan == "2":
        hitung_diskon()

    elif pilihan == "3":
        cek_peringatan_stok()

    elif pilihan == "0":
        print("\nProgram selesai. Terima kasih!")
        break

    else:
        print("\nPilihan tidak tersedia. Silakan pilih 0-3.")