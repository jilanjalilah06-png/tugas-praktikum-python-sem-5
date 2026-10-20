
# Data inventaris toko
inventaris = {
    "Buku": {"harga": 15000, "stok": 10},
    "Pensil": {"harga": 3000, "stok": 20},
    "Tas": {"harga": 120000, "stok": 5}
}

# (a) Menambahkan barang baru
inventaris["Penghapus"] = {
    "harga": 2000,
    "stok": 15
}

# (b) Memperbarui stok barang
inventaris["Buku"]["stok"] = 12

# (c) Mencari barang berdasarkan rentang harga
harga_min = 5000
harga_max = 100000

print("=== BARANG DALAM RENTANG HARGA ===")

for nama, data in inventaris.items():
    if harga_min <= data["harga"] <= harga_max:
        print(
            f"{nama}: Rp{data['harga']:,} "
            f"| Stok: {data['stok']}"
        )

# (d) Menghitung total nilai inventaris
total_inventaris = sum(
    data["harga"] * data["stok"]
    for data in inventaris.values()
)

print("\n=== DAFTAR INVENTARIS ===")

for nama, data in inventaris.items():
    print(
        f"{nama}: Harga Rp{data['harga']:,}, "
        f"Stok {data['stok']}"
    )

print(f"\nTotal nilai inventaris: Rp{total_inventaris:,}")
