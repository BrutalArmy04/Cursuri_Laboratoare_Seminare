import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**2

def aria_subgraf1(x):
    return (x**3)/3

def zar(c):
    for i in range (1, 7):
        if c<i:
            return i
        
def f3(x):
    return x**2+1   


subiect = 1


if subiect == 1:    #Problema 1

    subpunct = 2

    if subpunct == 1:   #Subp1

        print(5**5/6**6)

    elif subpunct == 2: #Subp2

        n = 10000
        nr_duble = 0
        val = []
        dist = []
        fig, ax = plt.subplots()
        ax.set_aspect(1)
        ax.set_xlim(0, 1)

        for i in range (1,n+1):

            zar1 = np.random.random() * 6
            zar2 = np.random.random() * 6

            if zar(zar1) == zar(zar2):
                nr_duble += 1

            val.append(nr_duble/(i))

        for i in range(1, n+1):
            dist.append(i/n)

        ax.plot(dist, val)
        print(nr_duble/n)  
        plt.show()

    else:   #Subp3

        n = 10000
        m = 30
        elem = 3
        probsuma3 = 0

        for i in range(n): 
            v = [0] * (m+1)

            for j in range(m):
                zar1 = np.random.random() * 6
                zar2 = np.random.random() * 6
                v[m] = zar(zar1) + zar(zar2)

            if elem in v:
                probsuma3 += 1

        print(probsuma3/n)
                    
else:   #Problema 2

    subpunct = 2

    if subpunct == 1:   #Subp1

        a = 0
        b = 2
        M = 4
        nr_puncte = 50

        for i in range(nr_puncte):
            x = np.random.random() * (b-a)
            y = f1(x)
            aria_subgraf = abs(aria_subgraf1(y) - aria_subgraf1(x))
            print(aria_subgraf)

    elif subpunct == 2: #Subp2

        a = 0
        b = 2
        M = 4
        nr_puncte = 50
        fig, ax = plt.subplots()
        ax.set_aspect(1)
        ax.set_xlim(0, f1(M))
        ax_x = []
        ax_y = []

        for i in range(nr_puncte):
            x = np.random.random() * (b-a)
            y = f1(x)
            aria_subgraf = abs(aria_subgraf1(y) - aria_subgraf1(x))
            ax_x.append(x)
            ax_y.append(aria_subgraf)

        ax.scatter(ax_x, ax_y)
        plt.show()

    else:   #Subp3

        a = -1
        b = 1
        M = 3
        n = 10000
        nrSG = 0

        for i in range(n):
            xa = np.random.random() * (b-a) + a
            xb = np.random.random() * (b-a) + a
            ya = np.random.random() * M
            yb = np.random.random() * M
            mijloc_x = (xa+xb)/2
            mijloc_y = (ya+yb)/2

            if mijloc_x <= b and a <= mijloc_x and mijloc_y >=0 and mijloc_y <= f3(mijloc_x):
                nrSG += 1

        print(nrSG/n)





