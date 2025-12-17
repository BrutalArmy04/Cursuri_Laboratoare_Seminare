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




########################################################################

#Rezolvarea oficiala


import numpy as np
import matplotlib.pyplot as plt

EXERCISE=3

if EXERCISE==1: #datul cu banul
    BAN=['cinstit','masluit'][0]

    K=100000 #nr de simulari

    PLOT=True

    if BAN=='cinstit':
        p=.5 #probabilitatea sa pice Cap
    else:
        p=.7

    if not PLOT:
        Capete=0
        
        for i in range(K):
            r=np.random.random() #ranodm in [0,1)
            
            C= 1 if r<p else 0 #a picat cap?

            Capete+=C

        print('Probabilitate empirică să pice Cap este:',Capete/K)

    if PLOT:
        ProbIntermediare=[]
        Capete=0
        
        for i in range(K):
            r=np.random.random() #ranodm in [0,1)
            
            C= 1 if r<p else 0 #a picat cap?

            Capete+=C

            ProbIntermediare.append(Capete/(i+1))

        fig,ax=plt.subplots()
        ax.plot(range(1,K+1),ProbIntermediare,color="b")
        ax.plot([1,K+1],[p,p],color="r") #probabilitatea reala
        plt.show()


if EXERCISE==2: #Mai multe aruncari cu banul
    N=20 #nr aruncari cu banul
    K=10000
    
    CHECK=['CCC','CPCPCPCP','CCCC/PPPP','CCCCC/PPPPP'][0]

    if CHECK=='CCC':
        MASK=[np.array([1,1,1],dtype=int)]
    elif CHECK=='CPCPCPCP':
        MASK=[np.array([1,0,1,0,1,0,1,0],dtype=int)]
    elif CHECK=='CCCC/PPPP':
        MASK=[np.array([1,1,1,1],dtype=int),np.array([0,0,0,0],dtype=int)]
    elif CHECK=='CCCCC/PPPPP':
        MASK=[np.array([1,1,1,1,1],dtype=int),np.array([0,0,0,0,0],dtype=int)]

    Favorabile=0

    for _ in range(K):
        vec=np.zeros(N,dtype=int)
        for i in range(N):
            r=np.random.random() #ranodm in [0,1)
            
            C= 1 if r<.5 else 0 #a picat cap?
            vec[i]=C
        #alternativ
        # vec=np.random.choice([0,1],N)
        
        #print(vec)

        to_break=False #ca sa dam break la ambele for-uri
        for mask in MASK:
            for i in range(N-len(mask)):
                if (vec[i:i+len(mask)]==mask).all(): #adica avem egalitate pe fiecare element
                    Favorabile+=1
                    to_break=True
                    break
            if to_break:
                to_break=False
                break
    

    print('Probabilitatea sa apara '+CHECK+' este:',Favorabile/K)


if EXERCISE==3: #Zarurile lui Efron
    Z1=[1,4,4,4,4,4]
    Z2=[3,3,3,3,3,6]
    Z3=[2,2,2,5,5,5]

    ZARURI=[Z1,Z2,Z3]

    K=10000

    Castiguri=np.zeros(len(ZARURI),dtype=int)
    for _ in range(K):
        aruncari=[] # aici punem rezultatele aruncarilor
        for zar in ZARURI:
            sim_zar=np.random.choice(zar) #alegem o cifra de pe zar
            aruncari.append(sim_zar)

        # print(aruncari)
        zar_castigator=np.argmax(aruncari) #care e zarul cu cea mai mare aruncare?
        #print('A castigat',zar_castigator)

        Castiguri[zar_castigator]+=1

    print('Probabilitatile de castig sunt:',Castiguri/K)
        

            