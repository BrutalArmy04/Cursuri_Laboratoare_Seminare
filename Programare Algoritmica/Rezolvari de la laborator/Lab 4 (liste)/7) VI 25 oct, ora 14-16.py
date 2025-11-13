## Laborator 4, VI 25 oct, ora 14-16

# L[start:stop:pas]
# L = [4,6,7,2,3,0,9,1]
# L[2:4] = [2,3,7,8,9]
# L[2:4] = []
# L[3:3] = [5,6,8]

## COMPREHENSIUNE

# L = [k for k in range(5) if k % 2 == 1]
#
# L = []
# for ... :
#     if .. :
#         L.append(k)


# ## Problema 1
# prop = "ana are mere    pere  alune  ananas"
# s=[cuv for cuv in prop.split() if cuv[0] in "AEIOUaeiou"]
# print(s)
#
# print(prop.split())
# print(prop.split(" "))


# ## Problema 2
# prop = "Ana are 3 mere, 5 pere!".lower()
# k = int(input("Introduceti cheia criptarii: "))
# lung = ord('z') - ord('a') + 1
# L = [(chr((ord(c) - ord('a') + k) % lung + ord('a')) if c.isalpha() else c)
#      for c in prop]
# print(L)
# prop2 = "".join(L)
# print(prop2)


# ## Problema 3
# prop = "ana are 3 mere, 4 pere!".lower()
# prop2=''.join([(c+'p'+c if c in "aeiou" else c) for c in prop ])
# print(prop2)
#
# prop3=''.join([(f"{c}p{c}" if c in "aeiou" else c) for c in prop ])
# print(prop3)

# ## Problema 4
# L=[chr(x) for x in range(ord("a"),ord("z")+1)]
# print(L)

# ## Problema 5
# n=int(input("n= "))
# L=[(-x if x%2==0 else x) for x in range(1,n+1)]
# print(L)
#
# L=[(-1)**(x+1)*x for x in range(1,n+1)]
# print(L)


# ## Problema 8
# L = [2,4,1,7,5,1,8,10]
# L2 = [L[i] for i in range(len(L)) if i%2==L[i]%2]
# print(L2)
#
# L3 = [nr for poz,nr in enumerate(L) if poz%2==nr%2]
# print(L3)

# ## Problema 9
# #perechi ca in enunt
# L=[1,2,3,4,5,6, 7]
# L2=[(L[k], L[k+1]) for k in range(len(L)-1)]
# print(L2)
#
# #perechi disjuncte
# L2=[(L[k], L[k+1]) for k in range(0, len(L)-1, 2)]
# print(L2)


# ## Problema 10
# sir = 'abcde'
# L = [sir[i:]+sir[:i] for i in range(len(sir))]
# print(L)


## OPERATII CU LISTE

# ## Problema 11
# L1 = list(range(0,11))
# L2 = list(range(10, 21))
# L1[::2] = L2[::2]
# print(L1)
# print(L2)
#

## Problema 12
# L = list(range(15))
# k = int(input("k="))
# L[:k]=[]
# print(L)

# del L[:k]
# print(L)

# for i in range(k):
#      L.pop(0)
# print(L)

# for i in range(k-1,-1,-1):
#      L.pop(i)
# print(L)

# ## Problema 13
# L = [4,6,7,8,0,4,3,4,0,4,6,0,2,3,0,1,3,0]
# if L.count(0)>=2:
#      p1=L.index(0)
#      p2=L.index(0, p1+1)
#      L[p1:p2+1]=[]
#
# print(L)


## Problema 2 decriptarea => TEMA
## Pb 6 si 7 => TEMA
## probleme 14 - final => TEMA
