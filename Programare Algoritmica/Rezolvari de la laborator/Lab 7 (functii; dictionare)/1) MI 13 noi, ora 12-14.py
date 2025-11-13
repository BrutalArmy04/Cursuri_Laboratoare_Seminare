## Laborator 7, MI 13 noi, ora 12-14

# # Pb1
# # a)
# def f():
#     n = int(input("n= "))
#     L = []
#     for x in range(n):
#         L.append(int(input("x= ")))
#     return n, L
#
#
# # b)
# def g(s, x, i=0, j=None):
#     if j is None:
#         j = len(s)
#     for p in range(i, j):
#         if s[p] > x:
#             return p
#     return -1
#
#
# # c)
# n, L = f()
# for k in range(n - 1):
#     poz = g(L, L[k], k + 1, n)
#     if poz != -1:
#         print("NU")
#         break
# else:
#     print("DA")


# ## Problema 2
# #a)
# def f1(*numere):
#     rez=int("".join([max(str(x)) for x in numere]))
#     return rez
# #b)
# def f2(a,b,c):
#     return f1(a,b,c)==111
#
# print(f2(1011,1,100))
# print(f2(1001,17,100))
# print(f2(101,10,0))


# ## Problema 3
#
# def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
#     cuv = cuv.lower()
#     with open(nume_fis_out, "w") as g:
#         for nume in nume_fis_in:
#             with open(nume, "r") as f:
#                 L = []
#                 for i, linie in enumerate(f):
#                     L_cuvinte = [x.strip(",.?;!:")
#                                  for x in linie.lower().replace("-", " ").split()]
#                     if cuv in L_cuvinte:
#                         L.append(i+1)
#                 g.write(f"{nume} {"Cuvantul nu a fost gasit" if len(L)==0
#                 else  " ".join([str(x) for x in L])}\n")
#
# cautare_cuvant("FlOare", "rez.txt", "eminescu.txt", "paunescu.txt")


## Problema 4
## a)
def citire_date():
    with open("cinema.in") as f:
        d = {}
        for linie in f:
            cinema, film, ore = linie.split(" % ")
            L_ore = ore.strip().split()

            if cinema not in d:
                d[cinema] = {}
            d[cinema][film] = L_ore

        return d


d = citire_date()
print(d)


## b)
def sterge_ore(d, cinema, film, multime_ore):
    if cinema in d and film in d[cinema]:
        for i in range(len(d[cinema][film]) - 1, -1, -1):
            if d[cinema][film][i] in multime_ore:
                d[cinema][film].pop(i)
        if len(d[cinema][film]) == 0:
            del d[cinema][film]
        return list(d[cinema].keys())


# film=input("nume film = ")
# cinema = input("cinema = ")
# ora = input("ora = ")
# L_filme = sterge_ore(d, cinema, film, {ora})
# print(L_filme)
# print(d)

## c)
def cinema_film(d, *cinematografe, ora_minima, ora_maxima):
    rez = []
    for cinema in cinematografe:
        if cinema in d:
            for film in d[cinema]:
                aux_ore = []
                for ora in d[cinema][film]:
                    if ora_minima <= ora <= ora_maxima:
                        aux_ore.append(ora)

                if len(aux_ore) != 0:
                    rez.append((film, cinema, aux_ore))

    rez.sort(key=lambda t: (t[0], -len(t[2])))
    return rez

# print(cinema_film(d,"Cinema 1","Cinema 2", ora_minima="14:00",ora_maxima="22:00"))

