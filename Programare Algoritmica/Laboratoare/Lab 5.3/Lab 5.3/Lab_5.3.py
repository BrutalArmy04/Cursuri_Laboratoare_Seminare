m, n = [int(x) for x in input('m, n= ').split()]
matr = [[int(x) for x  in input(f'Linia {i}: ').split()] for i in range(m)]
#for linie in matr:
#    for x in linie:
#        print(x, end=' ')
#    print()
for linie in matr:
    print(*linie)
L_maxime=[max(linie) for linie in matr]
print(L_maxime)