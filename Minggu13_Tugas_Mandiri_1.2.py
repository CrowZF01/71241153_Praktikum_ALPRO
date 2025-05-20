Data = ('Felix Benedictus Setiawan', '71241153', 'Godean, DI Yogyakararta')
print("NIM : ", Data[1])
print("NAMA: ", Data[0])
print("ALAMAT: ", Data[2])
print()

print("NIM: ", tuple(Data[1]))
print()

nama_awal = Data[0].split()
kata_awal = tuple(nama_awal[0])
print('NAMA DEPAN:',kata_awal[1:])
print()

nama = tuple(Data[0].split())
terbalik = nama[::-1]
print("NAMA TERBALIK: ", terbalik)
