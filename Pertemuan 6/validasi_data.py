
def validasi_data(data, schema, *args, **kwargs):
    errors = []

    # Memeriksa setiap aturan pada schema
    for field, aturan in schema.items():
        if field not in data:
            errors.append(f"{field} wajib diisi")
            continue

        nilai = data[field]
        tipe = aturan.get("type")

        # Memeriksa tipe data
        if tipe and not isinstance(nilai, tipe):
            errors.append(
                f"{field} harus bertipe {tipe.__name__}"
            )
            continue

        # Memeriksa nilai minimum
        if "min" in aturan and nilai < aturan["min"]:
            errors.append(
                f"{field} minimal {aturan['min']}"
            )

        # Memeriksa nilai maksimum
        if "max" in aturan and nilai > aturan["max"]:
            errors.append(
                f"{field} maksimal {aturan['max']}"
            )

    # Validasi tambahan dari *args
    for fungsi in args:
        hasil = fungsi(data)
        if hasil is not True:
            errors.append(str(hasil))

    # Validasi tambahan dari **kwargs
    for field, wajib in kwargs.items():
        if wajib and field not in data:
            errors.append(f"{field} wajib tersedia")

    return len(errors) == 0, errors


if __name__ == "__main__":
    mahasiswa = {
        "nama": "Jilan",
        "umur": 20,
        "ipk": 3.75
    }

    schema = {
        "nama": {"type": str},
        "umur": {"type": int, "min": 17, "max": 30},
        "ipk": {"type": float, "min": 0.0, "max": 4.0}
    }

    valid, errors = validasi_data(
        mahasiswa,
        schema,
        lambda data: True,
        fakultas=True
    )

    print("Data valid:", valid)
    print("Errors:", errors)
