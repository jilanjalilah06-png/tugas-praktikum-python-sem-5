
# Daftar nilai mahasiswa
nilai = [85, 90, 75, 60, 95, 80, 70, 55, 90, 65]

# Menghitung statistik
rata_rata = sum(nilai) / len(nilai)
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

# Fungsi untuk menentukan kategori nilai
def kategori_nilai(n):
    if n >= 85:
        return "A"
    elif n >= 75:
        return "B"
    elif n >= 65:
        return "C"
    elif n >= 50:
        return "D"
    else:
        return "E"

# Mengelompokkan nilai ke dalam kategori
frekuensi = {}

for n in nilai:
    kategori = kategori_nilai(n)

    if kategori in frekuensi:
        frekuensi[kategori] += 1
    else:
        frekuensi[kategori] = 1

# Menampilkan hasil
print("Daftar nilai       :", nilai)
print("Rata-rata          :", round(rata_rata, 2))
print("Nilai tertinggi    :", nilai_tertinggi)
print("Nilai terendah     :", nilai_terendah)

print("\nFrekuensi kategori:")
for kategori in ["A", "B", "C", "D", "E"]:
    print(f"Kategori {kategori}: {frekuensi.get(kategori, 0)} mahasiswa")
