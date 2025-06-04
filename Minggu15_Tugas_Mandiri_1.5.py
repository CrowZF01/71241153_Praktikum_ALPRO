def kombinasi(a, b):
    if b == 0 or b == a:
        return 1
    return kombinasi(a - 1, b - 1) + kombinasi(a - 1, b)
print('Nilai A harus lebih besar dari B')
a = 4
b = 2
hasil_kombinasi = kombinasi(a, b)
print(kombinasi(a, b))
