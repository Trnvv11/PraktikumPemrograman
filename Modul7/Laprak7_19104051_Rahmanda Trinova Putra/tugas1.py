def bubble_sort(ips):
    n = len(ips)
    for i in range(n):
        for j in range(n - i - 1):
            if ips[j] > ips[j + 1]:
                ips[j], ips[j + 1] = ips[j + 1], ips[j]
    return ips            
ips_mahasiswa = [3.8, 2.9, 3.3, 4.0, 2.7]
print("List sebelum diurutkan:", ips_mahasiswa)

bubble_sort(ips_mahasiswa)

ips_mahasiswa = bubble_sort(ips_mahasiswa)

print("List setelah diurutkan:",ips_mahasiswa)
