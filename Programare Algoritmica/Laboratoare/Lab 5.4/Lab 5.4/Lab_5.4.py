f = open('pb4.in', 'r')
m, n = [int(x) for x in f.readline().split()]
matr = [[int(x) for x in linie.split()] for linie in f]
#print(*matr, sep = '\n')
k = int(input('k= '))
#matr.insert(k+1, [0 for _ in range(n)])
#matr.insert(k+1, [0]*n)
matr[k+1:k+1] = [[0]*n]
g = open('pb4.out', 'w')
g.writelines([' '.join([str(x) for x in linie]) +'\n' for linie in matr])
g.close()