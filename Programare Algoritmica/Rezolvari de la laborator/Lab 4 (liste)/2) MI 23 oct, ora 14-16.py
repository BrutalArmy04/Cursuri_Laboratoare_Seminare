## Laborator 4, MI 23 oct, ora 14-16
#
# L[start:stop:pas]
#
# L = list(range(15))
# L[3:7] = [1, 5, 7, 8, 3, 9]
# L[3:7] = []
# L[3:3] = [23, 5, 8, 4]

# L = [k for k in range(5) if k%2 == 1]
#
# L = []
# for k ... :
#     if  ...:
#         L.append(k)


## COMPREHENSIUNE

# ## Problema 1
# prop = "Ana are mere,   pere, nuci, alune,   'ananas'!"
# L = [cuvant for cuvant in prop.split() if (cuvant.strip(" ,.:;?!'"))[0] in "AEIOUaeiou" ]
# print(L)


## Problema 2
# # a)
# prop = "O zi frumoasa! 548".lower()
# k = int(input("Introdu k: "))
# lung = ord("z") - ord("a") + 1
#
# L = [(chr((ord(x) - ord("a") + k) % lung + ord("a")) if x in "aeiou" else x)
#      for x in prop]
#
# prop2 = "".join(L)
# print(prop2)


## Problema 3
# prop = "Ana are mere.".lower()
# L = [(x+"p"+x if x in "aeiou" else x) for x in prop]
# prop2 = "".join(L)
# print(prop2)


## Problema 4
# L = [chr(i) for i in range(ord('a'),ord('z')+1)]
# print(L)

## Problema 5
# n=int(input("n= "))
# L=[(-i if i%2==0 else i) for i in range(1,n+1)]
# print(L)

## Problema 8
# L = [2, 4, 1, 7, 5, 1, 8, 10]
# L2 = [L[i] for i in range(len(L)) if i % 2 == L[i] % 2]
# print(L2)

# L3 = [x for i, x in enumerate(L) if i%2 == x %2]
# print(L3)

## Problema 9
# L = [1, 2, 3, 4]
# L2 = [(L[i], L[i+1]) for i in range(0,len(L)-1)]
# print(L2)

## Problema 10
# sir = "abcde"
# L = [sir[i:] + sir[:i] for i in range(len(sir))]
# print(L)


## OPERATII CU LISTE

## Problema 11
# L1 = [0,1,2,3,4,5,6,7,8,9,10]
# L2 = [10,11,12,13,14,15,16,17,18,19,20]
#
# L1[::2] = L2[::2]
# print(L1)
# print(L2)

## Problema 12
# L = list(range(20))
# k = int(input("k= "))

# a)
# L[:k] = []
# print(L)

## b)
# for i in range(k):
#     L.pop(0)
#
# print(L)

# # c)
# for i in range(k-1,-1,-1):
#     L.pop(i)
#
# print(L)


## Problema 13

# L = list(range(1, 20))
# L[3] = L[7] = L[18] = 0
#
# print(L)
#
# if L.count(0) >= 2:
#     p1 = L.index(0)
#     p2 = L.index(0, p1 + 1)
#     L[p1:p2 + 1] = []
#
# print(L)


## Problema 14
#
# L = [3,0,0,7,0,2,6,0,9,4,8,0]
#
# # for i in range(L.count(0)):
# #     L.remove(0)
# # print(L)
#
# while 0 in L:
#     L.remove(0)
# print(L)


## Problema 2 decriptarea => TEMA
## Pb 6 si 7 => TEMA
## probleme 15 - final => TEMA
