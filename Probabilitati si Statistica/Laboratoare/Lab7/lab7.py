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


# Definim functia de densitate a distributiei normale
def functie(x, miu, sigma2):
    # sigma2 este varianta (sigma^2)
    return 1 / (2 * np.pi * sigma2) ** 0.5 * np.exp(-(x - miu)**2 / (2 * sigma2))

def ex2_5():
    N = 10000
    
    # Parametrii lui X
    miu_x = 10
    sigma_x_patrat = 4
    sigma_x = np.sqrt(sigma_x_patrat)
    
    # Parametrii lui Y
    miu_y = 20
    sigma_y_patrat = 9
    sigma_y = np.sqrt(sigma_y_patrat)
    
    # 1. Generarea simularilor pentru X si Y
    X_sim = np.random.normal(loc=miu_x, scale=sigma_x, size=N)
    Y_sim = np.random.normal(loc=miu_y, scale=sigma_y, size=N)
    
    # 2. Calculul variabilei suma Z = X + Y
    Z_sim = X_sim + Y_sim
    
    # Parametrii teoretici pentru Z
    miu_z = miu_x + miu_y    # 30
    sigma_z_patrat = sigma_x_patrat + sigma_y_patrat  # 13
    sigma_z = np.sqrt(sigma_z_patrat)
    
    # 3. Realizarea Histogramei
    _, ax = plt.subplots(figsize=(10, 6))
    
    # Afisam histograma variabilei Z
    ax.hist(Z_sim, bins=50, density=True, color="blue", alpha=0.6, label='Simulare $X+Y$')
    
    # 4. Suprapunerea Graficului Functiei de Densitate
    
    # Generam puncte pentru graficul functiei de densitate N(30, 13)
    # Limitele sunt alese in jurul mediei Z (miu_z) ± 4 deviatia standard Z (sigma_z)
    v_x = np.linspace(miu_z - 4 * sigma_z, miu_z + 4 * sigma_z, 200)
    v_y = functie(v_x, miu_z, sigma_z_patrat)
    
    # Desenam curba de densitate teoretica
    ax.plot(v_x, v_y, color="red", linewidth=2, label=f'Densitate Normală $\mathcal{{N}}({miu_z}, {sigma_z_patrat})$')
    
    ax.set_title('Histograma sumei a două variabile Normale independente')
    ax.set_xlabel('Valoare Z = X + Y')
    ax.set_ylabel('Densitate')
    ax.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


#ex2_5()


# Functia de densitate a distributiei normale (reutilizata)
# def functie(x, miu, sigma2): ...

def ex2_6():
    N = 10000
    
    # Parametrii distributiei Normale pe care o tintim
    miu = 30
    sigma = 40
    sigma_patrat = sigma**2 # 1600
    
    # 1. Generarea a N variabile Uniforme U1 si U2
    U1 = np.random.random(size=N)
    U2 = np.random.random(size=N)
    
    # 2. Aplicarea formulei Box-Muller (forma polara - transformata)
    # NOTA: Folosim ln(U1) in formula corecta, nu cea din PDF-ul original
    
    try:
        # np.log este logaritm natural (ln)
        X_box_muller = miu + np.sqrt(-2 * sigma_patrat * np.log(U1)) * np.cos(2 * np.pi * U2)
    except FloatingPointError:
        # Aceasta eroare ar putea aparea daca un U1 este 0, caz in care ln(0) este infinit.
        # Desi putin probabil cu np.random.random, este o buna practica sa o gestionam.
        print("Eroare de calcul Box-Muller (posibil ln(0)).")
        return
        
    # 3. Realizarea Histogramei
    _, ax = plt.subplots(figsize=(10, 6))
    
    ax.hist(X_box_muller, bins=50, density=True, color="green", alpha=0.6, label='Simulare Box-Muller')
    
    # 4. Suprapunerea Graficului Functiei de Densitate
    
    # Generam puncte pentru graficul functiei de densitate N(30, 1600)
    v_x = np.linspace(miu - 4 * sigma, miu + 4 * sigma, 200)
    v_y = functie(v_x, miu, sigma_patrat)
    
    # Desenam curba de densitate teoretica
    ax.plot(v_x, v_y, color="red", linewidth=2, label=f'Densitate Normală $\mathcal{{N}}({miu}, {sigma_patrat})$')
    
    ax.set_title(f'Histograma generată prin Metoda Box-Muller (N={N})')
    ax.set_xlabel('Valoare X')
    ax.set_ylabel('Densitate')
    ax.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    
# Apelul functiei ex2_6()

#ex2_6()


##############################################################

#Rezolvarea oficiala


import numpy as np
import matplotlib.pyplot as plt

EXERCISE=2



