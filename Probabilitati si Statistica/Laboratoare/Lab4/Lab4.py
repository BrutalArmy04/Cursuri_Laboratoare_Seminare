#Ex 1

#print(98/(98+999)*100)
import numpy as np
n = 1000000
sensibilitate = 98/100
specificatie = 99/100
incidenta = 1/1000
c_poz = 0
b = 0
# bolnav = sunt in incidenta si sensibil
# sanatos = nu sunt in incidenta si nu sunt specific
for _ in range(n):
    bolnav = np.random.random()
    sens = np.random.random()
    spec = np.random.random()
    sens2 = np.random.random()
    spec2 = np.random.random()
    if (bolnav < incidenta and sens < sensibilitate) or (not(bolnav < incidenta) and not(spec < specificatie)):
        if (bolnav < incidenta and sens2 < sensibilitate) or (not(bolnav < incidenta) and not(spec2 < specificatie)):
            c_poz+=1
            if bolnav < incidenta:
                b+=1
print((b/c_poz)*100)

#Ex 2

n = 100000

count_ferrari = 0
switch = 0
for _ in range(n):
    first = np.random.random()
    door1 = first < (1/3)
    door2 = 1/3 <= first and first <= (2/3)
    door3 = 2/3 < first and first <= 1
    pick = np.random.random()

    if pick < 1/3:
        if door1 == 1 * switch:
            #print("ferrari")
            count_ferrari += 1
        #else:
            #print("logan")
    elif pick > 2/3:
        if door3 == 1  * switch:
            #print("ferrari")
            count_ferrari += 1
        #else:
            #print("logan")
    elif door2 == 1 * switch:
        #print("ferrari")
        count_ferrari += 1
    #else:
        #print("logan")

print(count_ferrari/n)

                


