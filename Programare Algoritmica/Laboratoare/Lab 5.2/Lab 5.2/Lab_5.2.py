
f = open("pb2_test.in", "r")
g = open("pb2_test.out", "w")
nota = 1
for linie in f:
    aux, rez = linie.split('=')
    x, y = aux.split('*')
    x, y, rez = int(x), int(y), int(rez)
    if x * y == rez:
         nota += 1
         g.write(f'{linie.strip()} Corect\n')
    else:
         g.write(f'{linie.strip()} Gresit {x*y}\n')
g.write(f'Nota {nota}')
