def cek_huruf(huruf):
    huruf = huruf.lower()  # Mengubah huruf menjadi huruf kecil

    if huruf in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

# Input huruf
huruf_input = input("Masukkan sebuah huruf: ")

if len(huruf_input) == 1:
    if cek_huruf(huruf_input):
        print(huruf_input, "adalah huruf vokal.")
    else:
        print(huruf_input, "bukan huruf vokal.")
else:
    print("Masukkan hanya satu huruf.")
