from sistem_informasi.service import (
    tambah_mahasiswa,
    lihat_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa
)
from sistem_informasi.utils import tampilkan_mahasiswa


if __name__ == "__main__":
    # CREATE
    print(tambah_mahasiswa(
        "26001", "Jilan", "Sistem Informasi"
    ))
    print(tambah_mahasiswa(
        "26002", "Alya", "Informatika"
    ))

    # READ
    print("\n=== DATA MAHASISWA ===")
    tampilkan_mahasiswa(lihat_mahasiswa())

    # UPDATE
    print("\n=== UPDATE ===")
    print(ubah_mahasiswa(
        "26001", nama="Jilan Jalilah"
    ))
    tampilkan_mahasiswa(lihat_mahasiswa("26001"))

    # DELETE
    print("\n=== DELETE ===")
    print(hapus_mahasiswa("26002"))

    print("\n=== DATA AKHIR ===")
    tampilkan_mahasiswa(lihat_mahasiswa())