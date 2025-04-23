import re, random

kalimat ='Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari'
pola = re.findall(r"\S+@\S+",kalimat)

for i in pola:
    nama = i.split("@")[0]
    pilihan_password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''.join(random.choices(pilihan_password, k=8))
    print(f'{i} username: {nama}, password: {password}')
