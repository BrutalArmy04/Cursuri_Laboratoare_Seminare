#Prob 3

# f = open("input.txt", 'r')
# n = int(f.readline())
# L = [int(x) for x in f.readline().split()]
# suma = int(f.readline())
# f.close()
# print(L, suma)

# d = {}
# for x in L:
#     for s in list(d):
#         if x + s not in d and x + s <= suma:
#             d[x + s] = x
#     if x not in d and x <= suma:
#         d[x] = x

# print(d)

# sol = []
# s = suma
# while s != d[s]:
#     sol.append(d[s])
#     s = d[s]

# print(sol)

# # afisare

# Prob 4

f = open('input.txt', 'r')
n = int(f.readline())
L = [cub.strip().split() for cub in f]
f.close()

for i in range(len(L)):
    L[i][0] = int(L[i][0])

L.sort()
print(L)
hMax = [cub[0] for cub in L] #inaltimea max a turnului care se termina cu cubul i
pred = [-1]*len(L) # poz cubului anterior in turn cubului i
nrTurnuri = [1]=len(L) # nr turnuri de inaltime maxima care se termina cu cubul i

for i in range(1, len(L)):
    for j in range(i):
        if L[i][1] != L[j][1] and L[i][0] > L[j][0]:
            if hMax[i] < hMax[j] + L[i][0]:
                hMax[i] = hMax[j] + L[i][0]
                pred[i] = j
                nrTururi
    
