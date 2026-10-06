print("=" * 60)
print("PROGRAM VALIDASI DATA MAHASISWA")
print("=" * 60)


def validasi_data(nim, ipk, sks, semester):
    error_list = []

    # Validasi NIM
    if not isinstance(nim, str):
        error_list.append("NIM harus berupa teks.")
    else:
        if len(nim) != 10:
            error_list.append("NIM harus terdiri dari 10 digit.")

        if not nim.isdigit():
            error_list.append("NIM hanya boleh berisi angka.")

        if nim.isdigit() and len(nim) >= 4:
            tahun = int(nim[:4])

            if tahun < 2000 or tahun > 2037:
                error_list.append(
                    "Tahun pada NIM harus berada antara 2000-2037."
                )

    # Validasi IPK
    try:
        ipk = float(ipk)

        if ipk < 0.0 or ipk > 4.0:
            error_list.append("IPK harus berada antara 0.0-4.0.")

    except ValueError:
        error_list.append("IPK harus berupa angka.")

    # Validasi SKS
    try:
        sks = int(sks)

        if sks < 0 or sks > 24:
            error_list.append("SKS harus berada antara 0-24.")

    except ValueError:
        error_list.append("SKS harus berupa angka.")

    # Validasi semester
    try:
        semester = int(semester)

        if semester < 1 or semester > 14:
            error_list.append("Semester harus berada antara 1-14.")

    except ValueError:
        error_list.append("Semester harus berupa angka.")

    # Hasil validasi
    if len(error_list) == 0:
        return True, "Data mahasiswa valid."
    else:
        return False, "Alasan: " + "; ".join(error_list)


# ============================================================
# INPUT DATA
# ============================================================

nim = input("NIM       : ")
ipk = input("IPK       : ")
sks = input("SKS       : ")
semester = input("Semester  : ")

# Memanggil fungsi validasi
valid, pesan = validasi_data(nim, ipk, sks, semester)

print("\n" + "=" * 60)
print("HASIL VALIDASI")
print("=" * 60)

if valid:
    print("Status : VALID")
    print(pesan)
else:
    print("Status : TIDAK VALID")
    print(pesan)