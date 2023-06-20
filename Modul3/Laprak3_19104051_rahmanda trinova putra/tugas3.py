def hitung_biaya_operasi_mata(penyakit):
    biaya = {
        '1': {'jenis': 'Katarak', 'biaya': 7500000},
        '2': {'jenis': 'Plus/Minus', 'biaya': 5000000},
        '3': {'jenis': 'Silinder', 'biaya': 4000000}
    }

    if penyakit in biaya:
        return f"Biaya operasi mata {biaya[penyakit]['jenis']} = Rp.{biaya[penyakit]['biaya']:,}"
    else:
        return "Jenis penyakit mata tidak valid."

def hitung_biaya_operasi_jantung(penyakit):
    biaya = {
        '1': {'jenis': 'Jantung Koroner', 'biaya': 500000000},
        '2': {'jenis': 'Otot Jantung', 'biaya': 350000000},
        '3': {'jenis': 'Katup Jantung', 'biaya': 450000000}
    }

    if penyakit in biaya:
        return f"Biaya operasi jantung {biaya[penyakit]['jenis']} = Rp.{biaya[penyakit]['biaya']:,}"
    else:
        return "Jenis penyakit jantung tidak valid."

print("<----Menu---->")
print("1. Hitung biaya operasi Mata")
print("2. Hitung biaya operasi Jantung")

pilih = input("Pilih: ")

if pilih == '1':
    print("1. Katarak")
    print("2. Plus/Minus")
    print("3. Silinder")

    jenis_penyakit = input("Masukkan jenis penyakit: ")
    biaya_mata = hitung_biaya_operasi_mata(jenis_penyakit)
    print(biaya_mata)

elif pilih == '2':
    print("1. Jantung Koroner")
    print("2. Otot Jantung")
    print("3. Katup Jantung")

    jenis_penyakit = input("Masukkan jenis penyakit: ")
    biaya_jantung = hitung_biaya_operasi_jantung(jenis_penyakit)
    print(biaya_jantung)

else:
    print("Pilihan tidak valid.")
