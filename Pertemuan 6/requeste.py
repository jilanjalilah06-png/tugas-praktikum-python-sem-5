
import requests
import json


def main():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        # Mengambil informasi nama, email, dan kota
        hasil_map = list(map(
            lambda user: {
                "nama": user["name"],
                "email": user["email"],
                "kota": user["address"]["city"]
            },
            data
        ))

        # Memilih pengguna dengan nama lebih dari 15 karakter
        hasil_filter = list(filter(
            lambda user: len(user["nama"]) > 15,
            hasil_map
        ))

        # Mengurutkan berdasarkan nama
        hasil_sorted = sorted(
            hasil_filter,
            key=lambda user: user["nama"]
        )

        # Menyimpan hasil ke file JSON
        with open("hasil_users.json", "w", encoding="utf-8") as file:
            json.dump(
                hasil_sorted,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Jumlah data dari API:", len(data))
        print("Jumlah data setelah filter:", len(hasil_sorted))
        print("\n=== HASIL ANALISIS ===")

        for user in hasil_sorted:
            print(
                f"Nama: {user['nama']} | "
                f"Email: {user['email']} | "
                f"Kota: {user['kota']}"
            )

        print("\nHasil berhasil disimpan ke hasil_users.json")

    except requests.RequestException as error:
        print("Gagal mengambil data API:", error)

    except (ValueError, KeyError) as error:
        print("Gagal memproses data:", error)


if __name__ == "__main__":
    main()
