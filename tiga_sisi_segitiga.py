bilangan1 = input("Masukkan sisi 1: ")
bilangan2 = input("Masukkan sisi 2: ")
bilangan3 = input("Masukkan sisi 3: ")
try:
    bilangan1 = int(bilangan1)
    bilangan2 = int(bilangan2)
    bilangan3 = int(bilangan3)
    if bilangan1 == bilangan2 and bilangan1 == bilangan3:
        print("3 sisi sama")
    elif bilangan1 == bilangan2 or bilangan1 == bilangan3 or bilangan2 == bilangan3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except:
    print("Sisi harus berupa angka")