## Laborator 14, JO 16 ian, ora 12-14
# # Problema 1
# with open("pb1_cuvinte.in") as f:
#     L_cuv = f.read().strip().split()
# print(L_cuv)
#
# # lungMax[i]=lungimea maxima a uniu subsir care se termina cu cuvantul de pe poz i
# # pred[i]=indicele cuvantului anterior cuvantului i in subsir
# lungMax = [1] * len(L_cuv)
# pred = [-1] * len(L_cuv)
#
# for i in range(1, len(L_cuv)):
#     for j in range(i):
#         if L_cuv[j][-2:] == L_cuv[i][:2]:
#             if lungMax[i] < lungMax[j] + 1:
#                 lungMax[i]=lungMax[j]+1
#                 pred[i]=j
#
# print(lungMax)
# print(pred)
#
# poz_lungMax=lungMax.index(max(lungMax))
# sol=[]
#
# poz=poz_lungMax
# while poz!=-1:
#     sol.append(L_cuv[poz])
#     poz=pred[poz]
#
# print(sol)
#
# g=open("pb1_cuvinte.out","w")
# # g.writelines([cuv+"\n" for cuv in sol[::-1]])
# ##sau
# # g.writelines([f"{cuv}\n" for cuv in sol[::-1]])
# ##sau
# sol.reverse()
# g.write('\n'.join(sol))
# g.close()


# ## Problema 2
#
# s = "SUBSIR"
# t = "RUSTICE"
#
# M = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
#
# for i in range(1, len(s) + 1):
#     for j in range(1, len(t) + 1):
#         if s[i - 1] == t[j - 1]:
#             M[i][j] = 1 + M[i - 1][j - 1]
#         else:
#             M[i][j] = max(M[i][j - 1], M[i - 1][j])
#
# for linie in M:
#     print(*linie)
#
# sol = []
# i = len(s)
# j = len(t)
# # while i != 0 and j != 0:
# ## sau
# while M[i][j] != 0:
#     if s[i - 1] == t[j - 1]:
#         sol.append(s[i - 1])
#         i -= 1
#         j -= 1
#     else:
#         if M[i - 1][j] >= M[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1
# print(sol)
#
# print("".join(sol[::-1]))


# ## Problema 3
#
# f = open("pb3_numere.in")
# n = int(f.readline())
# L = [int(x) for x in f.readline().split()]
# suma = int(f.readline())
# f.close()
# # print(L, suma)
#
# d = {} #suma platibila: ultimul numar adaugat la suma
#
# for nr in L:
#     for s in list(d.keys()):
#         if nr + s not in d and nr + s <= suma:
#             d[nr + s] = nr
#     if nr not in d and nr <= suma:
#         d[nr] = nr
#
# print(d)
# g = open("pb3_numere.out", "w")
# if suma not in d:
#     g.write(f"Suma {suma} nu poate fi obtinuta din numerele date\n")
# else:
#     sol = []
#     elem = suma
#     while d[elem] != elem:
#         sol.append(d[elem])
#         elem = d[elem]
#     g.write(" ".join(str(x) for x in sol))
# g.close()


# ## Problema 5
# 
# f = open("pb5_cuburi.in")
# n = int(f.readline())
# L = [cub for cub in f.readlines()]
# f.close()
# 
# L_cuburi = []
# for cub in L:
#     latura, culoare = cub.strip().split()
#     L_cuburi.append((int(latura), culoare))
# 
# L_cuburi.sort()
# print(L_cuburi)
# # hMax[i] = inaltimea maxima a turnului care se termina cu cubul i (are la baza)
# # pred[i] = pozitia cubului de deasupra cubului i in turn
# # nrTurnuri[i] = numarul turnurilor de inaltime maxima, care se termina cu cubul i
# 
# hMax = [cub[0] for cub in L_cuburi]
# pred = [-1] * len(L_cuburi)
# nrTurnuri = [1] * len(L_cuburi)
# 
# hMax[0] = L_cuburi[0][0]
# nrTurnuri[0] = 1
# for i in range(1, len(L_cuburi)):
#     for j in range(0, i):
#         if L_cuburi[i][1] != L_cuburi[j][1] \
#             and L_cuburi[i][0] > L_cuburi[j][0]:
# 
#             if hMax[i] < hMax[j] + L_cuburi[i][0]:
#                 hMax[i] = hMax[j] + L_cuburi[i][0]
#                 pred[i] = j
#                 nrTurnuri[i] = nrTurnuri[j]
# 
#             elif hMax[i] == hMax[j] + L_cuburi[i][0]:
#                 nrTurnuri[i] += nrTurnuri[j]
# 
# print(hMax, pred, nrTurnuri, sep="\n")
# 
# pozMax = hMax.index(max(hMax))
# print(pozMax)
# 
# poz = pozMax
# sol = []
# 
# while poz != -1:
#     sol.append(L_cuburi[poz])
#     poz = pred[poz]
# 
# print(sol)
# print(f"Nr turnuri = {nrTurnuri[pozMax]}")
