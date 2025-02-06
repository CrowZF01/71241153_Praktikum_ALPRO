
p = 200
a = 400 
r = 0.1 
t = 0  

while p < a:
    p = p + (r * p)
    t += 1

print(t)
