from collections import deque

class AntrianBank:
    def __init__(self):
        self.antrian = deque()

    def masuk(self, pelanggan):
        self.antrian.append(pelanggan) # syntax yang dilengkapi
        print(f"Pelanggan {pelanggan} telah masuk ke dalam antrian bank.")

    def keluar(self):
        if self.antrian: # syntax yang dilengkapi
            pelanggan = self.antrian.popleft()
            print(f"Pelanggan {pelanggan} telah keluar dari antrian bank.")
        else:
            print("Tidak ada pelanggan dalam antrian bank.")

# Penambahan untuk melihat output-nya
# Membuat objek antrian bank
antrian_bank = AntrianBank()

# Pelanggan masuk ke dalam antrian bank
antrian_bank.masuk("Alice")
antrian_bank.masuk("Bob")
antrian_bank.masuk("Charlie")

# Menampilkan antrian saat ini
antrian_bank.keluar()
antrian_bank.keluar()

# Pelanggan masuk lagi ke dalam antrian bank
antrian_bank.masuk("David")

# Menampilkan antrian saat ini
antrian_bank.keluar()
antrian_bank.keluar()
antrian_bank.keluar()
