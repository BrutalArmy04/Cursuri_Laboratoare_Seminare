n = int(input('Introduceti nr de studenti: '))
a, b = input('Primul interval:').split()
a, b = int(a), int(b)
for _ in range(n-1):
    a2, b2 = input('Alt interval= ').split()
    a2, b2 = int(a2), int(b2)
    a, b = max(a, a2), min(b, b2)
    if a >= b:
        print('Studentii nu sunt toti simultan prezenti')
        break
else:
    print(f'Studentii sunt toti simultan prezenti in intervalul [{a}, {b}]')
