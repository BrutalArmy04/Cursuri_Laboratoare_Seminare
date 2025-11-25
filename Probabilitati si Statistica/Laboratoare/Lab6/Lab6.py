# s-a luat curentul cand lucram pe calculatoarele din laborator

#Ex 3 din lab 5

# import numpy as np
# import matplotlib.pyplot as plt

# def binomial_simulation(n=30, p=0.09, num_simulari=100000):
#     """Simulează distribuția binomială pentru întâlniri în metrou"""
    
#     # 1. Simulări Monte Carlo
#     zile_cu_intalniri = np.zeros(num_simulari, dtype=int)
    
#     for i in range(num_simulari):
#         # Generăm 30 de zile independente
#         zile = np.random.random(n)
#         # Numărăm câte zile au avut întâlnire (număr < p)
#         zile_cu_intalniri[i] = np.sum(zile < p)
    
#     # Probabilități
#     prob_0 = np.mean(zile_cu_intalniri == 0)
#     prob_5 = np.mean(zile_cu_intalniri == 5)
    
#     print(f"#1 Probabilitatea de a nu mă întâlni cu nimeni: {prob_0:.4f}")
#     print(f"   Probabilitatea de a mă întâlni în exact 5 zile: {prob_5:.4f}")
    
#     if prob_0 > prob_5:
#         print("   → Este mai probabil să nu mă întâlnesc cu nimeni")
#     else:
#         print("   → Este mai probabil să mă întâlnesc în exact 5 zile")
    
#     # 2. Histograma
#     plt.figure(figsize=(12, 4))
    
#     plt.subplot(1, 2, 1)
#     valori, frecvente = np.unique(zile_cu_intalniri, return_counts=True)
#     plt.bar(valori, frecvente/num_simulari, alpha=0.7, color='blue', label='Simulare')
#     plt.xlabel('Număr de zile cu întâlniri')
#     plt.ylabel('Probabilitate')
#     plt.title('Distribuția numărului de zile cu întâlniri\n(Simulare Monte Carlo)')
#     plt.grid(True, alpha=0.3)
    
#     # 3. Distribuția binomială teoretică
#     k_values = np.arange(0, n+1)
#     prob_binomial = np.zeros(n+1)
    
#     # Calcul manual al coeficienților binomiali
#     for k in k_values:
#         # C(n,k) = n! / (k!(n-k)!)
#         # Folosim logaritmi pentru a evita overflow
#         log_comb = (np.sum(np.log(np.arange(1, n+1))) - 
#                    np.sum(np.log(np.arange(1, k+1))) - 
#                    np.sum(np.log(np.arange(1, n-k+1))))     
#         # log_comb = log(n!) - log(k!) - log((n-k)!)
#         comb = np.exp(log_comb)
#         # Probabilitatea binomială 
#         prob_binomial[k] = comb * (p**k) * ((1-p)**(n-k))
    
#     # Simulare folosind metoda intervalelor
#     intervale = np.cumsum(prob_binomial)
#     simulari_interval = np.zeros(num_simulari, dtype=int) # stocăm rezultatele simulării
    
#     for i in range(num_simulari):   
#         u = np.random.random()
#         # Găsim intervalul în care cade u
#         for k in range(n+1):
#             if u < intervale[k]:
#                 simulari_interval[i] = k
#                 break
    
#     plt.subplot(1, 2, 2)
#     valori_teor, frecvente_teor = np.unique(simulari_interval, return_counts=True)  # numărăm frecvențele 
#     plt.bar(valori_teor, frecvente_teor/num_simulari, alpha=0.7, color='red', label='Binomial teoretic')
#     plt.xlabel('Număr de zile cu întâlniri')
#     plt.ylabel('Probabilitate')
#     plt.title('Distribuția binomială teoretică\n(Metoda intervalelor)')
#     plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.show()
    
