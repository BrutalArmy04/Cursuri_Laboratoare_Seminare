## Laborator 11, JO 12 dec, ora 14-16

# ## Problema 1
#
# def munte(L, st, dr):
#     if dr - st + 1 < 3:
#         return False
#     mij = (st + dr) // 2
#     if L[mij - 1] < L[mij] > L[mij + 1]:
#         return L[mij], mij
#     if L[mij - 1] > L[mij]:
#         return munte(L, st, mij)
#     return munte(L, mij, dr)
#
#
# with open('pb1_date.in') as f:
#     n = int(f.readline())
#     L = [int(x) for x in f.readline().split()]
#     print(munte(L, 0, n - 1))


# ## Problema 2
#
# def nr_aparitii(L, x):
#     def prima_aparitie(L, x, st, dr):
#         if L[0] == x:
#             return 0
#         if st > dr:
#             return -1
#         mij = (st + dr) // 2
#         if L[mij] == x and L[mij - 1] < L[mij]:
#             return mij
#         if x <= L[mij]:
#             return prima_aparitie(L, x, st, mij - 1)
#         return prima_aparitie(L, x, mij + 1, dr)
#
#     def ultima_aparitie(L, x, st, dr):
#         if L[-1] == x:
#             return len(L) - 1
#         if st > dr:
#             return -1
#         mij = (st + dr) // 2
#         if L[mij] == x and L[mij] < L[mij + 1]:
#             return mij
#         if x < L[mij]:
#             return ultima_aparitie(L, x, st, mij - 1)
#         return ultima_aparitie(L, x, mij + 1, dr)
#
#     stanga = prima_aparitie(L, x, 0, len(L) - 1)
#     dreapta = ultima_aparitie(L, x, 0, len(L) - 1)
#     print(stanga, dreapta)
#     if stanga == -1 or dreapta == -1:
#         return -1
#     return dreapta - stanga + 1
#
#
# L = [1, 1, 2, 2, 2, 2, 6, 9, 9, 20]
# print(nr_aparitii([1, 1, 2, 2, 2, 2, 6, 9, 9, 20], 2))


## Problema 3

# n = 5
# 1 12 15 16 38
# 2 13 17 30 45
#
# 15 16 38
# 2 13 17
#
# 15 16
# 13 17
#
# 13 15 16 17 => mediana = (15+16)/2 = 15.5
#
# 1 2 12 13 15 16 17 30 38 45
# mediana = (15+16)/2 = 15.5

# 
# def mediana(L1, st1, dr1, L2, st2, dr2):
#     print(L1[st1:dr1 + 1], L2[st2:dr2 + 1])
#
#     if dr1 - st1 + 1 == 2 and dr2 - st2 + 1 == 2:
#         R = sorted([L1[st1], L1[dr1], L2[st2], L2[dr2]])
#         return (R[1] + R[2]) / 2
#
#     if (st1 - dr1 + 1) % 2 == 0:
#         mij1_st = (st1 + dr1) // 2
#         mij1_dr = mij1_st + 1
#     else:
#         mij1_st = mij1_dr = (st1 + dr1) // 2
#
#     if (st2 - dr2 + 1) % 2 == 0:
#         mij2_st = (st2 + dr2) // 2
#         mij2_dr = mij2_st + 1
#     else:
#         mij2_st = mij2_dr = (st2 + dr2) // 2
#
#     mediana1 = (L1[mij1_st] + L1[mij1_dr]) / 2
#     mediana2 = (L2[mij2_st] + L2[mij2_dr]) / 2
#
#     if mediana1 == mediana2:
#         return mediana1
#
#     if mediana1 < mediana2:
#         return mediana(L1, mij1_st, dr1, L2, st2, mij2_dr)
#
#     return mediana(L1, st1, mij1_dr, L2, mij2_st, dr2)
#
#
# L1 = [1, 12, 15, 16, 38]
# L2 = [2, 13, 17, 30, 45]
#
# print(mediana(L1, 0, len(L1) - 1, L2, 0, len(L2) - 1))

