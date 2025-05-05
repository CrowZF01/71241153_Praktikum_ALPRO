list_angka = [12, 32, 16, 92, 45, 78]
def tiga_bilangan(data):
    tertata = sorted(data)
    dibalik = list(reversed(tertata))
    print(f'3 bilangan terbesar = {dibalik[0]},{dibalik[1]},{dibalik[2]}')
tiga_bilangan(list_angka)
