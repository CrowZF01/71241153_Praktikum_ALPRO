def perkalian(no1, no2):
    hasil = 0
    spasi = ""
    for i in range(no1):
        hasil = hasil + no2
        if i == 0:
            spasi = str(no2)
        else:
            spasi = spasi + " + " + str(no2)
    return f"{no1} x {no2} = {spasi} = {hasil}"

no1 = int(input("Masukkan angka : "))
no2 = int(input("Masukkan angka pengali : "))
