def cek_angka():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = int(input("Masukkan angka ketiga: "))
    if a != b and a != c and b != c:
        if a + b == c or b + c == a or a + c == b:
            return True
        else:
            return False
    else:
        return False
    
print(cek_angka())

