L = [5,0,7,5,3,2,10,3, 0, 3, 0, 5]
if L.count(0)>=2:
    p1=L.index(0)
    p2=L.index(0, p1+1)
    L[p1:p2+1] = []
print(L)
