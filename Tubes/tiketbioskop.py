def pesan_tiket_bioskop():
    daftar_film = {
        "A001": {
            "judul": "Avengers: Endgame",
            "jam_tayang": ["10:00", "13:00", "16:00"]
        },
        "S001": {
            "judul": "Spider-Man: Far From Home",
            "jam_tayang": ["11:00", "14:00", "17:00"]
        },
        "B001": {
            "judul": "Black Panther",
            "jam_tayang": ["12:00", "15:00", "18:00"]
        }
    }

    while True:
        print("Daftar Film:")
        for kode_film, info_film in daftar_film.items():
            print("-", kode_film, "-", info_film["judul"])

        kode_film_pilihan = input("Pilih kode film ('x' untuk kembali): ")
        if kode_film_pilihan == 'x':
            return

        if kode_film_pilihan not in daftar_film:
            print("Kode film tidak tersedia.")
            continue

        film_pilihan = daftar_film[kode_film_pilihan]["judul"]
        print("Film yang dipilih:", film_pilihan)

        while True:
            print("Jam Tayang:")
            for jam in daftar_film[kode_film_pilihan]["jam_tayang"]:
                print("-", jam)

            jam_pilihan = input("Pilih jam tayang ('x' untuk kembali): ")
            if jam_pilihan == 'x':
                break

            if jam_pilihan not in daftar_film[kode_film_pilihan]["jam_tayang"]:
                print("Jam tayang tidak tersedia.")
                continue

            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
            harga_tiket = 10  # Harga tiket bioskop per tiket

            print("\nKetersediaan Kursi:")
            kursi = [[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15]]

            for row in kursi:
                for seat in row:
                    print(seat, end=" ")
                print()

            pesanan_kursi = []
            for _ in range(jumlah_tiket):
                while True:
                    kursi_pilihan = int(input("Pilih kursi (masukkan nomor kursi) ('x' untuk kembali): "))
                    if kursi_pilihan == 'x':
                        break
                    if kursi_pilihan in pesanan_kursi:
                        print("Kursi sudah dipesan.")
                    else:
                        pesanan_kursi.append(kursi_pilihan)
                        break

            if kursi_pilihan == 'x':
                continue

            total_harga = jumlah_tiket * harga_tiket
            if jumlah_tiket > 5:
                diskon = 0.05  # 5% diskon
                potongan_harga = total_harga * diskon
                total_harga -= potongan_harga

            print("\nDetail Pesanan:")
            print("Film: ", film_pilihan)
            print("Jam Tayang: ", jam_pilihan)
            print("Kursi: ", pesanan_kursi)
            print("Jumlah Tiket: ", jumlah_tiket)
            print("Total Harga: $", total_harga)
            return

pesan_tiket_bioskop()
