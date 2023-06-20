# perbandingan nilai dengan metode prosedur
def perbandingan (na,nb):
    if (na > nb):
        print(na)
    elif (na == nb):
        print("Tidak ada")
    else:
        print(nb)
        
bil1 = int(input("Masukan bilangan 1: "))
bil2 = int(input("Masukan bilangan 2: "))
print("bilangan yang lebih besar adalah ")
perbandingan(bil1, bil2)