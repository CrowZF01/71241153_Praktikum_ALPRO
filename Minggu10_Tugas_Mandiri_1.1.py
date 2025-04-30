nama = 'Tugasmandiri_1.txt'
print(f'Nama file 1: {nama}')

with open(nama) as file:
    for line in file:
        bagian = line.strip().split('||')
        pertanyaan = bagian[0].strip()
        jawaban = bagian[1].strip()
        print(pertanyaan)
        inputan = input('Jawab: ').strip()

        if inputan.lower() == jawaban.lower():
            print('Jawaban Benar!')
        else:
            print('Jawaban Salah!')


