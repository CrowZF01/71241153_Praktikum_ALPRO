pembelian = input("Masukkan pembelian: ")
try:
    pembelian = int(pembelian)
    print(pembelian >= 100000)
except:
    print("Pembelian harus berupa angka")

    