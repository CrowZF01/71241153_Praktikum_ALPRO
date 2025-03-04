def cek_digit_belakang():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = int(input("Masukkan angka ketiga: "))
    if a % 10 == b % 10:
        return True
    elif a % 10 == c % 10:
        return True
    elif b % 10 == c % 10:
        return True
    else:
        return False

print(cek_digit_belakang())