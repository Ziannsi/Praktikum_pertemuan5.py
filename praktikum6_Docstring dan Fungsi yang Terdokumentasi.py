def konversi_menit_ke_detik(menit):
    """
    Fungsi untuk mengkonversi waktu dari satuan menit ke detik.
    
    Parameter:
    menit (int/float): Jumlah waktu dalam satuan menit yang akan dikonversi.
    
    Nilai Kembalian:
    int/float: Hasil konversi waktu dalam satuan detik.
    """
    detik = menit * 60
    return detik
print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__)