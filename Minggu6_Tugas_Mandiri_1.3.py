jumlah_mk = int(input("Jumlah Matakuliah: "))
def hitung_nilai():
    bobot_nilai = 0
    
    for i in range(1, jumlah_mk + 1):
        nilai = input(f"Nilai MK {i} (A/B/C/D): ").upper()
        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1 
        bobot_nilai = bobot_nilai + bobot
    ips = bobot_nilai / jumlah_mk
    print(f"Nilai IPS anda semester ini {ips:.2f}")

hitung_nilai()
