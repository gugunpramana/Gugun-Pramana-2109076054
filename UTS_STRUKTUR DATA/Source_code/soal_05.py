from collections import deque

class AntrianBank:
    def __init__(self):
        self.antrian = deque()

    def masuk(self, pelanggan):
        # Menambahkan pelanggan ke dalam antrian
        self.antrian.append(pelanggan)

    def keluar(self):
        # Mengeluarkan pelanggan dari depan antrian (yang pertama masuk)
        if not self.is_empty():
            return self.antrian.popleft()
        else:
            raise IndexError("Antrian kosong. Tidak ada yang bisa dikeluarkan.")

    def is_empty(self):
        # Memeriksa apakah antrian kosong atau tidak
        return len(self.antrian) == 0

    def print_antrian(self):
        # Mencetak isi antrian dari depan ke belakang
        print("Isi Antrian Bank:")
        for pelanggan in self.antrian:
            print(pelanggan)
# Membuat objek antrian bank
antrian_bank = AntrianBank()

# Menambahkan beberapa pelanggan ke dalam antrian
antrian_bank.masuk("Pelanggan 1")
antrian_bank.masuk("Pelanggan 2")
antrian_bank.masuk("Pelanggan 3")
antrian_bank.keluar()
    
# Mencetak isi antrian
antrian_bank.print_antrian()
