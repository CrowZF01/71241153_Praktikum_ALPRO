nomor_bulan = input("Masukkan nomor bulan 1-12: ")
try:
    nomor_bulan = int(nomor_bulan)
    if nomor_bulan == 2:
       print("Jumlah hari : 29 hari")
    elif nomor_bulan == 4 or nomor_bulan == 6 or nomor_bulan == 9 or nomor_bulan == 11:
       print("Jumlah hari : 30 hari")
    elif nomor_bulan == 1 or nomor_bulan == 3 or nomor_bulan == 5 or nomor_bulan == 7 or nomor_bulan == 8 or nomor_bulan == 10 or nomor_bulan == 12:
        print("Jumlah hari : 31 hari")
except:
    print("Nomor bulan harus berupa angka")
  


