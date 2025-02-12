gaji_per_jam = float(input("Gaji setiap jam: "))
jam_kerja = int(input("Jumlah jam kerja dalam satu minggu: "))

total_jam_kerja = jam_kerja * 5
pendapatan_sebelum_pajak = gaji_per_jam * total_jam_kerja
pajak = pendapatan_sebelum_pajak * 0.14
pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak

pengeluaran_baju_aksesoris = pendapatan_setelah_pajak * 0.10
pengeluaran_alat_tulis = pendapatan_setelah_pajak * 0.01
sisa_uang = pendapatan_setelah_pajak - pengeluaran_baju_aksesoris - pengeluaran_alat_tulis

uang_sedekah = sisa_uang * 0.25
uang_anakyatim = uang_sedekah * 0.30
uang_kaumdhuafa = uang_sedekah * 0.70

print("Pendapatan Budi Sebelum Pajak: Rp ", pendapatan_sebelum_pajak)
print("Pendapatan Budi Setelah Pajak: Rp ", pendapatan_setelah_pajak)
print("Pengeluaran Baju dan Aksesoris Budi: Rp ", pengeluaran_baju_aksesoris)
print("Pengeluaran Alat Tulis Budi: Rp ", pengeluaran_alat_tulis)
print("Uang Budi sedekahkan: Rp ", uang_sedekah)
print("Uang yang diterima kaum dhuafa: Rp ", uang_kaumdhuafa)
print("Uang yang diterima anak yatim: Rp ", uang_anakyatim)




