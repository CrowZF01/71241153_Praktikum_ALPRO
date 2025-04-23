kalimat = 'red snakes and and black frog in the pool'
kata = kalimat.split()

pendek = kata[0]
panjang = kata[0]

for i in kata:
  if len(i) < len(pendek):
    pendek = i
  elif len(i) > len(panjang):
    panjang = i

print("paling pendek:",pendek)
print("paling panjang:", panjang)
