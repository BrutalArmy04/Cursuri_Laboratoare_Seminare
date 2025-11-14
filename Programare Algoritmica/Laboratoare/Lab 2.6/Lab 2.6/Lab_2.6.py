n = int(input("n= "))
maxim = 0
minim = 0
nr0 = 0
ok = True
for num in range(9, -1, -1):
    cn = n
    ap = 0
    while cn:
        if num==cn%10:
            ap +=1
        cn //= 10
    while ap:
        ap -=1
        maxim = maxim * 10 + num
cn = n
while cn:
    if cn%10 == 0:
        nr0 +=1
    cn //=10
for num in range(1, 10):
    cn = n
    ap = 0
    while cn:
        if num==cn%10:
            ap +=1
        cn //= 10
    if ap!=0 and minim==0:
        ap -= 1
        minim = num
        while nr0:
            minim = minim*10
            nr0-=1
    while ap:
        ap -=1
        minim = minim * 10 + num
print(minim, maxim)



