def deret_ganjil(n):
    if n == 1:
        return 1
    return (2 * n - 1) + deret_ganjil(n - 1)
n = int(input("Masukkan jumlah deret: "))
hasil_deret = deret_ganjil(n)
print(f"Jumlah = {hasil_deret}")
