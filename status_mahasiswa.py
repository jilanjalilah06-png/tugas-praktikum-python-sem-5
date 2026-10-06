print("=" * 60)
print("STATUS DATA MAHASISWA")
print("=" * 60)

mahasiswa = []

# Input data 5 mahasiswa
for i in range(5):
    print(f"\nData Mahasiswa ke-{i + 1}")

    nim = input("NIM       : ")
    nama = input("Nama      : ")
    ipk = float(input("IPK       : "))
    sks = int(input("SKS       : "))

    # Menentukan status mahasiswa
    if ipk >= 2.0 and sks >= 18:
        status = "Aktif"
    elif 1.5 <= ipk < 2.0:
        status = "Peringatan"
    elif ipk < 1.5:
        status = "Tidak Aktif"
    else:
        status = "Tidak Aktif"

    mahasiswa.append({
        "nim": nim,
        "nama": nama,
        "ipk": ipk,
        "sks": sks,
        "status": status
    })

# Menampilkan hasil
print("\n" + "=" * 60)
print("HASIL STATUS MAHASISWA")
print("=" * 60)

for mhs in mahasiswa:
    print(f"NIM       : {mhs['nim']}")
    print(f"Nama      : {mhs['nama']}")
    print(f"IPK       : {mhs['ipk']:.2f}")
    print(f"SKS       : {mhs['sks']}")
    print(f"Status    : {mhs['status']}")
    print("-" * 60)