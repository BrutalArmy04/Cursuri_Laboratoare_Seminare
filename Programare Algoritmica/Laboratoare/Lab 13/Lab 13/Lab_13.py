# Prob 1 model examen


# with open("matrice.in.txt", 'r') as f:
#     M = [[int(x) for x in linie.split()] for linie in f]
# for linie in M:
#     print(*linie)

# for i in range(len(M)):

#     M[i].remove(max(M[i]))
#     M[i].remove(max(M[i]))
# for linie in M:
#     print(*linie)
# with open("pb1_matrice.out", 'w') as g:
#     #g.write([" ".join([str(x) for x in linie]) for linie in M])
#     g.writelines([" ".join([str(x) for x in linie]) + "\n" for linie in M])

#Prob 2

# with open ('input.txt', 'r') as f:
#     d={} #cuvant : frecventa
#     for linie in f:
#         for cuv in linie.lower().split():
#             #if cuv not in d:
#             #   d[cuv = 1
#             #else:
#             #   d[cuv]+=1


#             d[cuv] = d.get(cuv, 0) + 1

# print(d)


# d2 = {} # frecventa : lista de cuvinte

# for cuv, frecv in d.items():
#     if frecv not in d2:
#         d2[frecv] = [cuv]
#     else:
#         d2[frecv].append(cuv)
#     # sau (ineficient (+ pe liste))
#     #d2[frecv] = d2.get(frecv, []) + [cuv]

# print(d2)

# rez = sorted(d2.keys(), reverse = True) # lista de frecvente descrescatoare

# # for frecv in rez:
# #     print(f'Frecventa {frecv}: {", ".join(sorted(d2[frecv]))}')


# # Prob 3

# with open('input.txt', 'r') as f:
#     m, n = [int(x) for x in f.readline().split()]
#     M = [[int(x) for x in linie.split()] for linie in f]

# #Smax[i][j] = suma maxima a traseului care se termina pe pozitia (i,j)

# Smax = [[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if i == 0 and j == 0:
#             Smax[i][j] = M[i][j]
#         elif i == 0:
#             Smax[i][j] = Smax[i][j - 1] + M[i][j]
#         elif j == 0:
#             Smax[i][j] = Smax[i - 1][j] + M[i][j]
#         else:
#             Smax[i][j] = max(Smax[i][j - 1], Smax[i - 1][j]) + M[i][j]


# L_traseu = [(m - 1, n - 1)]
# i = m - 1
# j = n - 1
# while i > 0 or j > 0:
#     if i > 0 and ( j == 0 or Smax[i - 1][j] >= Smax[i][j - 1]):
#         i -= 1
#     else:
#         j-=1
#     L_traseu.append((i, j))

# print(L_traseu)

# with open('traseu.out', 'w') as g:
#     g.write(f'Suma este {Smax[-1][-1]}.\n')
#     g.writelines([f'{i+1} {j+1}\n' for i, j in L_traseu[::-1]])

#Prob 4

with open ('input.txt', 'r') as f:
    L = [int(x) for x in f.readline().split()]
print(L)

Smax = [0 for x in range(len(L))]
Smax[0] = L[0]
for i in range(1, len(L)):
    Smax[i] = max(L[i], Smax[i-1]+L[i])

suma_max = max(Smax)
poz_ultimul = Smax.index(suma_max)
poz_primul = poz_ultimul
while L[poz_primul] != Smax[poz_primul]:
    poz_primul-=1
print(poz_primul, poz_ultimul)

with open ('traseu.out', 'w') as g:
    g.write(f'Suma este {suma_max}\n')
    g.write(" ".join([str(x) for x in L[poz_primul:poz_ultimul+1]]))
