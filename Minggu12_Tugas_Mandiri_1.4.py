import re
fname = input('Masukkan nama file: ')
with open(fname, 'r') as file:
    membaca = file.read()
    alamat_email = re.findall(r'@([A-Za-z0-9.-]+)', membaca)
    tempat = {}
    for email in alamat_email:
        if email in tempat:
            tempat[email] += 1
        else:
            tempat[email] = 1
print(tempat) 
