## Laborator 14, MI 15 ian, ora 12-14
# ## Problema 1
# ## masa carte sac teatru tema rustic sare
# ## carte teatru rustic
# f = open("pb1_cuvinte.in")
# L_cuv = f.read().strip().split()
# f.close()
# print(L_cuv)
#
# #L_max[i] = lungimea maxima a subsirului care se termina cu cuv de pe poz i
# #pred[i] = pozitia cuvantului predecesor al cuv de pe poz i
#
# L_max = [1] * len(L_cuv)
# pred = [-1] * len(L_cuv)
#
# L_max[0] = 1
# for i in range(1,len(L_cuv)):
#     for j in range(i):
#         if L_cuv[j][-2:] == L_cuv[i][:2]:
#             if L_max[j] + 1 > L_max[i]:
#                 L_max[i] = L_max[j] + 1
#                 pred[i] = j
# print(L_max)
# print(pred)
#
# poz_long_max = L_max.index(max(L_max))
# sol = [L_cuv[poz_long_max]]
# poz = poz_long_max
# while pred[poz] != -1:
#     poz = pred[poz]
#     sol.append(L_cuv[poz])
# print(sol)
#
# g = open("pb1_cuvinte.out", 'w')
# g.writelines([cuv + '\n' for cuv in sol[::-1]])
# ## sau
# #g.write("\n".join(sol[::-1]))
# g.close()



# ## Problema 2
# s = "SUBSIR"
# t = "RUSTICE"
#
# M =[[0]*(len(t)+1) for _ in range(len(s)+1)]
# # for linie in M:
# #     print(*linie)
#
# for i in range(1,len(s)+1):
#     for j in range(1,len(t)+1):
#         if s[i-1] == t[j-1]:
#             M[i][j] = 1 + M[i-1][j-1]
#         else:
#             M[i][j] = max(M[i][j-1],M[i-1][j])
#
# for linie in M:
#     print(*linie)
#
# sol=[]
# i=len(s)
# j=len(t)
# while i>0 and j>0: ## am corectat sa fie and, nu or
#     if s[i-1] == t[j-1]:
#         sol.append(s[i-1])
#         i-=1
#         j-=1
#     else:
#         if M[i][j-1] > M[i-1][j]:
#             j-=1
#         else:
#             i-=1
# print(sol)
#
# print("".join(sol[::-1]))



# ## Problema 3
# 
# f = open("pb3_numere.in")
# 
# n = int(f.readline())
# L = [int(x) for x in f.readline().split()]
# M = int(f.readline()) # M = suma
# f.close()
# print(L, M)
# 
# d = {}
# for x in L:
#     for y in list(d.keys()):
#         if y+x not in d:
#             d[y+x] = x
# 
#     if x not in d:
#         d[x] = x
# print(*d.items(), sep = "\n")
# 
# if M not in d:
#     print("Nu exista submultime")
# else:
#     sol = []
#     nr = M
#     while d[nr] != nr:
#         nr = d[nr]
#         sol.append(nr)
# 
#     print(sol)


## Pentru rezolvarea de la Problema 5 (turn cuburi), vedeti fisierele de joi.
