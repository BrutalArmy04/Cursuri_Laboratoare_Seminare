## Laborator 11, MI 11 dec, ora 12-14

from functools import lru_cache
@lru_cache(maxsize=None)

# ## Problema 1
#
# def munte(L, st, dr):
#     if dr-st<2:
#         print(L[st:dr+1])
#         return False
#     mij = (st + dr) // 2
#     if L[mij-1] < L[mij] > L[mij+1]:
#         return L[mij], mij
#     if L[mij-1] > L[mij]:
#         return munte(L,st,mij) #apel pe stanga
#     return munte(L,mij,dr) #apel pe dreapta
#
#
# f = open("pb1_date.in")
# n = int(f.readline())
# L = [int(x) for x in f.readline().split()]
# f.close()
# print(L)
# print(munte(L, 0, len(L) - 1))

# # Problema 2
# def nrAparitii(L, x):
#     def primaAparitie(L, x, st, dr):
#         if st == dr and L[st] != x:
#             return -1  # x nu exista
#         if L[0] == x:
#             return 0
#         mij = (st + dr) // 2
#         if L[mij] == x and mij - 1 >= 0 and L[mij - 1] != x:
#             return mij
#         if x <= L[mij]:
#             return primaAparitie(L, x, st, mij - 1)
#         return primaAparitie(L, x, mij, dr)
#
#     def ultimaAparitie(L, x, st, dr):
#         if st == dr and L[st] != x:
#             return -1  # x nu exista
#         if L[-1] == x:
#             return len(L) - 1
#         mij = (st + dr) // 2
#         if L[mij] == x and mij + 1 < len(L) and L[mij + 1] != x:
#             return mij
#         if L[mij] > x:
#             return ultimaAparitie(L, x, st, mij - 1)
#         return ultimaAparitie(L, x, mij + 1, dr)
#
#     prim = primaAparitie(L, x, 0, len(L) - 1)
#     ultim = ultimaAparitie(L, x, 0, len(L) - 1)
#     print(prim, ultim)
#     if prim == -1 or ultim == -1:
#         return -1
#     return ultim - prim + 1
#
#
# L = [int(x) for x in input("Numerele: ").split()]
# L.sort()
# x = int(input("Numar cautat: "))
# print(nrAparitii(L, x))


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

# 1 2 12 13 15 16 17 30 38 45
# mediana = (15+16)/2 = 15.5

def mediana(L1, st1, dr1, L2, st2, dr2):
    if dr1 - st1 == 1 and dr2 - st2 == 1:
        R = sorted([L1[st1], L1[dr1], L2[st2], L2[dr2]])
        return (R[1] + R[2]) / 2

    mij1 = (st1 + dr1) // 2
    mij2 = (st2 + dr2) // 2
    med1 = med2 = None
    if (dr1 - st1 + 1) % 2 == 0:
        med1 = (L1[mij1] + L1[mij1 + 1]) / 2
    else:
        med1 = L1[mij1]

    if (dr2 - st2 + 1) % 2 == 0:
        med2 = (L2[mij2] + L2[mij2 + 1]) / 2
    else:
        med2 = L2[mij2]

    if med1 == med2:
        return med1

    elif med1 < med2:
        if (dr2 - st2 + 1) % 2 == 0:
            mij2 += 1
        return mediana(L1, mij1, dr1, L2, st2, mij2)


    else:  # med1>med2
        if (dr1 - st1 + 1) % 2 == 0:
            mij1 += 1
        return mediana(L1, st1, mij1, L2, mij2, dr2)


L1 = [1, 12, 15, 16, 38]
L2 = [2, 13, 17, 30, 45]
print(mediana(L1, 0, len(L1) - 1, L2, 0, len(L2) - 1))

