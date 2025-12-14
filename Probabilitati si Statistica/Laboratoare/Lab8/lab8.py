import numpy as np
import matplotlib.pyplot as plt

# ex 2

def f(x):
    return (1/np.sqrt(np.pi * 2)) * np.exp(-(x**2/2))


def ex2_3():
    k = 10000
    N = 50000
    p = 0.3
    n = 10
    Ex = p
    Var = p * (1 - p)
    lamba = 20
    empiric = 0
    X = np.random.choice([0, 1], size=N, p=[1 - p, p])
    S = np.cumsum(X)
    N_vector = np.arange(1, N + 1)

    S = np.cumsum(X)
    N_vector = np.arange(1, N + 1)

    X_bar = S / N_vector
    Var_N = X_bar - X_bar**2
    eroare_medie = np.abs(X_bar - p)
    eroare_varianta = np.abs(Var_N - Var)
    print(eroare_medie, eroare_varianta)


    valori = []

    for _ in range(k):
        X = np.random.choice([0, 1], p = [p, 1 - p], size = N)
        valoare = np.sqrt(N)/np.sqrt(Var) * (np.average(X) - p)
        valori.append(valoare)
    plt.hist(valori, bins = 200, density=True)
    vx = np.linspace(-4, 4, 200)
    vy = [f(x) for x in vx]
    _, ax2 = plt.subplots()
    ax2.plot(vx, vy, color='red')
    ax2.hist(X, bins=100, density=True, alpha=0.7, color='blue', edgecolor='black')



    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(N_vector, eroare_medie, label=r'$|\overline{X}_N - \mu|$', color='blue')

    plt.subplot(1, 2, 2)
    plt.plot(N_vector, eroare_varianta, label=r'$|Var_N - Var(X)|$', color='red')

    plt.show()

ex2_3()

