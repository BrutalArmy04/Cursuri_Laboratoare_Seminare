a, b = input("a, b = ").split()
a, b = int(a), int(b)
f1, f2 = 0, 1
s = 0
while s<a:
    s = f1+f2
    f1 = f2
    f2 = s
if s>b:
    print('Nu exista')
else:
    print(f'Cel mai mic nr fibonacci din [{a}, {b}] este {s}')