def ganjil():
    bawah = int(input("Masukkan batas bawah: "))
    atas = int(input("Masukkan batas atas: "))
    if bawah < atas:
        step = 1
    else:
        step = -1

    for i in range(bawah,atas,step):
        if i % 2 != 0:
            print(i, end=" ")
    print()
ganjil()
