## Laborator 4, VI 25 oct, ora 16-18

# L[start:stop:pas]

# L = [4,7,2,3,90,5,7,3,4,5]
# L[2:4] = [5,6,7,8,9]
# L[2:4] = []
# L[3:3] [4,5,6,7,8]

## COMPREHENSIUNE

# L = [k for k in range(5) if k % 2 == 1]
#
# L = []
# for ... :
#     if ..:
#         L.append(k)

# ## Problema 1
#
# prop = "Ana  are    mere si 5 pere si 2.5 piersici, alune, ananas"
# L = [cuv for cuv in prop.split() if cuv[0] in "AEIOUaeiou"]
# print(L)
#
# print(prop.split())
# print(prop.split(" "))


# ## Problema 2
#
# prop = "Ana are  3  mere!".lower()
#
# k = int(input("k = "))
# lung = ord("z") - ord("a") + 1
#
# prop2 = [ (chr((ord(c) + k - ord("a")) % lung + ord("a"))
#             if c.isalpha() else c)
#             for c in prop ]
#
# print(''.join(prop2))


# ## Problema 3
#
# prop = "Ana are mere si vreo 3 prune..!".lower()
#
# prop2 = ''.join([ (c + "p" + c if c in "aeiou" else c) for c in prop ])
# print(prop2)
#
# prop2 = ''.join([ (f"{c}p{c}" if c in "aeiou" else c) for c in prop ])
# print(prop2)


# ## Problema 4
# L = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# print(L)

# # problema 5
# n = int(input("n="))
# L = [x * (-1) ** (x + 1) for x in range(1, n + 1)]
# print(L)
# L = [(-x if x % 2 == 0 else x) for x in range(1, n + 1)]
# print(L)

## Problema 8
# L = [2,4,1,7,5,1,8,10]L[i] for i in range(len(L)) if i%2==L[i]%2]
# print(L2)
#
# L2= [nr for poz,nr in enumerate(L) if poz%2==nr%2]
# print(L2)

# #Problema 9
# L = [1,2,3,4,5,6,7]
# L2=[(L[i],L[i+1]) for i in range(len(L)-1)]
# print(L2)
#
# #perechi disjuncte
# L2=[(L[i],L[i+1]) for i in range(0,len(L)-1,2)]
# print(L2)


# #Problema 10
# sir="abcde"
# # print(list(sir))
# L=[sir[i:] + sir[:i] for i in range(len(sir))]
# print(L)


##  OPERATII CU LISTE

# ## Problema 11
# L1 = list(range(0,11))
# L2 = list(range(10, 21))
# L1[::2] = L2[::2]
# print(L1)
# print(L2)

## Problema 12

# L = list(range(20))
# k = int(input("k= "))

#L[:k] = []
#print(L)

#del L[:k]
#print(L)

# for _ in range(k):
#    L.pop(0)
# print(L)

# for i in range(k-1, -1, -1):
#     L.pop(i)
# print(L)

# i = 0
# while i < k:
#     L.pop(0)
#     i+=1
# print(L)

# #Problema 13
#
# L = [1, 0, 4, 5, 0, 0, 6, 7]
# if L.count(0) >= 2:
#     p1 = L.index(0)
#     p2 = L.index(0, p1 + 1)
#     L[p1:p2+1] = []
# print(L)

#Problema 14

# L = [1, 0, 4, 5, 0, 0, 6, 7]

# nr_ap = L.count(0)
# while nr_ap > 0:
#     L.remove(0)
#     nr_ap = nr_ap - 1
# print(L)

# while 0 in L:
#     L.remove(0)
# print(L)

## Problema 2 decriptarea => TEMA
## Pb 6 si 7 => TEMA
## probleme 15 - final => TEMA
