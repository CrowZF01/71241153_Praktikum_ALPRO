kalimat = 'Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan'
kata = 'makan'

kata_kecil = kalimat.lower()
kata_full = kata_kecil.replace('.', '')

jumlah_kata = kata_full.count(kata)
print(f'{kata} ada {jumlah_kata} jumlahnya')
