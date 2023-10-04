def faktorial(n):
    if n == 0:
        return 1 # kode yang dilengkapi
    else:
        return n * faktorial(n - 1) # kode yang dilengkapi

# Menghitung faktorial dari 5
bilangan = 5
hasil_faktorial = faktorial(bilangan)
print("Faktorial dari", bilangan, "adalah", hasil_faktorial)