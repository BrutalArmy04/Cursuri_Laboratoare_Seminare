## Laborator 13, JO 9 ian, ora 12-14

# ## Problema 1 model test
#
# f=open("pb1_matrice.in", 'r')
# matr=[[int(x) for x in line.split()] for line in f]
# f.close()
# for line in matr:
#     print(*line)
#
# for i in range(len(matr)):
#     matr[i].remove(max(matr[i]))
#     matr[i].remove(max(matr[i]))
#
# print('\n')
# for line in matr:
#     print(*line)
#
# with open('pb1_matrice.out', 'w') as g:
#     g.writelines([" ".join([str(x) for x in linie])+'\n'
#              for linie in matr])
#
#     ## sau
#     # g.write('\n'.join([" ".join([str(x) for x in linie])
#     #               for linie in matr]))


# ## Problema 2 model test
# f = open(input("nume fisier = ")) # pb2_exemplu.txt
#
# d = {} # dictionar - cuvant:frecventa
#
# for line in f:
#     for cuv in line.lower().split():
#         # if cuv not in d:
#         #     d[cuv] = 1
#         # else:
#         #     d[cuv]+=1
#
#         ## SAU
#         d[cuv] = d.get(cuv,0)+1
#
#
# f.close()
# #print(d)
#
# d_frecv = {} # frecventa:lista cuvinte
#
# for cuv,frecv in d.items():
#     if frecv not in d_frecv:
#         d_frecv[frecv] = []
#     d_frecv[frecv].append(cuv)
#
#     ##SAU (!!ineficient + intre liste !!)
#     # d_frecv[frecv] = d_frecv.get(frecv,[]) + [cuv]
#
# # print(d_frecv)
#
# rez = sorted(d_frecv.items(),reverse=True)
#
# #print(rez)
#
# for frecv,Lcuv in rez:
#     print(f"Frecventa {frecv}: {', '.join(sorted(Lcuv))}")


## PROGRAMARE DINAMICA

# ## Problema 3
#
# f = open("pb3_matrice.in")
# m, n = [int(x) for x in f.readline().split()]
# matr = [[int(x) for x in linie.split()] for linie in f]
#
# f.close()
# print(m, n)
# for linie in matr:
#     print(*linie)
# #s_max[i][j] = suma maxima a numerelor de pe
# # traseul care incepe de la pozitia (i, j)
# s_max = [[0] * n for _ in range(m)]
#
# for i in range(m):
#     for j in range(n):
#         if i == 0 and j == 0:
#             s_max[i][j] = matr[i][j]
#         elif i == 0:
#             s_max[i][j] = matr[i][j] + s_max[i][j - 1]
#         elif j == 0:
#             s_max[i][j] = matr[i][j] + s_max[i - 1][j]
#         else:
#             s_max[i][j] = (matr[i][j] +
#                            max(s_max[i - 1][j], s_max[i][j - 1]))
#
# print()
# for linie in s_max:
#     print(*linie)
#
# L_traseu = [(m - 1, n - 1)]
# i, j = m - 1, n - 1
#
# while i != 0 or j != 0:
#     if i > 0 and (j == 0 or s_max[i - 1][j] >= s_max[i][j - 1]):
#         i -= 1
#     else:
#         j -= 1
#
#     L_traseu.append((i, j))
#
# g = open("pb3_traseu.out", "w")
#
# g.write(f"Suma este: {s_max[-1][-1]}\n")
# g.writelines([f"{i + 1} {j + 1}\n" for i, j, in L_traseu[::-1]])
# g.close()


# ## Problema 4
# 
# f = open("pb4_numere.in")
# L = [int(x) for x in f.readline().split()]
# f.close()
# 
# print(L)
# # s_max[i] = suma maxima posibila a subsecventei care se termina pe pozitia i
# s_max = [0] * len(L)
# s_max[0] = L[0]
# 
# for i in range(1, len(L)):
#     s_max[i] = max(s_max[i - 1] + L[i], L[i])
# 
# print(s_max)
# 
# suma_max = max(s_max)
# pos_ult = s_max.index(suma_max)
# pos_prim = pos_ult
# copie_suma = suma_max
# while copie_suma > 0:
#     copie_suma -= L[pos_prim]
#     pos_prim -= 1
# 
# print(pos_prim, pos_ult)
# 
# g = open("pb4_secventa.out", "w")
# g.write(f"Suma este: {suma_max}\n")
# g.write(" ".join(str(x) for x in L[pos_prim + 1:pos_ult + 1]))
# g.close()
