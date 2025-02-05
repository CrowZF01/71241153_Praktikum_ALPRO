emas_awal = 25
emas_ditambah = 15

harga_emas_awal = 650000
harga_emas_sekarang = 685000
harga_emas_ditambah = 715000

total_harga_emas_awal = emas_awal * harga_emas_awal
total_harga_emas_sekarang = emas_awal * harga_emas_sekarang
total_harga_emas_ditambah = emas_ditambah * harga_emas_sekarang
total_harga_semua_emas = total_harga_emas_awal + total_harga_emas_ditambah

total_emas = emas_awal + emas_ditambah
total_harga_emas3 = total_emas * harga_emas_ditambah

Keuntungan = total_harga_emas_sekarang - total_harga_emas_awal
Keuntungan_persen = (Keuntungan / total_harga_emas_awal) * 100


Keuntungan_ditambah = total_harga_emas3 - total_harga_semua_emas
keuntungan_total_semua = total_harga_emas3 - total_harga_semua_emas
Keuntungan_persen_ditambah = (keuntungan_total_semua / total_harga_semua_emas) * 100


print('ini adalah keuntungan : ',Keuntungan)
print('ini adalah keuntungan persen : ',Keuntungan_persen,'%')
print('ini adalah keuntungan setelah ditambah : ',keuntungan_total_semua)
print('ini adalah keuntungan persen setelah ditambah : ',Keuntungan_persen_ditambah,'%')