s = input('cuvant=')
i = 0
while len(s)-2*i:
    print((s[i:len(s)-i]).center(10))
    i+=1
