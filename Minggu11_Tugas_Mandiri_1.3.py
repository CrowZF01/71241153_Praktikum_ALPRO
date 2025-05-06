kata_unik = ['halo', 'topi', '!', 'makan', 'piring']
kata_sama = []
with open ('kalimat.txt') as file:
    kalimat = file.read()
    kata = kalimat.split()
    for i in kata:
        if i in kata_unik:
            kata_sama.append(i)
print('Kata yang unik:', kata_sama)


#isi file kalimat.txt dibawah ini:
#halo semuanya nama saya tono dengan ! topi biasa
