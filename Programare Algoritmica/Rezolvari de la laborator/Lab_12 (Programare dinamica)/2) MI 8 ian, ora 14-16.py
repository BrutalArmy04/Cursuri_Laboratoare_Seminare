## Laborator 13, MI 8 ian, ora 14-16

# ## Problema 1 model test
#
# f = open("pb1_matrice.in", "r")
# M = [[int(x) for x in linie.split()] for linie in f]
# f.close()
#
# for linie in M:
#     print(*linie)
#
# for i in range(len(M)):
#     M[i].remove(max(M[i]))
#     M[i].remove(max(M[i]))
#
# for linie in M:
#     print(*linie)
#
# g = open("pb1_matrice.out", "w")
# # g.write("\n".join([" ".join([str(x) for x in linie])
# #                    for linie in M]))
#
# g.writelines([" ".join([str(x) for x in linie]) + "\n"
#                    for linie in M])
# g.close()


# ## Problema 2 model test
# filename = input("name= ") #pb2_exemplu.txt
# f = open(filename, "r")
# d = {} #cuvant:frecventa
# for linie in f:
#     # L_cuv=[cuv.lower() for cuv in linie.split()]
#     ##sau
#     L_cuv = linie.lower().split()
#     for cuv in L_cuv:
#         d[cuv] = d.get(cuv, 0)+1
# f.close()
# print(d)
#
# d2={} #frecventa:lista cuvinte
# for cuv,frecv in d.items():
#     if frecv not in d2:
#         d2[frecv] = [cuv]
#     else:
#         d2[frecv].append(cuv)
#         # d2[frecv] += [cuv]
#
#     ## sau
#     #d2[frecv] = d2.get(frecv, []) + [cuv]
#
# print(d2)
#
# rez = sorted(d2.items(), reverse=True)
# for frecv,L_cuv in rez:
#     print(f"Frecventa {frecv}: {' '.join(sorted(L_cuv))}")


## PROGRAMARE DINAMICA

# ## Problema 3
#
# with open("pb3_matrice.in","r") as f:
#     # m,n = map(int,f.readline().split())
#     m,n = [int(x) for x in f.readline().split()]
#     matrice = [ [int(x) for x in linie.split()] for linie in f]
#
# # for linie in matrice:
# #     # for x in linie:
# #     #     print(x,end=" ")
# #     # print()
# #     print(*linie)
#
# #smax[i][j] = suma maxima a traseului care se termina la pozitia (i,j)
# smax = [[0] * n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if i==j==0:
#             smax[i][j] = matrice[i][j]
#         elif i == 0:
#             smax[i][j] = matrice[i][j] + smax[i][j-1]
#         elif j==0:
#             smax[i][j] = matrice[i][j] + smax[i-1][j]
#         else:
#             smax[i][j] = matrice[i][j] + max(smax[i-1][j],smax[i][j-1])
#
# for linie in smax:
#     print(*linie)
#
# L_traseu = [(m-1,n-1)]
# i = m-1
# j = n-1
# while i!=0 or j!=0:
#     if i!=0 and (j==0 or smax[i-1][j]>=smax[i][j-1]):
#         i = i - 1
#     else:
#         j = j - 1
#     L_traseu.append((i,j))
# print(L_traseu)
#
# with open("pb3_traseu.out","w") as g:
#     g.write(f"Suma este {smax[-1][-1]}\n")
#     g.writelines([f"{i+1} {j+1}\n" for i,j in L_traseu[::-1]])


# ## Problema 4
#
# with open("pb4_numere.in") as f:
#     L = [int(x) for x in f.readline().split()]
#
# print(L)
#
# # smax[i] suma maxima a subsecventei care se termina pe pozitia i
# smax = [0] * len(L)
#
# smax[0] = L[0]
# for i in range(1, len(L)):
#     # smax[i] = L[i] + max(0, smax[i - 1])
#     ## SAU
#     smax[i] = max(L[i], L[i] + smax[i - 1])
#
# print(smax)
#
# suma_max = max(smax)
#
# poz_ult = smax.index(suma_max)
# poz_prim = poz_ult
#
# copie_suma_max = suma_max
# while copie_suma_max > 0:
#     copie_suma_max -= L[poz_prim]
#     poz_prim -= 1
#
# print(poz_prim, poz_ult)
#
# with open("pb4_secventa.out", "w") as g:
#     g.write(f"Suma este {suma_max}\n")
#     g.write(" ".join([str(x) for x in L[poz_prim + 1: poz_ult + 1]]))

