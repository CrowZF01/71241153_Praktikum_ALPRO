n = int(input("Masukkan angka: "))
n_asli = n
count = 1
while count < 2:
    n = n - 1
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print (f"Bilangan prima terdekat < {n_asli} adalah {n}")
        count += 1