#     # Afișăm primele 10 probabilități
#     print(f"\n#3 Primele 10 valori ale distribuției binomiale:")
#     for k in range(11):
#         print(f"   P(X = {k}) = {prob_binomial[k]:.6f}")

# binomial_simulation()

# #Ex1
# # Set seed pentru rezultate reproducible
# np.random.seed(42)

# print("=== EX#1 (Distribuția Geometrică) ===\n")

# def simulare_geometrica(p=0.09, num_simulari=100000):
#     """Simulează distribuția geometrică pentru prima întâlnire în metrou"""
    
#     # 1. Metoda Monte Carlo directă
#     print("#1 Probabilitatea să văd prima persoană peste 7 zile:")
    
#     zile_pana_la_intalnire = np.zeros(num_simulari, dtype=int)
    
#     for i in range(num_simulari):
#         zile = 0
#         while True:
#             zile += 1
#             # Generăm o zi: dacă numărul aleator < p, avem întâlnire
#             if np.random.random() < p:
#                 zile_pana_la_intalnire[i] = zile
#                 break
    
#     # Probabilitatea să văd prima persoană peste 7 zile
#     # Adică prima întâlnire este la ziua 8 sau mai târziu
#     prob_peste_7 = np.mean(zile_pana_la_intalnire > 7)
#     print(f"P(X > 7) = {prob_peste_7:.4f}")
    
#     # Verificare teoretică: P(X > k) = (1-p)^k
#     prob_teoretica = (1 - p)**7
#     print(f"Valoare teoretică: (1-p)^7 = {prob_teoretica:.4f}")
    
#     # 2. Histograma metodei Monte Carlo
#     plt.figure(figsize=(15, 5))
    
#     plt.subplot(1, 3, 1)
#     max_zile = 50  # Afișăm doar primele 50 de zile pentru claritate
#     zile_filtrate = zile_pana_la_intalnire[zile_pana_la_intalnire <= max_zile]
    
#     bins = np.arange(0.5, max_zile + 1.5, 1)
#     hist, bin_edges = np.histogram(zile_filtrate, bins=bins, density=True)
    
#     plt.bar(bin_edges[:-1], hist, width=1, alpha=0.7, color='blue', edgecolor='black')
#     plt.xlabel('Ziua primei întâlniri')
#     plt.ylabel('Probabilitate')
#     plt.title('Distribuția geometrică - Metoda Monte Carlo\n(Prima zi cu întâlnire)')
#     plt.grid(True, alpha=0.3)
    
#     # 3. Metoda cu formula geometrică (intervalelor)
#     print("\n#3 Simulare folosind formula distribuției geometrice:")
    
#     def generare_geometrica_formula(p, num_valori):
#         """Generează valori geometrice folosind formula cu logaritmi"""
#         s = np.random.random(num_valori)
#         # Formula: k = 1 + floor(ln(1-s) / ln(1-p))
#         k = 1 + np.floor(np.log(1 - s) / np.log(1 - p))
#         return k.astype(int)
    
#     zile_geometric_formula = generare_geometrica_formula(p, num_simulari)
    
#     plt.subplot(1, 3, 2)
#     zile_filtrate_formula = zile_geometric_formula[zile_geometric_formula <= max_zile]
    
#     hist_formula, bin_edges_formula = np.histogram(zile_filtrate_formula, 
#                                                  bins=bins, density=True)
    
#     plt.bar(bin_edges_formula[:-1], hist_formula, width=1, alpha=0.7, 
#             color='red', edgecolor='black')
#     plt.xlabel('Ziua primei întâlniri')
#     plt.ylabel('Probabilitate')
#     plt.title('Distribuția geometrică - Formula\n(Prima zi cu întâlnire)')
#     plt.grid(True, alpha=0.3)
    
#     # 4. Comparație cu distribuția teoretică
#     plt.subplot(1, 3, 3)
    
#     # Calculăm probabilitățile teoretice
#     k_values = np.arange(1, max_zile + 1)
#     prob_teoretice = [(1 - p)**(k-1) * p for k in k_values]
    