if EXERCISE==1:
    SUBPUNCT=6

    lam=20

    f=lambda t: lam*np.exp(-t*lam)

    if SUBPUNCT==1:

        p=1/180
        n=3600


        N=100000

        ore_pana_la_mesaj=[]

        cnt_mai_putin_10_min=0

        cnt_mai_mult_20_min=0

        for _ in range(N):
            cnt_secunde=1

            while(True):
                if np.random.random()<p:
                    break
                else:
                    cnt_secunde+=1

            ore_pana_la_mesaj.append(cnt_secunde/3600)

            if cnt_secunde<=60:
                cnt_mai_putin_10_min+=1

            elif cnt_secunde>=5*60:
                cnt_mai_mult_20_min+=1

        print('Probabilitatea sa primesc mesaj in primele 10 min',cnt_mai_putin_10_min/N)
        print('Probabilitatea sa primesc mesaj dupa mai mult de 20 min',cnt_mai_mult_20_min/N)

        print('Timpul mediu până la mesaj (minute)',np.average(ore_pana_la_mesaj)*60)

        fig,ax=plt.subplots()
        ax.hist(ore_pana_la_mesaj,bins=100,density=True)

        v_x=np.linspace(0,0.5,100)
        v_y=f(v_x)

        plt.plot(v_x,v_y)
        plt.show()

    if SUBPUNCT==4:
        N=10000

        ore_pana_la_mesaj=[]

        for _ in range(N):
            u=np.random.random()

            ore_pana_la_mesaj.append(-np.log(1-u)/lam)

        fig,ax=plt.subplots()
        ax.hist(ore_pana_la_mesaj,bins=100,density=True)

        v_x=np.linspace(0,0.5,100)
        v_y=f(v_x)

        plt.plot(v_x,v_y)

        plt.show()

    if SUBPUNCT==6:
        N=100000

        ore_pana_la_mesaj=[]
        cnt_astept_mai_mult_de_5_min=0
        cnt_a_venit_dupa_mai_putin_1_min=0

        for _ in range(N):
            u=np.random.random()

            x=-np.log(1-u)/lam

            if x>=5/60:
                cnt_astept_mai_mult_de_5_min+=1

                if x<=6/60:
                    cnt_a_venit_dupa_mai_putin_1_min+=1


        print('Probabilitatea ca, daca nu a venit mesaj de 5 minute, sa vina mesaj intr-un minut:',cnt_a_venit_dupa_mai_putin_1_min/cnt_astept_mai_mult_de_5_min)

if EXERCISE==2:
    SUBPUNCT=1

    if SUBPUNCT==1:
        N=50000

        VARIANTA=['INCET','RAPID'][1]

        nr_pasi=3600

        mu=0
        sigma=np.sqrt(nr_pasi)

        f=lambda x: np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)

        if VARIANTA=='INCET':

            pozitii_finale=[]

            cnt_favorabile=0

            for _ in range(N):
                poz=0
                for pas in range(nr_pasi):
                    directia=-1 if np.random.random() <0.5 else 1
                    poz+=directia

                pozitii_finale.append(poz)
                if np.abs(poz)<25:
                    cnt_favorabile+=1

        if VARIANTA=='RAPID':

            miscari=np.random.choice([-1,1],replace=True,size=(N,nr_pasi))

            pozitii_finale=np.sum(miscari,axis=1)

            cnt_favorabile=np.sum(np.abs(pozitii_finale)<25)


        print('Probabilitatea să am distanța mai mică de 25 de metri',cnt_favorabile/N)

        fig,ax=plt.subplots()

        ax.hist(pozitii_finale,density=True,bins=range(min(pozitii_finale),max(pozitii_finale)+2,2)) #punem bin-urile din 2 in 2 pentru ca pozitia betivului va avea mereu paritatea numarului de pasi
        v_x=np.linspace(-200,200,1000)
        v_y=f(v_x)

        plt.plot(v_x,v_y)

        plt.show()

    if SUBPUNCT==3:

        mu=2
        sigma=3

        f=lambda x: np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)

        N=100000

        normal_vector=np.random.normal(loc=mu,scale=sigma,size=N)

        fig,ax=plt.subplots()

        ax.hist(normal_vector,bins=100,density=True)

        v_x=np.linspace(-10,15,100)
        v_y=f(v_x)

        plt.plot(v_x,v_y)

        plt.show()

    if SUBPUNCT==5:

        mu=2
        sigma=3

        nu=4
        tau=2

        f=lambda x: np.exp(-(x-mu-nu)**2/(2*(sigma**2+tau**2)))/(np.sqrt(2*np.pi*(sigma**2+tau**2)))

        N=100000

        X=np.random.normal(loc=mu,scale=sigma,size=N)

        Y=np.random.normal(loc=nu,scale=tau,size=N)

        fig,ax=plt.subplots()

        ax.hist(X+Y,bins=100,density=True)

        v_x=np.linspace(-10,15,100)
        v_y=f(v_x)

        plt.plot(v_x,v_y)

        plt.show()


    if SUBPUNCT==6:

        N=100000

        mu=2
        sigma=3

        f=lambda x: np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)

        results=[]

        for _ in range(N):
            u1=np.random.random()
            u2=np.random.random()

            x= mu+ np.sqrt(-2*sigma**2*np.log(u1))*np.cos(2*np.pi*u2)

            results.append(x)

        fig,ax=plt.subplots()

        ax.hist(results,bins=200,density=True)

        v_x=np.linspace(-10,15,100)
        v_y=f(v_x)

        plt.plot(v_x,v_y)

        plt.show()

