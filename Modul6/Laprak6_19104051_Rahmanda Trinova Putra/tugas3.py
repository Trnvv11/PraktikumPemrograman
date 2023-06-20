# Function untuk penjumlahan
def tambah(a, b):
    return a + b

# Function untuk pengurangan
def kurang(a, b):
    return a - b

# Function untuk perkalian
def kali(a, b):
    return a * b

# Function untuk pembagian
def bagi(a, b):
    return a / b

# Procedure untuk menerima input dan menampilkan
def kalkulator():
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))

    print("Menu")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    choice = int(input("Masukkan pilihan (1/2/3/4): "))

    if choice == 1:
        hasil = tambah(a, b)
        operator = "+"
    elif choice == 2:
        hasil = kurang(a, b)
        operator = "-"
    elif choice == 3:
        hasil = kali(a, b)
        operator = "*"
    elif choice == 4:
        hasil = bagi(a, b)
        operator = "/"
    else:
        print("Pilihan tidak valid.")
        return

    print(f"Hasil: {a} {operator} {b} = {hasil}")

# Memanggil procedure kalkulator untuk menjalankan program
kalkulator()
