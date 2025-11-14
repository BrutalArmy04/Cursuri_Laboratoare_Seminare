n = int(input('n='))
x = 0
divmax = 0
for num in range(1,n+1):
    nrdiv = 0
    for div in range(1, num+1):
        if num%div == 0:
            nrdiv += 1
    if divmax<nrdiv:
        divmax = nrdiv
        x = num
    print(nrdiv)



