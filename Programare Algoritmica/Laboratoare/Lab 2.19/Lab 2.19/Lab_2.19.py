n = int(input('n='))
if n == 0:
    print(1)
elif n == 1:
    print(10)
else:
    numbers = 10
    for num in range(10, 10**n):
        l = []
        x = num
        ok = True
        while x:
            for item in l:
                if item == x%10:
                    ok = False
            l.append(x%10)
            x = x//10
        if ok == True:
            numbers += 1
print(numbers)

