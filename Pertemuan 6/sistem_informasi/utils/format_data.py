def tampilkan_mahasiswa(data):
    if not data:
        print("Belum ada data mahasiswa")
        return

    if isinstance(data, dict):
        data = [data]

    for mahasiswa in data:
        print(
            f"NIM: {mahasiswa['nim']} | "
            f"Nama: {mahasiswa['nama']} | "
            f"Jurusan: {mahasiswa['jurusan']}"
        )