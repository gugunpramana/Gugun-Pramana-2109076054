def hitung_jumlah_list(my__list):
    total = 0
    for element in my__list:
        total += element
    return total


#contoh penggunaan
list_angka = [1,2,3,4,5,]
jumlah = hitung_jumlah_list(list_angka)
print("jumlah semua elemen dalam list : ",jumlah)
