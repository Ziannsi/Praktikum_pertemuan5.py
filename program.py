def tampilkan_soal(nomor, teks_soal, pilihan):
    print(f"Soal {nomor}:")
    print(teks_soal)
    for huruf, teks in pilihan.items():
        print(f"{huruf}. {teks}")


def periksa_jawaban(jawaban_mahasiswa, kunci_jawaban):
    if jawaban_mahasiswa == kunci_jawaban:
        return True
    else:
        return False


def hitung_skor(jumlah_benar, jumlah_soal):
    skor = (jumlah_benar / jumlah_soal) * 100
    return skor


def main():
    nomor = 1
    pilihan = {
        "A": "Jakarta",
        "B": "Bandung",
        "C": "Surabaya",
        "D": "Medan",
    }
    tampilkan_soal(nomor, "Apa ibukota Indonesia?", pilihan)
    jawaban = input("Jawaban Anda: ").strip().upper()
    hasil = periksa_jawaban(jawaban, "A")

    if hasil:
        jumlah_benar = 1
        print("Jawaban benar!")
    else:
        jumlah_benar = 0
        print("Jawaban salah!")

    skor_akhir = hitung_skor(jumlah_benar, 1)
    print(f"Skor akhir: {skor_akhir}")


main()