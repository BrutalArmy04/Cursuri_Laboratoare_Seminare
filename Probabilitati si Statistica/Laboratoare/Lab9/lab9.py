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