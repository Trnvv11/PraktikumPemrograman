import math

def hitung_volume_persegi(sisi):
    volume = sisi ** 3
    return volume

def hitung_volume_lingkaran(jari_jari):
    volume = (4/3) * math.pi * (jari_jari ** 3)
    return volume

# menghitung volume persegi
sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
volume_persegi = hitung_volume_persegi(sisi_persegi)
print("Volume persegi dengan sisi", sisi_persegi, "adalah", volume_persegi)

# menghitung volume lingkaran
jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))
volume_lingkaran = hitung_volume_lingkaran(jari_jari_lingkaran)
print("Volume lingkaran dengan jari-jari", jari_jari_lingkaran, "adalah", volume_lingkaran)
