import re
from datetime import date
kalimat = " Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02). "
tanggal = re.findall(r'\d{4}-\d{2}-\d{2}', kalimat)

Tahun_sekarang = 2025
bulan_sekarang = 4
hari_sekarang = 22
tanggal_sekarang = date(Tahun_sekarang, bulan_sekarang, hari_sekarang)

for i in tanggal:
  pecahan_tanggal = i.split('-')
  tgl_tahun = int(pecahan_tanggal[0])
  tgl_bulan = int(pecahan_tanggal[1])
  tgl_hari = int(pecahan_tanggal[2])

  tanggal_dulu = date(tgl_tahun, tgl_bulan, tgl_hari)
  hasil_selisih = (tanggal_sekarang - tanggal_dulu).days
  print(f'{tgl_hari:02d}-{tgl_bulan:02d}-{tgl_tahun:02d} 00:00:00 selisih {hasil_selisih} hari')
