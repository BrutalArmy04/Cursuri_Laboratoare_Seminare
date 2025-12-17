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

                





######################################################

#Rezolvarea oficiala

import numpy as np
import matplotlib.pyplot as plt

EXERCISE=2

if EXERCISE==1:

    NR_TESTE=1

    P_BOLNAV=1/1000

    N=int(1e7)

    cnt =0

    cnt_pozitive=0

    for _ in range(N):

        sunt_bolnav=np.random.random()<1/1000

        sunt_negativ=False

        for t in range(NR_TESTE):

            test_sensibil=np.random.random()<98/100 #am nimerit un test care recunoaste bine bolnavii?

            test_specific=np.random.random()<99/100 #am nimerit un test care recunoaste bine sanatosii?

            test_pozitiv= (sunt_bolnav and test_sensibil) or ((not sunt_bolnav) and (not test_specific))

            if not test_pozitiv:
                sunt_negativ=True


        if not sunt_negativ:
            cnt_pozitive+=1

            if sunt_bolnav:
                cnt+=1


    print(f'Probabilitatea să fiu bolnav cu {NR_TESTE} teste pozitive este:',cnt/cnt_pozitive)


if EXERCISE==2:

    SCHIMB=False

    N=10000

    cnt=0

    #presupun tot timpul ca masina se afla pe pozitia 2 in lista [0,1,2])

    for _ in range(N):

        alegerea=np.random.choice([0,1,2])

        if alegerea==0:
            deschide=1
        elif alegerea==1:
            deschide=0
        else:
            deschide=np.random.choice([0,1])

        if not SCHIMB:
            final=alegerea

        else:
            for i in [0,1,2]:
                if i != alegerea and i!=deschide:
                    final=i
                    break

        castig=False
        if final==2:
            cnt+=1
            castig=True

        # print(f'Initial aleg {alegerea}, apoi deschide {deschide}. Final: {final}. '+ ('Am castigat! :)' if castig else 'Am pierdut:('))

    print('')
    print('Probabilitatea de castig:', cnt/N)