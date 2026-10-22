def buat_biodata(nama, umur, jurusan):
    print("Nama    :", nama)
    print("Umur    :", umur)
    print("Jurusan :", jurusan)

print("--- Positional argument ---")
buat_biodata("Zian sisti agustin", 20, "Sistem Informasi")


print("--- Keyword argument ---")
buat_biodata(jurusan="Sistem Informasi", nama="Zian sisti agustin", umur=20)