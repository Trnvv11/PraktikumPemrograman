# Function untuk mengecek bilangan ganjil atau genap
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        print("genap")
    else:
        print("ganjil")

bil = int (input("Masukan bilangan: "))
print(f"Bilangan {bil} adalah ")
cek_ganjil_genap(bil)
