import math
import random
import bisect
import matplotlib.pyplot as plt
import numpy as np

def citire_date(nume_fisier="input.txt"):
    with open(nume_fisier, 'r') as f:
        n = int(f.readline().strip())
        st, dr = map(float, f.readline().strip().split())
        a, b, c = map(float, f.readline().strip().split())
        p = int(f.readline().strip())
        prob_crossover = float(f.readline().strip())
        prob_mutatie = float(f.readline().strip())
        etape = int(f.readline().strip())
        
    return n, st, dr, a, b, c, p, prob_crossover, prob_mutatie, etape

n, st, dr, a, b, c, p, prob_crossover, prob_mutatie, etape = citire_date()

l = math.ceil(math.log2((dr-st)*10**p))
d = (dr-st)/2**l

populatie = []

for i in range(n):
    individ = ''
    for num in range(l):
        individ += random.choice(['0', '1'])

    int_individ = int(individ, 2)
    val = st + int_individ * d
    fitness = a * val ** 2 + b * val + c

    populatie.append({
        "biti": individ,
        "x": val,
        "fitness": fitness
    })

open("Evolutie.txt", 'w').close()

plt.ion() 
fig, ax = plt.subplots(figsize=(10, 6))

x_grafic = np.linspace(st, dr, 200)
y_grafic = a * x_grafic**2 + b * x_grafic + c

ax.plot(x_grafic, y_grafic, label=f"f(x) = {a}x^2 + {b}x + {c}", color="blue", linewidth=2)

scatter_populatie = ax.scatter([], [], color="red", zorder=5, label="Indivizi")

ax.set_title("Evolutia Algoritmului Genetic")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)


