from sistem_informasi.model import buat_mahasiswa

# Penyimpanan data sementara
database_mahasiswa = {}


def tambah_mahasiswa(nim, nama, jurusan):
    if nim in database_mahasiswa:
        return "NIM sudah terdaftar"

    mahasiswa = buat_mahasiswa(nim, nama, jurusan)
    database_mahasiswa[nim] = mahasiswa
    return "Mahasiswa berhasil ditambahkan"


def lihat_mahasiswa(nim=None):
    if nim is None:
        return list(database_mahasiswa.values())

    return database_mahasiswa.get(nim, "Data tidak ditemukan")


def ubah_mahasiswa(nim, nama=None, jurusan=None):
    if nim not in database_mahasiswa:
        return "Data tidak ditemukan"

    if nama is not None:
        database_mahasiswa[nim]["nama"] = nama

    if jurusan is not None:
        database_mahasiswa[nim]["jurusan"] = jurusan

    return "Data berhasil diubah"


def hapus_mahasiswa(nim):
    if nim not in database_mahasiswa:
        return "Data tidak ditemukan"

    del database_mahasiswa[nim]
    return "Data berhasil dihapus"