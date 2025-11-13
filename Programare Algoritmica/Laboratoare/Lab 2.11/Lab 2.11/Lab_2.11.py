n = int(input('n='))
l = []
for i in range(n):
    x = int(input(f'l[{i}]='))
    l.append(x)
i = 0
while (l[i]<l[i+1]):
    i += 1
peakup = l[i]
i = n-1
while (l[i-1]>l[i]):
    i -= 1
peakdown = l[i]
if peakup == peakdown:
    print('Vectorul este creasta')
else:
    print('Vectorul nu este creasta')