import numpy as np
import matplotlib.pyplot as plt

#1

def zar():
    c = np.random.random() * 6
    for i in range(1, 7):
        if c<=i:
            return i

def ex1():
    s = 8
    v = 2
    n = 1000000
    nr_aruncari_bune = 0
    nr_correct_v = 0
    for i in range(n):
        zar1 = zar()
        zar2 = zar()
        if zar1 == v and (s-zar2)<=6:
            nr_aruncari_bune += 1
            if zar2 == (s - v):
                nr_correct_v += 1

    print(nr_correct_v/nr_aruncari_bune)
        

#2

def ex2():
    zar1 = 1
    s = 8
    nr_corecte = 0
    n = 10000000
    for i in range(n):
        zar2 = zar()
        if (zar1+zar2) == s:
            nr_corecte += 1
    print(nr_corecte/n)
    nr_corecte = 0
    for i in range(n):
        zar3 = zar() + zar()
        if (zar3-zar1) == 6:
            nr_corecte += 1
    print(nr_corecte/n)
    nr_corecte = 0
    for i in range(n):
        zar1 = zar()
        zar2 = zar()
        zar3 = zar() + zar()
        if (zar1 == 1 and zar2 == 5 and zar3 == 8):
            nr_corecte += 1
    print(nr_corecte/n)


#3

def ex3():
    procentaj = 9/100
    cinci_zile = 0
    zero_zile = 0
    n = 1000000
    v = np.zeros(31)
    for i in range(n):
        nr_intalniri = 0
        for _ in range(30):
            c = np.random.random()
            if c < procentaj:
                nr_intalniri += 1
        if nr_intalniri == 0:
            zero_zile += 1
        if nr_intalniri == 5:
            cinci_zile += 1
        v[nr_intalniri] += 1
    fig, ax = plt.subplots()
    ax.bar(range(31), v/n)
    plt.show()
    print(f'De 0 ori: {zero_zile}; de 5 ori: {cinci_zile}.\n Prob 0: {zero_zile/n}. Prob 5: {cinci_zile/n}.')


ex3()




