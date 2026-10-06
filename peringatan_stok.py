print("=" * 70)
print("PROGRAM PERINGATAN STOK BARANG")
print("=" * 70)

BATAS_AMAN = 20
BATAS_PERINGATAN = 10

# Data inventaris
inventaris = [
    {
        "kode": "PRT001",
        "nama": "ProyektorCanon",
        "stok": 25,
        "harga": 2500000
    },
    {
        "kode": "PRT002",
        "nama": "Mouse",
        "stok": 15,
        "harga": 150000
    },
    {
        "kode": "PRT003",
        "nama": "PC Desktop",
        "stok": 8,
        "harga": 3000000
    },
    {
        "kode": "PRT004",
        "nama": "Laptop",
        "stok": 5,
        "harga": 18000000
    },
    {
        "kode": "PRT005",
        "nama": "Flashdisk",
        "stok": 20,
        "harga": 100000
    },
    {
        "kode": "PRT006",
        "nama": "Headset",
        "stok": 12,
        "harga": 300000
    },
    {
        "kode": "PRT007",
        "nama": "Kamera Digital",
        "stok": 0,
        "harga": 5000000
    },
    {
        "kode": "PRT008",
        "nama": "Kabel HDMI",
        "stok": 3,
        "harga": 75000
    }
]


def cek_status_stok(stok):
    if stok == 0:
        return "HABIS", "URGENT: Restock segera!", "CRITICAL"
    elif stok <= BATAS_PERINGATAN:
        return "RENDAH", "Restock dalam 1-3 hari", "HIGH"
    elif stok <= BATAS_AMAN:
        return "PERINGATAN", "Rencanakan restock 1-2 minggu", "MEDIUM"
    else:
        return "AMAN", "Stok mencukupi", "LOW"


total_nilai = 0
jumlah_aman = 0
jumlah_peringatan = 0
jumlah_rendah = 0
jumlah_habis = 0

print("\nLAPORAN STOK")
print("=" * 70)

for barang in inventaris:
    status, rekomendasi, prioritas = cek_status_stok(barang["stok"])

    nilai_barang = barang["stok"] * barang["harga"]
    total_nilai += nilai_barang

    if status == "AMAN":
        jumlah_aman += 1
    elif status == "PERINGATAN":
        jumlah_peringatan += 1
    elif status == "RENDAH":
        jumlah_rendah += 1
    elif status == "HABIS":
        jumlah_habis += 1

    print(f"\nKode        : {barang['kode']}")
    print(f"Nama        : {barang['nama']}")
    print(f"Stok        : {barang['stok']}")
    print(f"Harga       : Rp {barang['harga']:,.0f}")
    print(f"Nilai Stok  : Rp {nilai_barang:,.0f}")
    print(f"Status      : {status}")
    print(f"Prioritas   : {prioritas}")
    print(f"Rekomendasi : {rekomendasi}")

# Statistik
total_barang = len(inventaris)
jumlah_perlu_restock = jumlah_peringatan + jumlah_rendah + jumlah_habis
persentase_restock = (jumlah_perlu_restock / total_barang) * 100

print("\n" + "=" * 70)
print("RINGKASAN STATISTIK")
print("=" * 70)

print(f"Total jenis barang       : {total_barang}")
print(f"Stok aman                : {jumlah_aman}")
print(f"Stok peringatan          : {jumlah_peringatan}")
print(f"Stok rendah              : {jumlah_rendah}")
print(f"Stok habis               : {jumlah_habis}")
print(f"Perlu restock            : {jumlah_perlu_restock}")
print(f"Persentase perlu restock : {persentase_restock:.2f}%")
print(f"Total nilai inventaris   : Rp {total_nilai:,.0f}")

print("=" * 70)