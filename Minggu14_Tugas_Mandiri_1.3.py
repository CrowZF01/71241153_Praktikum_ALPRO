file_1 = input('Masukkan nama file satu: ')
file_2 = input('Masukkan nama file dua: ')
try:
    with open(file_1) as file1:
        file1_kata = file1.read().lower().split()
    with open(file_2) as file2:
        file2_kata = file2.read().lower().split()
except:
    print(f"File tidak ditemukan")

kata_1 = set(file1_kata)
kata_2 = set(file2_kata)
gabungan_kata = kata_1.intersection(kata_2)

if len(gabungan_kata) > 0:
    for i in gabungan_kata:
        print(f'Kata "{i}" ada di kedua file')
else:
    print('Tidak ada kata yang sama di kedua file')
