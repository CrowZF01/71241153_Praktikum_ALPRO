import re
def kata_unik(nama_file):
    with open(nama_file, 'r') as file:
        isi = file.read().lower()
        kata_bersih = re.sub(r'[^a-zA-Z\s]', '', isi)
        kata = kata_bersih.split()
        kata.reverse()
        i = 0
        while i < len(kata):
            if kata.count(kata[i]) > 1:
                kata.remove(kata[i])
            else:
                i += 1
        kata.reverse()
        print('Kata unik:', ', '.join(kata))
kata_unik('kalimat.txt')
