## Laborator 14, JO 16 ian, ora 14-16

# ## Problema 1
# f = open("pb1_cuvinte.in")
# L = f.readline().strip().split()
# f.close()
# print(L)
#
# # lungMax[i] = lungimea maxima a subsurilui care se termina cu cuv i
# # pred[i] = poz cuv predecesor in subsir fata de cuv i
#
# lungMax = [1] * len(L)
# pred = [-1] * len(L)
#
# for i in range(1, len(L)):
#     for j in range(i):
#         if L[j][-2:] == L[i][:2]:
#             if lungMax[i] < lungMax[j] + 1:
#                 lungMax[i] = lungMax[j] + 1
#                 pred[i] = j
#
# print(lungMax)
# print(pred)
#
# sol = []
# pozLungMax = lungMax.index(max(lungMax))
# poz = pozLungMax
#
# while poz != -1:
#     sol.append(L[poz])
#     poz = pred[poz]
#
# print(sol)
#
# g = open("pb1_cuvinte.out", 'w')
#
# g.write('\n'.join(sol[::-1]))
# g.close()


# ## Problema 2
#
# s = 'SUBSIR'
# t = 'RUSTICE'
#
# M = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
#
# for i in range(1, len(s) + 1):
#     for j in range(1, len(t) + 1):
#         if s[i - 1] == t[j - 1]:
#             M[i][j] = 1 + M[i - 1][j - 1]
#         else:
#             M[i][j] = max(M[i - 1][j], M[i][j - 1])
#
# for linie in M:
#     print(*linie)
#
# sol = []
# i = len(s)
# j = len(t)
#
# while i != 0 and j != 0:
#     if s[i - 1] == t[j - 1]:
#         sol.append(s[i - 1])
#         i -= 1
#         j -= 1
#     else:
#         if M[i - 1][j] >= M[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1
#
# print(sol)
# print("".join(sol[::-1]))


# ## Problema 3
# f = open("pb3_numere.in","r")
# n = int(f.readline())
# L=[int(x) for x in f.readline().split()]
# suma = int(f.readline())
# f.close()
# print(L,suma)
#
# d = {} #suma platibila : ultimul numar adaugat la suma
# for x in L:
#     for s in list(d):
#         if x + s not in d and x + s <= suma:
#             d[x+s] = x
#     if x not in d and x <= suma:
#         d[x] = x
# print(d)
#
# sol = []
# s = suma
# while s != d[s]:
#     sol.append(d[s])
#     s=d[s]
# print(sol)
#
# g = open("pb3_numere.out","w")
# g.write(" ".join([str(x) for x in sol]))
# g.close()


# ## Problema 5
# 
# f = open("pb5_cuburi.in", "r")
# n = int(f.readline())
# L = [cub.strip().split() for cub in f]
# f.close()
# 
# for i in range(len(L)):
#     L[i][0] = int(L[i][0])
# 
# L.sort()
# print(L)
# 
# # hMax[i] = inaltimea maxima a turnului
# #           care se termina cu cubul i
# # pred[i] = pozitia cubului anterior in turn
# #           cubului i
# # nrTurnuri[i] = numar de turnuri de inaltime
# #               maxima care se termina cu
# #               cubul i
# 
# hMax = [cub[0] for cub in L]
# pred = [-1] * len(L)
# nrTurnuri = [1] * len(L)
# 
# for i in range(1, len(L)):
#     for j in range(i):
#         if L[i][1] != L[j][1] and L[i][0] > L[j][0]:
#             if hMax[i] < hMax[j] + L[i][0]:
#                 hMax[i] = hMax[j] + L[i][0]
#                 pred[i] = j
#                 nrTurnuri[i] = nrTurnuri[j]
#             elif hMax[i] == hMax[j] + L[i][0]:
#                 nrTurnuri[i] += nrTurnuri[j]
# 
# print(hMax, pred, nrTurnuri, sep='\n')
# 
# pozhMax = hMax.index(max(hMax))
# poz = pozhMax
# sol = []
# 
# while poz != -1:
#     sol += L[poz]
#     poz = pred[poz]
# 
# print(sol, nrTurnuri[pozhMax])

