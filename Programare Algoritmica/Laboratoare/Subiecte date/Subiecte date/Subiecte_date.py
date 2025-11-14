# Scrieți o funcție citire_numere cu un parametru reprezentând numele unui fișier text 
# care conține, pe mai multe linii, numere naturale despărțite între ele prin spații și returnează o 
# listă de liste (numite subliste), elementele unei subliste fiind numerele de pe o linie din fișier. 

# Să se scrie o funcție prelucrare_lista care primește ca parametru o listă de liste pe care 
# o modifică astfel: 
# • din fiecare sublistă se vor elimina toate aparițiile valorii minime, apoi  
# • din fiecare sublistă se vor păstra doar primele m elemente, unde m reprezintă lungimea 
# minimă a unei subliste.

# Se dă fișierul "numere.in" cu următoarea structură: pe linia 𝑖 se află separate prin câte 
# un spațiu 𝑛 numere naturale reprezentând elementele de pe linia 𝑖 a unei matrice, ca în exemplul 
# de mai jos. Să se apeleze funcția prelucrare_lista pentru matricea obținută în urma apelului 
# funcției citire_numere pentru fișierul text numere.in. Matricea astfel obținută să se afișeze pe 
# ecran, fără paranteze și virgule, iar elementele de pe fiecare linie să fie separate prin câte un 
# spațiu. 

#  Fie L matricea (memorată ca listă de liste) obținută în urma apelării funcției citire_numere 
# pentru fișierul text "numere.in". Să se citească de la tastatură un număr natural nenul k și apoi 
# să se scrie în fișierul text "cifre.out" elementele matricei L care sunt formate din exact k cifre sau 
# mesajul “Imposibil!” dacă nu există niciun element cu proprietatea cerută. Elementele vor fi 
# scrise în fișier în ordine descrescătoare și fără duplicate.


# 100 54 101 54 2 81 92 
# 10 1 1 2 2 1 70 
# 12 81 10 8 9 8 10

# n = 0
# def citire_numere(f):
#     global n
#     for line in f.readlines():
#         mat.append([int(x) for x in line.split()])
#         n += 1

# def prelucrare_lista(mat):
#     lmin = None
#     for l in mat:
#         if lmin is None:
#             lmin = len(l)
#         minim = min(l)
#         while True:
#             if minim not in l:
#                 break
#             else:
#                 l.remove(minim)
#         if len(l)<lmin:
#             lmin = len(l)
#     for l in mat:
#         while len(l) != lmin:
#             l.pop()
#     for l in mat:
#         for item in l:
#             print(item, end = " ")
#         print()
    
    




# mat = []
# f = open("input.txt")
# citire_numere(f)

# nr_k_cifre = []

# k = 2 # k = int(input("k= "))

# for l in mat:
#     for item in l:
#         if len(str(item)) == k:
#             nr_k_cifre.append(item)

# nr_k_cifre = list(set(nr_k_cifre))
# nr_k_cifre = sorted(nr_k_cifre, reverse = True)
# print(nr_k_cifre)

# prelucrare_lista(mat)


# def insereaza_legatura():
#     pass





# i = 0
# with open('input.txt') as f:
#     for line in f.readlines():
#         i += 1
# L = []

# with open('input.txt') as f:
#     for line in f.readlines():
#         c1, c2, culoare, *eticheta = line.split()
#         c1 = c1.strip('[')
#         c1 = c1.strip(']')
#         c2 = c2.strip('[')
#         c2 = c2.strip(']')
#         c1 = c1.split(sep = ',')
#         for i in range(len(c1)):
#             c1[i] = int(c1[i])
#         c1 = tuple(c1)
#         c2 = c2.split(sep = ',')
#         for i in range(len(c2)):
#             c2[i] = int(c2[i])
#         c2 = tuple(c2)
#         eticheta = eticheta[0] + " " + eticheta[1]
#         l = []
#         l.append(c1)
#         l.append(c2)
#         l.append(culoare)
#         l.append(eticheta)
#         L.append(l)

# print(L)
def citire():
    m = n = None
    d = {}
    with open('input.txt') as f:
        for line in f.readlines():
            if m is None:
                m, n = line.strip().split()
                m, n = int(m), int(n)
            elif m!=0:
                cod_autor, nume_autor = line.strip().split(maxsplit = 1)
                cod_autor = int(cod_autor)
                m -= 1
                d[cod_autor] = []
                d[cod_autor].append(nume_autor)
                d[cod_autor].append({})

            else:
                cod_autor, cod_carte, an_carte, nr_pagini, nume_carte = line.strip().split(maxsplit = 4)
                cod_autor = int(cod_autor)
                cod_carte = int(cod_carte)
                an_carte = int(an_carte)
                nr_pagini = int(nr_pagini)
                d[cod_autor][1].update({cod_carte:[an_carte, nr_pagini, nume_carte]})
    return d

def sterge_date(d, cod_carte):
    for autor in d:
        r = d[autor][1].pop(cod_carte, None)
        if r is not None:
            print(f"Cartea a fost scrisa de {d[autor][0]}")
            return d
    else:
        print('Cartea nu a fost gasita')
        return d

def carti_autor(d, cod_autor):
    for autor in d:
        if autor == cod_autor:
            print(d[autor][0])
            for carte in d[autor][1]:
                sorted((d[autor][1][carte], key = d[autor][1][carte][2], reverse = True)
                #print(d[autor][1][carte][2], d[autor][1][carte][0], d[autor][1][carte][1])
            return
    else:
        print('cod incorect')
        return



d = citire()
g = open('output.txt', 'w')
g.write(str(d))

#d = sterge_date(d, 214)
carti_autor(d, 11)
g.close()