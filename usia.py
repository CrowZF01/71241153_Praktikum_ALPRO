usia = input("Masukkan usia anda: ")

try:
    usia = int(usia)
    if usia <= 5:
        print("Balita")
    elif usia >= 6 and usia <= 11:
        print("Kanak-kanak")
    elif usia >= 12 and usia <= 25:
        print("Remaja")
    elif usia >= 26 and usia <= 45:
        print("Dewasa")
    elif usia >45:
        print("Lansia")
except:
    print("Usia harus berupa angka")