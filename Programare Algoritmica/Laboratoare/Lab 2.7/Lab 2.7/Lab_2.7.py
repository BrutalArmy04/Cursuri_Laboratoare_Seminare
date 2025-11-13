n = int(input('n= '))
min = None
nrap = 0
while n:
    x = int(input('x='))
    if min==None:
        min = x
        nrap = 1
    elif min==x:
        nrap +=1
    elif x<min:
        min=x
        nrap = 1
    n -=1
print(min, nrap)

