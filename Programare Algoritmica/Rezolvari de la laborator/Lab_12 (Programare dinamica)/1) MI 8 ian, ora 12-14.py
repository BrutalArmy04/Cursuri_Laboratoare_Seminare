## Laborator 13, MI 8 ian, ora 12-14

# # Problema 1 model test
# f = open("pb1_matrice.in")
# matr = [[int(x) for x in linie.split()] for linie in f]
# f.close()
# print(*matr, sep="\n")
#
# for i in range(len(matr)):
#     max1 = max(matr[i])
#     matr[i].remove(max1)
#     max2 = max(matr[i])
#     matr[i].remove(max2)
# print(*matr, sep="\n")
#
# g=open("pb1_matrice.out" , "w")
# # g.writelines([" ".join([str(x) for x in linie]) + "\n"
# #          for linie in matr])
#
# g.write("\n".join([" ".join([str(x) for x in linie])
#          for linie in matr]))
# g.close()


# # # Problema 2 model test
## f = open("pb2_exemplu.txt")
# filename = input("name= ") # pb2_exemplu.txt
# f = open(filename, "r")

# d = {}  # cuvinte:frecvente
# for linie in f:
#     L_cuv = [cuv.lower() for cuv in linie.split()]
#     for cuvant in L_cuv:
#         d[cuvant] = d.get(cuvant, 0) + 1
# f.close()
# # print(d)
#
# d2 = {}  # frecventa:cuvinte
# for cuv, frecv in d.items():
#     # d2[frecv] = d2.get(frecv, []) + [cuv]
#
#     #var eficienta-cu if
#     if frecv not in d2:
#         d2[frecv]=[cuv]
#     else:
#         d2[frecv].append(cuv)
# # print(d2)
#
# rez=sorted(d2.items(), reverse=True)
# for frecv, L_cuv in rez:
#     print(f"Frecventa {frecv}: {', '.join(sorted(L_cuv))}")


## PROGRAMARE DINAMICA

# ## Problema 3
# f = open("pb3_matrice.in")
# m, n = [int(x) for x in f.readline().split()]
# matr = [[int(x) for x in linie.split()] for linie in f]
# f.close()
# print(*matr, sep="\n")
#
# s_max = [[0] * n for _ in range(m)]
# print(s_max)
#
# # s_max[i][j] = suma maxima a traseului care se termina pe
# # pozitia [i][j]
# for i in range(m):
#     for j in range(n):
#         if i == 0 and j == 0:
#             s_max[i][j] = matr[i][j]
#         elif i == 0:
#             s_max[i][j] = matr[i][j] + s_max[i][j - 1]
#         elif j == 0:
#             s_max[i][j] = matr[i][j] + s_max[i - 1][j]
#         else:
#             s_max[i][j] = matr[i][j] + max(s_max[i][j - 1], s_max[i - 1][j])
#
# print(*s_max, sep="\n")
#
# L_traseu = [(m - 1, n - 1)]
# i = m - 1
# j = n - 1
# while i != 0 or j != 0:
#
#     if i!=0 and (j==0 or s_max[i - 1][j] >= s_max[i][j - 1]):
#         i -= 1
#     else:
#         j -= 1
#     L_traseu.append((i, j))
# print(L_traseu)
#
# g=open("pb3_traseu.out",'w')
# g.write(str(s_max[-1][-1])+'\n')
# g.write("\n".join([f'{i+1} {j+1}' for i,j in L_traseu[::-1]]))
# g.close()


# ## Problema 4
# f = open("pb4_numere.in")
# L = [int(x) for x in f.read().split()]
# f.close()
# print(L)
#
# # s_max[i] = suma maxima care se termina pe pozitia i
# s_max = [0] * len(L)
# s_max[0] = L[0]
# for i in range(1, len(L)):
#     s_max[i] = max(L[i], L[i] + s_max[i - 1])
# print(s_max)
#
# sumaMax = max(s_max)
# pozUlt = s_max.index(sumaMax)
#
# copie_sumaMax = sumaMax
# pozInceput = pozUlt
# while copie_sumaMax > 0:
#     copie_sumaMax -= L[pozInceput]
#     pozInceput -= 1
#
# # print(pozInceput, pozUlt, sep=",")
#
# g = open("pb4_secventa.out", 'w')
# g.write(f"Suma este {sumaMax}\n")
# g.write(" ".join([str(x) for x in L[pozInceput + 1: pozUlt + 1]]))
# g.close()