for etapa in range(etape):
    elita = max(populatie, key=lambda ind: ind['fitness'])

    suma_fitness = sum(ind["fitness"] for ind in populatie)

    lista_p = []
    lista_q = [0.0] 
    suma_partiala = 0.0

    for ind in populatie:
        p_i = ind["fitness"] / suma_fitness
        lista_p.append(p_i)
        suma_partiala += p_i
        lista_q.append(suma_partiala)

    if etapa == 0:
        with open("Evolutie.txt", "a") as f:
            f.write("Populatia initiala:\n")
            for i, ind in enumerate(populatie):
                f.write(f"Individ {i+1:2}: Bi = {ind['biti']}, Xi = {round(ind['x'], p)}, f(Xi) = {round(ind['fitness'], p)}\n")
            
            f.write("\nProbabilitati selectie:\n")
            for i, prob in enumerate(lista_p):
                f.write(f"Cromozom {i+1:2} probabilitate {prob}\n")
                
            f.write("\nIntervale probabilitati cumulate:\n")
            for q in lista_q:
                f.write(f"{q}\n")
                
            f.write("\nProcesul de selectie:\n")

    populatie_selectata = []

    for _ in range(n):
        u = random.random()
        index = bisect.bisect_right(lista_q, u)
        populatie_selectata.append(populatie[index - 1].copy())
        
        if etapa == 0:
            with open("Evolutie.txt", "a") as f:
                f.write(f"u={round(u, 5)} selectam cromozomul {index}\n")

    indici_crossover = []

    if etapa == 0:
        with open("Evolutie.txt", "a") as f:
            f.write(f"\nProbabilitatea de incrucisare {prob_crossover}\n")
            for i, pop_ind in enumerate(populatie_selectata):
                u = random.random()
                f.write(f"{i+1:2}: {pop_ind['biti']} u={round(u, 5)}")
                if u < prob_crossover:
                    indici_crossover.append(i)
                    f.write(f" < {prob_crossover} participa\n")
                else:
                    f.write("\n")
            f.write("\n")
    else:
        for i in range(n):
            u = random.random()
            if u < prob_crossover:
                indici_crossover.append(i)

    if etapa == 0:
        with open("Evolutie.txt", "a") as f:
            for i in range(0, len(indici_crossover) - 1, 2):
                idx1 = indici_crossover[i]
                idx2 = indici_crossover[i+1]
                
                p1 = populatie_selectata[idx1]['biti']
                p2 = populatie_selectata[idx2]['biti']
                
                punct = random.randint(1, l - 1)
                
                c1 = p1[:punct] + p2[punct:]
                c2 = p2[:punct] + p1[punct:]
                
                populatie_selectata[idx1]['biti'] = c1
                val_c1 = st + int(c1, 2) * d
                populatie_selectata[idx1]['x'] = val_c1
                populatie_selectata[idx1]['fitness'] = a * val_c1 ** 2 + b * val_c1 + c
                
                populatie_selectata[idx2]['biti'] = c2
                val_c2 = st + int(c2, 2) * d
                populatie_selectata[idx2]['x'] = val_c2
                populatie_selectata[idx2]['fitness'] = a * val_c2 ** 2 + b * val_c2 + c
                
                f.write(f"Recombinare intre cromozomul {idx1+1} si {idx2+1}:\n")
                f.write(f"{p1} {p2} punct {punct}\n")
                f.write(f"Rezultat: {c1} {c2}\n")
    else:
        for i in range(0, len(indici_crossover) - 1, 2):
            idx1 = indici_crossover[i]
            idx2 = indici_crossover[i+1]
            
            p1 = populatie_selectata[idx1]['biti']
            p2 = populatie_selectata[idx2]['biti']
            
            punct = random.randint(1, l - 1)
            
            c1 = p1[:punct] + p2[punct:]
            c2 = p2[:punct] + p1[punct:]
            
            populatie_selectata[idx1]['biti'] = c1
            val_c1 = st + int(c1, 2) * d
            populatie_selectata[idx1]['x'] = val_c1
            populatie_selectata[idx1]['fitness'] = a * val_c1 ** 2 + b * val_c1 + c
            
            populatie_selectata[idx2]['biti'] = c2
            val_c2 = st + int(c2, 2) * d
            populatie_selectata[idx2]['x'] = val_c2
            populatie_selectata[idx2]['fitness'] = a * val_c2 ** 2 + b * val_c2 + c

    if etapa == 0:
        with open("Evolutie.txt", "a") as f:
            f.write("\nPopulatia dupa recombinare:\n")
            for i, ind in enumerate(populatie_selectata):
                f.write(f"Individ {i+1:2}: Bi = {ind['biti']}, Xi = {round(ind['x'], p)}, f(Xi) = {round(ind['fitness'], p)}\n")

            f.write(f"\nProbabilitatea de mutatie pentru fiecare bit {prob_mutatie}\n")
            f.write("Au fost modificati cromozomii:\n")

    for i, ind in enumerate(populatie_selectata):
        biti_noi = ""
        modificat = False
        
        for bit in ind['biti']:
            u = random.random()
            if u < prob_mutatie:
                biti_noi += '1' if bit == '0' else '0'
                modificat = True
            else:
                biti_noi += bit

        if modificat:
            ind['biti'] = biti_noi
            val_noua = st + int(biti_noi, 2) * d
            ind['x'] = val_noua
            ind['fitness'] = a * val_noua ** 2 + b * val_noua + c
            
            if etapa == 0:
                with open("Evolutie.txt", "a") as f:
                    f.write(f"{i+1}\n")

    if etapa == 0:
        with open("Evolutie.txt", "a") as f:
            f.write("\nPopulatia dupa mutatie:\n")
            for i, ind in enumerate(populatie_selectata):
                f.write(f"Individ {i+1:2}: Bi = {ind['biti']}, Xi = {round(ind['x'], p)}, f(Xi) = {round(ind['fitness'], p)}\n")

    weak = min(range(n), key=lambda i: populatie_selectata[i]['fitness'])
    populatie_selectata[weak] = elita.copy()
    
    populatie = populatie_selectata.copy()


    x_curenti = [ind['x'] for ind in populatie]
    y_curenti = [ind['fitness'] for ind in populatie]
    scatter_populatie.set_offsets(np.c_[x_curenti, y_curenti])
    ax.set_title(f"Evolutia Algoritmului Genetic - Etapa {etapa + 1}/{etape}")
    plt.pause(0.1)

    with open("Evolutie.txt", "a") as f:
        if etapa > 0:
            max_fit = max(ind['fitness'] for ind in populatie)
            mean_fit = sum(ind['fitness'] for ind in populatie) / n
            f.write(f"\nEvolutia dupa etapa {etapa}:\n")
            f.write(f"Max Fitness: {max_fit}\n")
            f.write(f"Mean Fitness: {mean_fit}\n")

plt.ioff()
plt.show()