def genap_ganjil(n):
    if n == 0:
        return "Genap"
    elif n == 1:
        return "Ganjil"
    else:
        return genap_ganjil(n - 2)
angka = int(input("Masukkan bilangan bulat: "))
print(genap_ganjil(angka))
