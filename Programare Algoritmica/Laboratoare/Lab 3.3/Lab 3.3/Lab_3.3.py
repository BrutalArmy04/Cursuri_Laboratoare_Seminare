s = input('sir = ')
t = input('subsir = ')
#poz = s.find(t)
#if poz == -1:
#    print(f'Subsirul {t} nu a fost gasit in sirul {s}')
#else:
#    while poz!=-1:
#        print(poz, end=', ')
#        poz = s.find(t, poz + len(t))
poz = -len(t)
gasit = False
while True:
    try:
        poz = s.index(t, poz + len(t))
        print(poz, end=', ')
        gasit = True
    except ValueError:
        print('Gata cautarea')
        break
if not gasit:
    print(f'Subsirul {t} nu a fost gasit in sirul {s}')