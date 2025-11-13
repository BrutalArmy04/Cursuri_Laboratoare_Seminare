L = [4, 6, 6, 3, 2, 6, 6, 2, 7, 4, 2, 2]
k = 3
start = final = 0
s = sum(L) + 1
for i in range (len(L)-k+1):
    suma = sum(L[i:i+k])
    if suma<s:
        s = suma
        start = i
        final = i+k
L[start:final] = []
#print(L)
Lelim = list(set(L))
#print(Lelim)
M = [-2, -5, 3, 6, -3, 6, 7]

M = [M[i] if M[i]>=0 else M[i]*10 for i in range(len(M))]
print(M)