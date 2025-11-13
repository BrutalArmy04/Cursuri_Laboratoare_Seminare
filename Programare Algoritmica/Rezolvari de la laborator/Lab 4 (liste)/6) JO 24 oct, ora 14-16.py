## Laborator 4, JO 24 oct, ora 14-16

# L[start:stop:pas]
#
# L = [5,7,9,2,3,0,1,6]
# L[2:4] = [7,4,5,2,3,0]
# L[2:4] = []
# L[3:3] [6,7,8,3,5]

## COMPREHENSIUNE

# L = [k for k in range(5) if k % 2 == 1]
#
# L = []
# for ...:
#     if ...:
#         L.append(k)


# ## Problema 1
#
# prop = "ana   are mere ananas alune  banane ".lower()
# L = [cuv for cuv in prop.split() if cuv[0] in "aeiou"]
# print(L)
#
# print(prop.split())
# print(prop.split(" "))


# ## Problema 2
# prop = "ana are 3 mere!".lower()
# k = int(input('k = '))
# lung = ord('z') - ord('a') + 1
# L = [(chr((ord(c) - ord('a') + k) % lung + ord('a')) if c.isalpha() else c)
#      for c in prop]
# prop2 = "".join(L)
# print(prop2)


# ## Problema 3
# prop = "ana are 3 mere, 5 pere!".lower()
# prop2 = "".join([(c + 'p' + c if c in "aeiou" else c) for c in prop])
# print(prop2)
#
# prop3 = "".join([(f"{c}p{c}" if c in "aeiou" else c) for c in prop])
# print(prop3)


# ## Problema 4
# L = [chr(x) for x in range(ord('a'), ord('z')+1)]
# print(L)


# ## Problema 5
# n = int(input("n= "))
# L = [(x if x%2==1 else -x) for x in range(1, n+1)]
# print(L)
#
# L = [(-1)**(x+1) * x for x in range(1, n+1)]
# print(L)

# ## Problema 8
# L = [2, 4, 1, 7, 5, 1, 8, 10]
# L2 = [L[i] for i in range(len(L)) if L[i] % 2 == i % 2]
# print(L2)
#
# L3 = [nr for poz, nr in enumerate(L) if poz % 2 == nr % 2]
# print(L3)

# ## Problema 9
# L = [1, 2, 3, 4, 5, 6, 7]
# # L2 = [(L[i], L[i+1]) for i in range(len(L)-1)]
# # print(L2)
#
# L2 = [(L[i], L[i+1]) for i in range(0, len(L)-1, 2)]
# print(L2)


# ## Problema 10
# sir = "abcde"
# L = [sir[i:] + sir[:i] for i in range(len(sir))]
# print(L)


## OPERATII CU LISTE

# ## Problema 11
# L1 = list(range(0, 11))
# L2 = list(range(10, 21))
# L1[::2] = L2[::2]
# print(L1)
# print(L2)


## Problema 12
# L = list(range(20))
# k = int(input("k= "))
#
# # L[:k]=[]
# # print(L)
#
# # del L[:k]
# # print(L)
#
# # for _ in range(k):
# #     L.pop(0)
# # print(L)
#
# # for i in range(k-1,-1,-1):
# #     L.pop(i)
# # print(L)
#
# # i=k-1
# # while i>=0:
# #     L.pop(i)
# #     i-=1
# # print(L)
#
# # i=0
# # while i<k:
# #     L.pop(0)
# #     i+=1
# # print(L)


# ## Problema 13
# L = [5,8,0,3,4,0,7,9,0,4,5,0,2]
# if L.count(0) >= 2:
#     p1 = L.index(0)
#     p2 = L.index(0, p1 + 1)
#     L[p1:p2 + 1] = []
# print(L)


# ## Problema 14
# L = [5,8,0,3,4,0,7,9,0,4,5,0,2]
# # for _ in range(L.count(0)):
# # #     L.remove(0)
# # # print(L)
#
# while 0 in L:
#     L.remove(0)
# print(L)


# L_nr = [int(nr) for nr in input("Introduceti numerele: ").split()]
# print(L_nr)


## Problema 2 decriptarea => TEMA
## Pb 6 si 7 => TEMA
## probleme 15 - final => TEMA
