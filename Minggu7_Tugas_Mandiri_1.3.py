tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

for i in range(1, tinggi+1):
    for j in range(1, lebar+1):
        print((i-1)*lebar + j, end=" ")
    print()
