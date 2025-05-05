def rata_rata():
    angka = []
    jumlah = input('Masukkan jumlah angka yang ingin dihitung rata-ratanya: ')
    for i in range(int(jumlah)):
        num = input(f'masukkan angka:')
        angka.append(float(num))
    rata = sum(angka) / len(angka)
    print(f'Rata-rata = {rata:.2f}')
rata_rata()
