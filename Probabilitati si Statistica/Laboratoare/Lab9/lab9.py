# avem o functie g pe R
# omega e pe intervalul [a, b]
# X ~ f
# f > 0 pe omega si f = 0 pe R minus omega
# I = integrala(g(x)dx)
# E [h(x)] = integrala (h(x) * f(x)dx)
# pt 0....1/2.....1, unde pe grafic 1/2 se intersecteaza cu 2/3
# E[h(x)] = integrala 0_1/2(h(x) * 2/3 dx) + integrala 1/2_1(h(x)*4/3 dx)
# integrala pe omega (g(x)dx = E[g(x)/f(x)])
# care este aprox (g(x1)/f(x1) + g(x2)/f(x2)+...+g(xn)/f(xn))/n

# integrala a_b (g(x)dx ~ (b-a)/N * suma i = 1_N g(x:...)  )

# g:[a,b] -> R
# x1, x2, ..., xn ~ f independente
# x ~ Unif ([a, b])                 f = 1/(b-a) * lambda [a, b]
# P (X apartine [c, d]) = (c - d)/ (b-a) = integrala c_d (1/(b-a)dx)

import numpy as np
#ex1\

def g(x):
    return x**3/3


def ex1():
    a = 1
    b = 5
    N = 10000
    v = []
    for _ in range (N):
        c = np.random.random() * (b-a)
        v.append(g(c))
    print((b-a)/N * sum(v))

ex1()


# un singur hint la 2
# omega poate fi incarcat intr-un patrat
# integrala omega g = integrala patrat g1 unde g1 = g(x) cand x este in omega si 0 altfel


################################################

# Rezolvarea oficiala

import numpy as np
import matplotlib.pyplot as plt



SUBPUNCTUL=3

if SUBPUNCTUL==1:
    #Spre exemplu,
    g=lambda x: x**2+2
    a=1
    b=2
    int_teoretic=13/3
    N=10000

    X=a+np.random.random(size=N)*(b-a)

    Z=g(X)

    partials=(b-a)*np.cumsum(Z)/np.array(range(1,N+1))

    fig,ax=plt.subplots()
    ax.plot(range(1,N+1),partials-int_teoretic)
    ax.plot([1,N],[0,0])
    plt.show()


if SUBPUNCTUL==2:
    R=4
    rho = lambda theta: 3+np.cos(4*theta)
    def is_in_omega(x,y):
        r=np.linalg.norm([x,y])
        th=np.arctan2(y,x)
        return r<=rho(th)
    def g(x,y):
        if not is_in_omega(x,y):
            return 0
        return x**2-3*y**3

    N=5000000

    X=-R+np.random.random(size=N)*2*R
    Y=-R+np.random.random(size=N)*2*R

    Z=[g(x,y) for (x,y) in zip(X,Y)]

    integrala=4*R**2*sum(Z)/N

    print(integrala)

if SUBPUNCTUL==3:
    g = lambda x: 1/(x**2+1)

    int_teoretic=np.pi

    sigma=20

    f=lambda x: 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-x**2/(2*sigma**2))

    N=100000


    X=np.random.normal(scale=sigma,size=N)

    print(X)

    Z=g(X)/f(X)

    print(Z)


    partials=np.cumsum(Z)/np.array(range(1,N+1))

    fig,ax=plt.subplots()
    ax.plot(range(1,N+1),partials-int_teoretic)
    ax.plot([1,N],[0,0])
    plt.show()



