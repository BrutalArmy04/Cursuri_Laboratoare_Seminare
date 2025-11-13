#Pb1 - O(n)

f = open("cuvinte.in")
L = [i for i in f.readline().split() ]

mare = [0] * len(L)

d = {}

for i in range(len(L)):
    x = L[i]
    if x[:2] not in d:
        mare[i] = 1
        d[x[-2:]] = i
    else:
        mare[i] = 1 + mare[d[x[:2]]]
        if mare[i] > mare[d.get(x[-2:],-1) ]:
            d[x[-2:]] = i


k = mare.index(max(mare))

## ar trebui afisate in ordine inversa cuvintele...
while True:
    print(L[k],end=" ")
    if mare[k] == 1:
        break
    k = d[L[k][:2]]