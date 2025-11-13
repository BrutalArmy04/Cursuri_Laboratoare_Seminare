f = open("pb_6.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
print()
f.close()
k = int(input('k= '))

#matr2 = [linie[-k:] + linie[:-k+1] for linie in matr]
#lista_par = [x for linie in matr for x in linie if not x%2]
l_sume = [sum(linie)-max(linie) for linie in matr]
matr2 = [matr[i] if not i%2 else matr[i].reverse()) for i in range(len(matr))]