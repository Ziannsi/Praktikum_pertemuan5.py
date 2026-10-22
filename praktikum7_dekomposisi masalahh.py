def hitung_subtotal(harga, jumlah):
    return harga * jumlah

def hitung_diskon(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.10
    return 0

def tampilkan_struk(nama_barang, subtotal, diskon):
    total_akhir = subtotal - diskon
    print("=== STRUK PEMBELIAN ===")
    print("Barang      :", nama_barang)
    print("Subtotal    :", int(subtotal))
    print("Diskon      :", int(diskon))
    print("Total akhir :", int(total_akhir))
nama_barang = "Buku Tulis"
subtotal = hitung_subtotal(25000, 5)
diskon = hitung_diskon(subtotal)
tampilkan_struk(nama_barang, subtotal, diskon)