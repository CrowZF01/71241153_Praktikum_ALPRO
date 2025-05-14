angka = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print('key\tvalue\titem')
temp = []
for key, value in angka.items():
    temp.append((key, value))
    print(f'{key}\t{value}\t{key}')
angka = dict(temp)
print(angka)
