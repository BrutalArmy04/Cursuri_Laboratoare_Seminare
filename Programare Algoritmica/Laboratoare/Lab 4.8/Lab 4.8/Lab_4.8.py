L = [2, 4, 1, 7, 5, 1, 8, 10]
rez = [L[i] for i in range (len(L)) if L[i]%2==i%2]
#print(rez)
wo = [nr for poz, nr in enumerate(L) if poz%2 == nr%2]
print(wo)