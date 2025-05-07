def kata_unik(nama_file):
    with open(nama_file) as file:
        isi = file.read().lower()
        data = isi.split()
        hasil = []
        for i in range(len(data)):
            duplikat = False
            for j in range(len(data)):
                if i != j and data[i] == data[j]:
                    duplikat = True
                    break
            if not duplikat and data[i] not in hasil:
                hasil.append(data[i])
        print('Kata unik:', ', '.join(hasil))
kata_unik('kalimat.txt')


