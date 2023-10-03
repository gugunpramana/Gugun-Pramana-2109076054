def faktorial(n):

    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)
    
#contoh penggunaan
bilangan = 5
hasil_faktorial = faktorial(bilangan)
print("Faktorial dari : ",bilangan,"adalah",hasil_faktorial)
