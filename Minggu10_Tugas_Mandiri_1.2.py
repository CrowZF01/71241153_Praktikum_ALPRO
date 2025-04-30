text_1 = 'perbandingan_1.txt'
text_2 = 'perbandingan_2.txt'
nomer = 1
with open(text_1) as file_1, open(text_2) as file_2:
    for baris1, baris2 in zip(file_1, file_2):
        if baris1.strip() != baris2.strip():
            bagian1 = baris1.strip().lower().split()
            bagian2 = baris2.strip().lower().split()
            hasil1 = ""
            hasil2 = ""
            for kata in bagian1:
                if kata not in bagian2:
                    hasil1 += kata + " "

            for kata in bagian2:
                if kata not in bagian1:
                    hasil2 += kata + " "
            if hasil1 or hasil2:
                print(f"Baris {nomer} ada perbedaan")
                print(f"File1 = {baris1.strip()}")
                print(f"File2 = {baris2.strip()}")
                print(f'File1 ada kata "{hasil1.strip()}" sedangkan di File2 ada kata "{hasil2.strip()}"')
        nomer += 1
