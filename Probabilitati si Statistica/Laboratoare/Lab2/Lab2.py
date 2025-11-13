#ne simtim ca la cazino

import numpy as np
import matplotlib.pyplot as plt

# ex 1


#nrc = 0
#k = 10000
#fig, ax = plt.subplots()
#proc = 0.5 # 0.7 pt necinstit, 0.5 pt cinstit
#ax.plot([0, k], [proc, proc], color = 'r')




#prob_part = []
#for num in range(k):
#    c = np.random.random()
#    if c < proc:    
#        nrc+=1
#    prob_part.append(nrc/(num+1))

#ax.plot(range(1, k+1), prob_part, color = 'b')

#print(f"Probabilitatea sa pice cap = {nrc/10000}")
#plt.show()

#ex 2 de revizuit
s = 'cccccccccc'
c=0
print('ccc' in s)
while s:
    if 'ccc' in s:
        c+=1
    s = s[1:]
print(c)


import numpy as np
prob3cap = 0
prob4larand = 0
prob4cp = 0
for num in range(1000):
    nr3c = 0
    cpcp = 0
    nr4cp = 0
    s = ''
    for i in range(20):
        c = np.random.random()
        if c < 0.5:
            s+='c'
        else:
            s+='v'
    while s:
        if 'ccc' in s:
            nr3c+=1
        if 'cpcpcpcp' in s:
            cpcp+=1
        if ('cccc' in s) or ('pppp' in s):
            nr4cp+=1
        s = s[1:] 
    prob3cap+=nr3c
    prob4cp+=cpcp
    prob4larand+=nr4cp

print(prob3cap/20000, prob4larand/20000, prob4cp/2000)


    
    



for num in range(1000):
    nr3c = 0
    cpcp = 1
    nr4p = 0
    nr4c = 0
    vect = []
    c = np.random.random()
    if c<0.5:
        last = 'c'
        print('c', end=" ")
        nr3c+=1
        nr4c+=1
    else:
        last = 'p'
        print('p', end=" ")
        nr4p+=1
    
    for i in range(19):
        c = np.random.random()
        if c<0.5: #e cap
            print('c', end=" ")
            nr4p = 1
            nr3c+=1
            nr4c+=1
            if last == 'c':
                cpcp = 1
   
            else:
                cpcp+=1
                last = 'p'

        else:   #e pajura
            print('p', end=" ")
            nr4p+=1
            nr3c=1
            nr4c=1
            if last == 'c':
                cpcp+=1
                last = 'p'
            else:
                cpcp=1
        if nr3c >=3:
            prob3cap+=1
        if nr4c >=4 or nr4p >=4:
            prob4larand+=1
        if cpcp >=8:
            prob4cp+=1
    print(prob3cap, prob4cp, prob4larand)
    print()

print(prob3cap/20000, prob4cp/20000, prob4larand/20000)





