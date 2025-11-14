## Laborator 4, MI 23 oct, ora 12-14

# L = [2, 3, 4, 5, 6, 7]
#
# if 3 in [1, 2, 3, 4, 5]:
#     print("este")
#
# L[2:4] = []
# L[3:3] = [10, 11, 12]
#

# L = [x for x in range(5) if x%2 == 1]
#
# L = []
# for ...:
#     if ... :
#         L.append(x)

## COMPREHENSIUNE

# # Problema 1
# propozitie = "Ana are mere si pere, dar ananas nu are"
# L_vocale = [cuv for cuv in propozitie.split() if cuv[0] in "aeiouAEIOU"]
# print(L_vocale)

## Problema 2
## a) criptarea
# prop = "ana are multe mere, dar nu are 7 banane!".lower()
# k=int(input("k= "))
# lung = ord("z") - ord("a") + 1
# l_cesar = [(chr((ord(x) - ord("a") + k) % lung + ord("a")) if x.isalpha() else x)
#            for x in prop]
# prop2="".join(l_cesar)
# print(prop2)

## b) decriptarea => TEMA


# ## Problema 3 - pasareasca
# prop = "Ana are mere.".lower()
#
# l_cuv = [(c+"p"+c if c in "aeiou" else c) for c in prop ]
# prop2="".join(l_cuv)
# print(prop2)

# ## Problema 4
#
# prop = [chr(i) for i in range(ord('a'),ord('z')+1)]
# print(prop)


# ## Problema 5
# n=int(input("n= "))
# L=[(-x if x%2==0 else x) for x in range(1,n+1)]
# print(L)

## Pb 6 si 7 => TEMA

# ## Problema 8
# L = [2, 4, 1, 7, 5, 1, 8, 10]
# L2 = [L[i] for i in range(len(L)) if i % 2 == L[i] % 2]
# print(L2)


# # Problema 9
# L = [1, 2, 3, 4]
# L2 =  [(L[i],L[i+1]) for i in range(len(L)-1)]
# print(L2)

## Problema 10
# sir = "abcde"
# L = [sir[i:] + sir[:i] for i in range(len(sir))]
# print(L)


## OPERATII CU LISTE

## Problema 11

# L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# L2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# L1[::2] = L2[::2]
# print(L1)
# print(L2)

## Problema 12

# L = list(range(15))
# print(L)
# k = int(input("k= "))

# #a)
# L[:k] = []
# print(L)

# #b)
# for i in range(k-1, -1, -1):
#     L.pop(i)
# print(L)

## c)
# for i in range(k):
#     L.pop(0)
# print(L)


## Problema 13
# L = list(range(1,20))
# L[6] = L[9] = L[11] = 0
# print(L)
#
# if L.count(0) >= 2:
#     p1 = L.index(0)
#     p2 = L.index(0, p1+1)
#     L[p1:p2+1]=[]
#     print(L)


## Problema 2 decriptarea => TEMA
## Pb 6 si 7 => TEMA
## probleme 14 - final => TEMA

