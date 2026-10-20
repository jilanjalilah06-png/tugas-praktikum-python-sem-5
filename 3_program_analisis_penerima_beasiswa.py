
# ID mahasiswa penerima beasiswa
beasiswa_A = {101, 102, 103, 104, 105}
beasiswa_B = {104, 105, 106, 107, 108}

# Mahasiswa yang menerima kedua beasiswa
kedua_beasiswa = beasiswa_A & beasiswa_B

# Mahasiswa penerima A tetapi bukan B
hanya_A = beasiswa_A - beasiswa_B

# Seluruh mahasiswa unik penerima beasiswa
semua_penerima = beasiswa_A | beasiswa_B

# Menampilkan hasil
print("Penerima beasiswa A       :", sorted(beasiswa_A))
print("Penerima beasiswa B       :", sorted(beasiswa_B))
print("Menerima kedua beasiswa   :", sorted(kedua_beasiswa))
print("Hanya menerima beasiswa A :", sorted(hanya_A))
print("Semua penerima unik       :", sorted(semua_penerima))
print("Jumlah penerima unik      :", len(semua_penerima))
