lista = ['red', 'green', 'blue']
listb = ['008000', '0000FF', 'FF0000']
tempat = []
for i in range(len(lista)):
    tempat.append((lista[i], f'#{listb[i]}'))
kamus = dict(tempat)
print(kamus)
