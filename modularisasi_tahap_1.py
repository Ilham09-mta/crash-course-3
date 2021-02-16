"""
Program Menghitung Luas Segitiga
Luas_Segitiga = alas * tinggi / 2
"""
print('\nMenghitung Luas Segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung Luas Segitiga 2 Dengan Copy Paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nmembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 2)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(100, 2)}')





