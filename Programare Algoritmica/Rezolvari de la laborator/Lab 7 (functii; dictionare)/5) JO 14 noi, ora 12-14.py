## Laborator 7, JO 14 noi, ora 12-14
# #Problema 1
# #a)
#
# def fct():
#     n=int(input("n= "))
#     L=[int(input(f"L[{i}]= ")) for i in range(n)]
#     return n,L
#
# #b)
#
# def fctb(s,x,i=0,j=None):
#     if j is None:
#         j=len(s)
#     for k in range(i,j):
#         if s[k] > x:
#             return k
#     return -1
#
# #c)
#
# n,L=fct()
# for k in range(n-1):
#     if fctb(L,L[k],k+1) != -1: #j=valoarea implicita
#         print("NU")
#         break
# else:
#     print("DA")


# ## Problema 2
#
# ## a)
# def alipire(*numere):
#     Rez = int(''.join([ max(str(x)) for x in numere]))
#     return Rez
#
# ## b)
# def baza_2(a,b,c):
#     return alipire(a,b,c) == 111
#
# print(baza_2(111,101,1011))
# print(baza_2(1001,17,100))
# print(baza_2(0,11,101))


# ## Problema 3
#
# def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
#     cuv = cuv.lower()
#     with open(nume_fis_out, "w") as g:
#         for nume in nume_fis_in:
#             with open(nume) as f:
#                 L = []  # indexi liniilor
#                 for i, linie in enumerate(f):
#                     L_cuv = [c.strip("!?.,;:")
#                              for c in linie.lower().replace('-', ' ').split()]
#                     if cuv in L_cuv:
#                         L.append(i + 1)
#                 g.write(f"{nume} {"Cuvantul nu a fost gasit" if len(L) == 0
#                 else " ".join([str(x) for x in L])}\n")
#
#
# # cautare_cuvant("fLoaRe","rez.txt", "eminescu.txt", "paunescu.txt")
# cautare_cuvant("alBastRa", "rez.txt", "eminescu.txt", "paunescu.txt")


## Problema 4

## a)
def citire():
    f = open("cinema.in")
    D = {}
    for linie in f:
        cinema, film, ore = linie.split(" % ")
        L_ore = ore.strip().split()
        if cinema not in D:
            D[cinema] = {}
        D[cinema][film] = L_ore
    f.close()
    return D

D = citire()
# print(D)

## b)

def sterge_ore(D, cinema, film, Multime_ore):
    if cinema in D and film in D[cinema]:
        for i in range(len(D[cinema][film]) - 1, -1, -1):
            if D[cinema][film][i] in Multime_ore:
                D[cinema][film].pop(i)
        if len(D[cinema][film]) == 0:
            del D[cinema][film]
    return list(D[cinema].keys())


# f = input("Numele filmului: ")
# c = input("Numele cinema-ului: ")
# ora = input("Ora (hh:mm): ")
# print(sterge_ore(D, c, f, {ora}))
# print(D)

## c)
def cinema_film(D, *cinematografe, ora_minima, ora_maxima):
    rez = []
    for cinema in cinematografe:
        if cinema in D:
            for film in D[cinema]:
                aux_ore = []
                for ora in D[cinema][film]:
                    if ora_minima <= ora <= ora_maxima:
                        aux_ore.append(ora)

                if len(aux_ore) > 0:
                    rez.append((film, cinema, aux_ore))
    rez.sort(key = lambda t: (t[0], -len(t[2])))
    return rez

# print(cinema_film(D, "Cinema 1", "Cinema 2", ora_minima="14:00", ora_maxima="22:00"))

# print(type(D.keys()), type(D.values()), type(D.items()))

