# input n kategori
n = int(input('Masukkan jumlah kategori: '))

# siapkan dictionary kosong
data_aplikasi = {}

# input nama kategori dan aplikasi di dalamnya
for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)

    # siapkan list kosong untuk nama-nama aplikasi
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)

    # masukkan dalam dictionary
    data_aplikasi[nama_kategori] = aplikasi

# tampilkan dictionary data_aplikasi
print()
print(data_aplikasi)

daftar_aplikasi_list = []
# ambil semua daftar aplikasi dari setiap kategori
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

print()
print(daftar_aplikasi_list)

# lakukan intersection ke semua set yang ada
hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

print()
print(hasil)

union_all = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    union_all = union_all | daftar_aplikasi_list[i]

multi_kategori = set()
for i in range(n):
    for j in range(i + 1, n):
        irisan = daftar_aplikasi_list[i] & daftar_aplikasi_list[j]
        multi_kategori = multi_kategori | irisan
satu_kategori = union_all - multi_kategori

print()
print("Aplikasi di satu kategori:")
print(satu_kategori)
print()

if n >= 2:
    jumlah_kemunculan = {}
    
    for app_set in daftar_aplikasi_list:
        for app in app_set:
            if app in jumlah_kemunculan:
                jumlah_kemunculan[app] += 1
            else:
                jumlah_kemunculan[app] = 1
    
    dua_kategori_apps = set()
    for app, jumlah in jumlah_kemunculan.items():
        if jumlah == 2:
            dua_kategori_apps.add(app)

    print("Aplikasi di dua kategori:")
    print(dua_kategori_apps)
