def hitung_nilai(nilai):
    total = sum(nilai)
    rata = total / len(nilai)
    return rata

def tentukan_predikat(nilai):
    if 100 > nilai >= 90:
        return "A"
    elif 90 > nilai >= 70:
        return "B"
    elif 70 > nilai >= 50:
        return "C"
    elif 50 > nilai >= 30:
        return "D"
    elif 30 > nilai >= 0:
        return "E"
    else:
        return "Tidak valid"

# Menginputkan nilai-nilai
jumlah_nilai = int(input("Masukkan jumlah nilai: "))
nilai_list = []
for i in range(jumlah_nilai):
    nilai = float(input("Masukkan nilai ke-{}: ".format(i+1)))
    nilai_list.append(nilai)

# Menghitung rata-rata nilai
rata_nilai = hitung_nilai(nilai_list)

# Menentukan predikat
predikat = tentukan_predikat(rata_nilai)

# Menampilkan output
for i, nilai in enumerate(nilai_list):
    print("Nilai ke-{}: {:.2f}".format(i+1, nilai))
print("Rata-rata nilai: {:.2f}".format(rata_nilai))
print("Predikat: {}".format(predikat))

