text_1 = 'perbandingan_1.txt'
text_2 = 'perbandingan_2.txt'
nomer = 1
with open(text_1) as file_1, open(text_2) as file_2:
    for baris1, baris2 in zip(file_1, file_2):
        if baris1.strip() != baris2.strip():
            kata1 = baris1.strip().lower().split()
            kata2 = baris2.strip().lower().split()
            pembanding1 = ""
            pembanding2 = ""
            state = False

            for kata in kata1:
                if kata not in kata2:
                    pembanding1 += kata + " "
                    state = True

            for kata in kata2:
                if kata not in kata1:
                    pembanding2 += kata + " "
                    state = True

            if state:
                print(f"Baris {nomer} ada perbedaan")
                print(f"File1 = {baris1.strip()}")
                print(f"File2 = {baris2.strip()}")
                print(f'File1 ada kata "{pembanding1.strip()}" sedangkan di File2 ada kata "{pembanding2.strip()}"')
        nomer += 1
