def binary_search(nim_list, target):
    left = 0
    right = len(nim_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if nim_list[mid] == target:
            return True
        elif nim_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Daftar NIM mahasiswa
nim_list = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005,
            20103011, 20103003, 20103009, 20103021, 20103006, 20103015,
            20103013, 20103007]

# Meminta input dari pengguna
target_nim = int(input("Masukkan NIM yang ingin Anda cari: "))

# Melakukan pencarian
result = binary_search(nim_list, target_nim)

# Menampilkan hasil
if result:
    print("NIM", target_nim, "ditemukan di kelas.")
else:
    print("NIM", target_nim, "tidak ditemukan di kelas.")
