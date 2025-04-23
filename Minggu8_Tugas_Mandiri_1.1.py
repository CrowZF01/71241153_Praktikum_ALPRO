def anagram(kata_1,kata_2):
  kata_1 = kata_1.lower()
  kata_2 = kata_2.lower()

  if len(kata_1) != len(kata_2):
    return 'tidak sama jumlah hurufnya'
  
  for i in kata_1:
    if kata_1.count(i) != kata_2.count(i):
      return f'tidak sama hurufnya'
    else:
      return f'kata tersebut anagram'

print(anagram("atma", "tama"))
