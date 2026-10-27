
import statistics
import math


def hitung_statistik(data):
    if not data:
        raise ValueError("Data tidak boleh kosong")

    mean = statistics.mean(data)
    median = statistics.median(data)

    try:
        modus = statistics.mode(data)
    except statistics.StatisticsError:
        modus = None

    rentang = max(data) - min(data)

    # Standard deviation populasi
    std_dev = math.sqrt(
        sum((x - mean) ** 2 for x in data) / len(data)
    )

    return {
        "mean": mean,
        "median": median,
        "modus": modus,
        "range": rentang,
        "standard_deviation": std_dev
    }


if __name__ == "__main__":
    nilai = [70, 80, 80, 90, 100]
    hasil = hitung_statistik(nilai)

    print("Data:", nilai)
    for nama, angka in hasil.items():
        print(f"{nama}: {angka}")
