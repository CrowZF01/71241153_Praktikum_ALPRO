import re
nama_file= input('Ketik nama file: ')
with open(nama_file) as file:
    tempat = {}
    for line in file:
        jam_list = re.findall(r'\b(\d{2}):\d{2}:\d{2}\b', line)
        for i in jam_list:
            if i in tempat:
                tempat[i] += 1
            else:
                tempat[i] = 1
    sorted_jam = sorted(tempat.keys(), key=int)
    for i in sorted_jam:
        print(i, tempat[i])
