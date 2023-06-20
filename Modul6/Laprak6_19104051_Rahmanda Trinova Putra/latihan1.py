# Metode function
def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi(sisi):
    return sisi * sisi

panjang = int(input("Masukan panjang sisi : "))
print("Keliling persegi :",keliling_persegi(panjang))
print("Luas persegi :",luas_persegi(panjang))

# Metode Prosedur
def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print("Keliling persegi: %d" %keliling)
    print("Luas persegi: %d" %luas)
    
panjang = int(input("Masukan panjang sisi: "))
keliling_luas_persegi(panjang)