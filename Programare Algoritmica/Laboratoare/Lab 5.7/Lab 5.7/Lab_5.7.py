f = open("pb_7.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
f.close()

nr_linii = len(matr)
nr_coloane = len(matr[0])
matr2 = [[matr[i][j] for i in range(nr_linii)]for j in range(nr_coloane)]

print(*matr2, sep='\n')
