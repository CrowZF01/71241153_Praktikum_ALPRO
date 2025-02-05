import math

P = 200000000  
A = 400000000  
r = 0.10         
t = math.log(A / P) / math.log(1 + r)

print(f"waktu yang diperlukan untuk mencapai 400 juta = {t:.2f} tahun.")
