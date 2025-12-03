#Ex 1
import numpy as np
import matplotlib.pyplot as plt
from math import factorial


def ex1_1_2_3_6():

    n = 10000
    l = 20  #lambda
    ora = 3600
    p = l/ora
    fig, ax1 = plt.subplots()
    sec_mes = []
    minut = [] * 60
    nu_cinci_minut = 0
    am_primit_in_6 = 0
    prim_minut = 0
    for _ in range(n):
        for i in range(ora):     
            c = np.random.random()
            if c < p:
                sec_mes.append(i)
                if i < 60:
                    prim_minut += 1
                elif i >= 300:
                    nu_cinci_minut += 1
                    if i < 360:
                        am_primit_in_6 += 1
    minut.append(i//60)
    print(prim_minut/n)
    print(nu_cinci_minut/n)
    print(np.average(minut))
    print(am_primit_in_6/n)
    #ax1.hist(sec_mes, bins=range(0, ora+2), density=True, alpha=0.7, color='blue', edgecolor='black')
    #ax1.hist(sec_mes, bins=100, density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.show()

#ex1_1_2_3_6()


# ne intrreseaza prob ca x sa apartina intervalul [a,b]
# P(x <= t)  = lim(n->oo) P(Xn <= t)   Xn~Geom(l/n) (l este lambda, cea din enunt)  
#  = lim(n->oo) suma(k = 1, parte intreaga tn) (l/n)*(1 - l/n)^(k-1) = 1 - lim(n->oo) (1 - l/n)^parte intreaga(tn)
# = 1 - e^(-lt)



# F(t) = P(x <= t) = 1 - e^(-lt)  pentru t >= 0
# F(t) = 0 pentru t < 0
# U = np.random.random()
# P(U <= r) = r, pt oricare r din [0,1]
# Vreau X var aleatiare astfel incat P(X <= t) = F(t)
# P (X <= F^(-1)(r)) = r, oricare r din [0,1]
# P(F(X) <= r) = r, oricare r din [0,1]
# F(X) are aceeasi distributie ca U, adica X = F^(-1)(U) atunci X ~ Exp(l)

def f(t, l=20):
    return l * np.exp(-l * t) if t >= 0 else 0
def F(u, l=20):
    return - (1 / l) * np.log(1 - u)

def ex1_4_5():
    n = 10000
    l = 20
    v = []
    for _ in range(n):
        u = np.random.random()
        x = F(u, l)  
        v.append(x)
    _, ax2 = plt.subplots()
    v_x = np.linspace(0, 5, 200)
    v_y = np.array([f(t, l) for t in v_x])
    ax2.plot(v_x, v_y, color='red')
    ax2.hist(v, bins=100, density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.show()

    # la 5 f(t) = l * e^(-l * t) pt t >= 0

#ex1_4_5()

#ex 2

def f2(x):
    # Correct Gaussian PDF for random walk:
    # μ = 0, σ² = 3600, σ = 60
    return 1/(2*3600*np.pi)**0.5 * np.exp(-x**2/(2*3600))
def ex2_1_2():
    n = 10000
    nrbune = 0
    fig, ax = plt.subplots()
    ora = 3600
    v = []
    for _ in range(n):
          dist = 0
          for _ in range(ora):
              c = np.random.random()
              if (c < 0.5):
                  dist -= 1
              else:
                  dist += 1
          v.append(dist)
          if abs(dist) < 25:
              nrbune += 1
    ax.hist(v, bins = range(min(v), max(v) + 2, 2), density=True, color="blue")
    v_x = np.linspace(min(v), max(v), 200)
    v_y = np.array([f2(x) for x in v_x])
    ax.plot(v_x, v_y, color = "red")
   
    print(nrbune/n)
    plt.show()
              

ex2_1_2()

def functie(x, miu, sigma):
    # Fixed version of your original
    return 1/(2 * np.pi * sigma**2) ** 0.5 * np.exp(-(x - miu)**2/(2 * sigma**2))


def ex2_3_4():
    miu = 30 #np.random.randint(1000)
    sigma = 40 #np.random.randint(1000) 
    v = np.random.normal(miu, sigma, size = 10000)
    _, ax = plt.subplots()
    ax.hist(v, bins = range(round(min(v)), round(max(v)) + 2), density=True, color="blue")
    v_x = np.linspace(miu - 4 * sigma, miu + 4 * sigma, 200)
    v_y = np.array([functie(x, miu, sigma) for x in v_x])
    ax.plot(v_x, v_y, color = "red")
    plt.show()

#ex2_3_4()

def ex2_5_6():
    pass


ex2_5_6()