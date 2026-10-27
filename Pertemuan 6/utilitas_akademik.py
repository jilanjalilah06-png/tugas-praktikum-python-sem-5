
def hitung_ipk(nilai_list):
    if not nilai_list:
        return 0.0

    return sum(nilai_list) / len(nilai_list)


def konversi_nilai_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def generate_transkrip(nama, nim, mata_kuliah):
    transkrip = {
        "nama": nama,
        "nim": nim,
        "mata_kuliah": mata_kuliah,
        "ipk": hitung_ipk(
            [mk["nilai"] for mk in mata_kuliah]
        )
    }

    return transkrip


if __name__ == "__main__":
    print("Testing modul akademik")
    print(hitung_ipk([85, 90, 80]))
    print(konversi_nilai_huruf(90))
