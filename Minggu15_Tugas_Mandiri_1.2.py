def palindrom(n):
    if len(n) <= 1:
        return "Palindrom"
    if n[0] != n[-1]:
        return "Bukan Palindrom"
    return palindrom(n[1:-1])
input_user = input("Masukkan kata: ")
print(palindrom(input_user))
