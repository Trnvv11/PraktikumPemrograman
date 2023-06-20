import math

# Metode function 
def keliling_lingkaran(jari):
    return 2 * math.pi * jari

def luas_lingkaran(jari):
    return math.pi * jari **2

panjang = int(input("Masukan jari-jari : "))
print("Keliling Lingkaran :",keliling_lingkaran(panjang))
print("Luas Lingkaran :",luas_lingkaran(panjang))

# Metode Prosedur
def keliling_luas_lingkaran(jari):
    keliling = round (2 * math.pi *jari, 1)
    luas = round (math.pi * jari **2, 1)
    print("Keliling persegi: %d" %keliling)
    print("Luas persegi: %d" %luas)
    
panjang = int(input("Masukan panjang sisi: "))
keliling_luas_lingkaran(panjang)