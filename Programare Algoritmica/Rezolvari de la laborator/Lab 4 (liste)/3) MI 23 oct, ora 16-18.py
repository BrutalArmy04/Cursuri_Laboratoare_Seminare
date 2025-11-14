## Laborator 4, MI 23 oct, ora 16-18

# L[start:stop:pas]
#
# L = [3,6,8,2,4,6,9,0,1]
# L[2:4] = [3,4,6,7,8,1,0]
# L[2:4] = []
# L[3:3] = [2,3,5,7,9,4]
#


## COMPREHENSIUNE

# L = [x for x in range(15) if x%2 == 1]

# L = []
# for x ...:
#     if ...:
#         L.append(x)


# ## Problema 1
# prop = "ana are mere   pere ananas   alune".lower()
# print(prop.split())
# print(prop.split(' '))
#
# L=[cuv for cuv in prop.split() if cuv[0] in 'aeiou']
# print(L)


## Problema 2
# prop = "ana are mere, 3 pere, etc.!".lower()
# k = int(input("k= "))
# lung = ord('z') - ord('a') + 1
# L = [(chr((ord(x) - ord('a') + k) % lung + ord('a')) if x.isalpha() else x)
#      for x in prop]
# prop2=''.join(L)
# print(prop2)

## Problema 3
# prop = "Ana are mere.".lower()
# print("".join([(x + 'p' + x if x in 'aeiou' else x) for x in prop]))

## Problema 4
# L = [chr(i) for i in range(ord('a'), ord("z") + 1)]
# print(L)
#
# L2 = [chr(i + ord("a")) for i in range(ord("z") - ord("a") + 1)]
# print(L2)


## Problema 5
# L = [(i if i % 2 else -i) for i in range(1, int(input("n = ")) + 1)]
# print(L)

## Problema 8
# L = [2, 4, 1, 7, 5, 1, 8, 10]
# L2 = [L[i] for i in range(len(L)) if i % 2 == L[i] % 2]
# print(L2)
#
# L3=[ nr for poz, nr in enumerate(L) if poz%2==nr%2]
# print(L3)


## Problema 9
# L = [1,2,3,4]
# L2 = [(L[i],L[i+1]) for i in range(len(L)-1)]
# print(L2)

## Problema 10
# sir = "abcde"
# L = [sir[i:] + sir[:i] for i in range(len(sir))]
# print(L)

## OPERATII CU LISTE

## Problema 11
# L1 = [0,1,2,3,4,5,6,7,8,9,10]
# L2 = [10,11,12,13,14,15,16,17,18,19,20]
# L1[::2] = L2[::2]
# print(L1)
# print(L2)

## Problema 12
# L = list(range(20))
# k = int(input("k= "))

## a)
# L[:k] = []
# print(L)

## b)
# for _ in range(k):
#     L.pop(0)
# print(L)

## c)
# for i in range(k-1,-1,-1):
#     L.pop(i)
# print(L)

## d)
# i = 0
# while i < k:
#     L.pop(0)
#     i=i+1
# print(L)


## Problema 13

# L = [3,6,0,8,6,3,9,0,2, 7, 0, 2, 1, 0]

## a)

# if L.count(0) > 1:
#     p1 = L.index(0)
#     p2 = L.index(0, p1 + 1)
#     L[p1:p2 + 1] = []
#     print(L)

## b)
# zeros = []
# for i in range(len(L)):
#     if L[i] == 0:
#         zeros.append(i)
#         if len(zeros) == 2:
#             L[zeros[0]:zeros[1] + 1] = []
#             break    
# print(L)


## Problema 2 decriptarea => TEMA
## Pb 6 si 7 => TEMA
## probleme 14 - final => TEMA
