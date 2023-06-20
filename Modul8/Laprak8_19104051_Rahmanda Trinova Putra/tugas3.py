def bubble_sort(bilangan, data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
    return binary_search(bilangan, data)

def binary_search(bilangan, data):
    left = 0
    right = len(data) - 1
    
    while left <= right :
        mid = (left+right)//2
        if str(data[mid]).lower() > bilangan.lower() :
            right = mid - 1
        elif str(data[mid]).lower() < bilangan.lower() :
            left = mid + 1
        else :
            print(data)
            print(f"Bilangan {bilangan} terdapat pada index {mid}")
            return mid
    
    print(f"bilangan {bilangan} tidak ditemukan")
    return - 1

data = [ 17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]
bilangan = input("input bilangan: ")
bubble_sort(bilangan, data)