#     plt.bar(k_values, prob_teoretice, alpha=0.7, color='green', 
#             edgecolor='black', label='Teoretic')
#     plt.xlabel('Ziua primei întâlniri')
#     plt.ylabel('Probabilitate')
#     plt.title('Distribuția geometrică - Teoretic\n(Prima zi cu întâlnire)')
#     plt.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.show()
    
#     # Afișăm primele 10 probabilități teoretice
#     print("\nPrimele 10 probabilități teoretice:")
#     for k in range(1, 11):
#         prob_teoretica = (1 - p)**(k-1) * p
#         print(f"P(X = {k}) = {prob_teoretica:.6f}")
    
#     # Comparație între metode
#     print(f"\nComparație între metode pentru primele {max_zile} zile:")
#     print(f"Metoda Monte Carlo - medie: {np.mean(zile_pana_la_intalnire):.2f} zile")
#     print(f"Metoda Formula - medie: {np.mean(zile_geometric_formula):.2f} zile")
#     print(f"Valoare teoretică - medie: {1/p:.2f} zile")

# # Rularea simulării
# simulare_geometrica()

# print("\n" + "="*50)
# print("Explicație detaliată a metodelor:")
# print("="*50)

# print("""
# EXPLICAȚIE DETALIATĂ:

# 1. DISTRIBUȚIA GEOMETRICĂ:
#    - Modelăm timpul până la primul succes (prima întâlnire)
#    - P(X = k) = (1-p)^(k-1) × p
#    - unde k = ziua primei întâlniri, p = 0.09

# 2. METODA MONTE CARLO DIRECTĂ:
#    - Pentru fiecare simulare:
#      * Generăm zile consecutive
#      * La fiecare zi, probabilitatea p să întâlnim pe cineva
#      * Ne oprim la prima întâlnire
#    - P(X > 7) = probabilitatea să nu întâlnim pe nimeni în primele 7 zile
#      = (1-p)^7 = (0.91)^7 ≈ 0.5168

# 3. METODA CU FORMULA (INTERVALELOR):
#    - Folosim transformarea: k = 1 + floor(ln(1-s) / ln(1-p))
#    - unde s este un număr aleator uniform în [0,1)
#    - Această metodă este mai eficientă computațional

# 4. INTERPRETARE REZULTATE:
#    - Media teoretică: 1/p = 1/0.09 ≈ 11.11 zile
#    - Modul (cea mai probabilă valoare): întotdeauna 1
#    - Distribuția este descrescătoare: P(X=1) > P(X=2) > P(X=3) > ...
# """)

# Cu Dragos, ex 2

import numpy as np
from math import factorial
from matplotlib import pyplot as plt

def prob(k, l):
    return l**k * np.exp(-l) / factorial(k)


def ex2():
    n = 10000
    l = 20 #lambda
    k = 30
    ora = 3600
    p = l/ora
    fig, ax1 = plt.subplots()
    total_mesaje_ora = [0] * ora
    caz_bun = []

    for _ in range(n):
        nr_mes = 0
        for _ in range(ora):     
            c = np.random.random()
            if c <= p:
                nr_mes += 1
        if nr_mes == k:
            
            caz_bun.append(c)
        total_mesaje_ora.append(nr_mes)
        print(np.average(total_mesaje_ora))
    ax1.hist(caz_bun, bins= range(max(caz_bun)+2), density=True, alpha=0.7, color='blue', edgecolor='black')

    v = []
    for _ in range(n):
        s = np.random.random()
        capat_interval = prob(0, l)
        k = 0
        while (s > capat_interval):
            k += 1
            capat_interval += prob(k, l)
        v.append(k)
    # histograma pentru asta
    fig, ax2 = plt.subplots()
    ax2.hist(v, bins=range(0, (max(v)+2)), density=True, alpha=0.7, color='red', edgecolor='black')
    plt.show()


        
ex2()