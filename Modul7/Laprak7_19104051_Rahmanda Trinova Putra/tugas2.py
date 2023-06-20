def selectionSort(nama):
    n = len(nama)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if nama[j] < nama[min_idx]:
                min_idx = j
        nama[i], nama[min_idx] = nama[min_idx], nama[i]

nama_anggota = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]

print("Nama anggota sebelum diurutkan:", nama_anggota)

selectionSort(nama_anggota)

print("\nNama anggota setelah diurutkan:", nama_anggota)
