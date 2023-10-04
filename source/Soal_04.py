class Stack:
    def __init__(self):
        self.items = [] # syngtax yang dilengkapi

    def push(self, item):
        self.items.append(item) # syntax yang dilengkapi

    def pop(self):
        if not self.is_empty(): # syntax yang dilengkapi
            return self.items.pop()
        else:
            return "Tumpukan kosong"

    def is_empty(self):
        return len(self.items) == 0 # syntax yang dilengkapi

    # Sedikit Penambahan syntax dan uji coba syntax
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Tumpukan kosong"

    def size(self):
        return len(self.items)

# Inisialisasi stack sebagai rak buku
rack = Stack()

# Menambahkan beberapa buku ke rak satu per satu
rack.push("Buku A")
rack.push("Buku B")
rack.push("Buku C")

# Menampilkan isi rak buku sekaligus mengeluarkannya
print("Isi rak buku:")
while not rack.is_empty(): # satu persatu mengikuti prinssip LIFO
    print(rack.pop())

# Menampilkan ukuran akhir rak buku
print("Ukuran rak buku:", rack.size())
