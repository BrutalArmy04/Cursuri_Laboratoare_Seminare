## Laborator 7, VI 15 noi, ora 14-16

# ## Problema 1
# ## a)
# def citire():
#     n=int(input("n="))
#     L=[]
#     for i in range(n):
#         L.append(int(input(f"Elementul L[{i}]")))
#     return n,L
#
# ## b)
# def cautare (s,x,i=0,j=None):
#     if j is None:
#         j=len(s)
#     for k in range(i,j):
#         if s[k]>x:
#             return k
#     return -1
#
# ## c)
# n,L=citire()
# for k in range(n-1):
#     ##rezolvare in O(n^2); j=valoarea default
#     ##if cautare(L,L[k],k+1)!=-1:
#
#     #rezolvare in O(n)
#     if cautare(L,L[k],k+1,k+2)!=-1:
#         print("Nu e sortata")
#         break
# else:
#     print("Secventa este sortata")


# ## Problema 2
# ## a)
# def alipire(*numere):
#     return int("".join([max(str(x)) for x in numere]))
#
# ## b)
# def baza(a,b,c):
#     return alipire(a,b,c)==111
#
# print(baza(1001,100,11))
# print(baza(1001,17,101))
# print(baza(1001,0,101))
# print(alipire(4251,73,8,133))


# ## Problema 3
# def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
#     cuv = cuv.lower()
#     with open(nume_fis_out, "w") as g:
#         for nume in nume_fis_in:
#             L = []  # indecsi linii
#             with open(nume, "r") as f:
#                 for i, linie in enumerate(f):
#                     L_cuvinte = [c.strip("!.,:;?") for c in linie.lower().replace("-", " ").split()]
#                     if cuv in L_cuvinte:
#                         L.append(i + 1)
#             g.write(f"{nume} {"Cuvantul nu a fost gasit" if len(L) == 0
#             else " ".join([str(x) for x in L])}\n")
#
#
# cautare_cuvant("flOarE", "rez.txt", "eminescu.txt", "paunescu.txt")
# cautare_cuvant("albaStrA", "rez.txt", "eminescu.txt", "paunescu.txt")


## Problema 4
def citire():
    f = open("cinema.in")
    d = {}
    for linie in f:
        cinema, film, ore = linie.split(" % ")
        L_ore = ore.strip().split()
        if cinema not in d:
            d[cinema] = {}
        d[cinema][film] = L_ore
    f.close()
    return d


d = citire()
# print(d)


## b)
def sterge_ore(d, cinema, film, multime_ore):
    if cinema in d and film in d[cinema]:
        for i in range(len(d[cinema][film]) - 1, -1, -1):
            if d[cinema][film][i] in multime_ore:
                d[cinema][film].pop(i)
        if len(d[cinema][film]) == 0:
            del d[cinema][film]
        return list(d[cinema].keys())


# f = input("Filmul: ")
# c = input("Cinemaul: ")
# ora = input("hh:mm = ")
# print(sterge_ore(d,c,f,{ora}))
# print(d)


## c)
def cinema_film(d, *cinematografe, ora_min, ora_max):
    rez = []

    for cinema in cinematografe:
        if cinema in d:
            for film in d[cinema]:
                aux_ore = []
                for ora in d[cinema][film]:
                    if ora_min <= ora <= ora_max:
                        aux_ore.append(ora)
                if len(aux_ore) > 0:
                    rez.append((film, cinema, aux_ore))

    rez.sort(key=lambda t: (t[0], -len(t[2])))
    return rez

# print(cinema_film(d,"Cinema 1", "Cinema 2", ora_min="14:00", ora_max="22:00"))
