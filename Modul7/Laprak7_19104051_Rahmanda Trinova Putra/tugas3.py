def insertionSortAscending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def insertionSortDescending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

total_buku = int(input("Masukkan total buku: "))
judul_buku = []

for i in range(total_buku):
    judul = input("Masukkan judul buku ke-{0}: ".format(i+1))
    judul_buku.append(judul)

print("\n<======== urutkan ========")
print("1. insertion ascending")
print("2. insertion descending")

pilih = int(input("Pilih: "))

if pilih == 1:
    insertionSortAscending(judul_buku)
    print("\nSorting buku secara ascending:")
elif pilih == 2:
    insertionSortDescending(judul_buku)
    print("\nSorting buku secara descending:")

for i, judul in enumerate(judul_buku, start=1):
    print("judul buku ke-{0} : {1}".format(i, judul))