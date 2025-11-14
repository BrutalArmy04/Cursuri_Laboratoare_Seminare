n = int(input('n= '))
L = [x if x%2==1 else -x for x in range(1, n+1)]
print(L)