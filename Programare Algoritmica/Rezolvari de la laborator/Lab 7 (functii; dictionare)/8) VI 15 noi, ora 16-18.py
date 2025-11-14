## Laborator 7, VI 15 noi, ora 16-18


# ## Problema 1
# ## a)
# def citire():
#     n = int(input("n= "))
#     L = [int(input(f'L[{i}] = ')) for i in range(n)]
#     return n,L
#
# ## b)
# def cautare(s,x,i=0,j=None):
#     if j is None:
#         j = len(s)
#     for k in range(i,j):
#         if s[k] > x:
#             return k
#     return -1
#
# ## c)
# n,L = citire()
# for k in range(n-1):
#     ## rezolvare in O(n^2)
#     ##if cautare(L,L[k],k+1) != -1: ## j - valoare Default
#
#     ## rezolvare in 0(n)
#     if cautare(L,L[k],k+1,k+2) != -1:
#         print("Nu")
#         break
#     else:
#         pass
# else:
#     print("Da")



# ## Problema 2
# ## a)
# def alipire(*numere):
#     return int("".join([max(str(x)) for x in numere]))
#
# ## b)
# def baza2(a, b, c):
#     return alipire(a, b, c) == 111
#
# print(baza2(1001, 100, 1))
# print(baza2(1001, 100, 17))
# print(baza2(1001, 100, 0))


# ## Problema 3
# def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
#     cuv=cuv.lower()
#     g=open(nume_fis_out,"w")
#     for nume in nume_fis_in:
#         L=[]    #indecsii liniilor
#         f=open(nume,"r")
#         for i,linie in enumerate(f):
#             L_cuv=[c.strip("!?.,:;") for c in linie.lower().replace("-"," ").split()]
#             if cuv in L_cuv:
#                 L.append(i+1)
#         f.close()
#         g.write(f"{nume} {"cuvantul nu a fot gasit" if L==[]
#         else " ".join([str(x) for x in L])}\n")
#     g.close()
#
# # cautare_cuvant("flOarE","rez.txt", "eminescu.txt", "paunescu.txt")
# cautare_cuvant("AlbAstra","rez.txt", "eminescu.txt", "paunescu.txt")



## Problema 4
## a)
def citire():
    d = {}
    with open("cinema.in", "r") as f:
        for linie in f:
            cinema, film, ore = linie.split(" % ")
            L_ore = ore.strip().split()
            if cinema not in d:
                d[cinema] = {}
            d[cinema][film] = L_ore
    return d


d = citire()
# print(d)


## Punctul b)
def sterge_ore(d, cinema, film, multime_ore):
    if cinema in d and film in d[cinema]:
        for i in range(len(d[cinema][film]) - 1, -1, -1):
            if d[cinema][film][i] in multime_ore:
                d[cinema][film].pop(i)
        if d[cinema][film] == []:
            del d[cinema][film]
        return list(d[cinema].keys())

# f = input("Film = ")
# c = input("Cinema = ")
# o = input("Ora hh:mm = ")
#
# print(sterge_ore(d, c, f, {o}))
# print(d)


##c
def cinema_film(d, *cinematografe, ora_min, ora_max):
    rez = []
    for cinema in cinematografe:
        if cinema in d:
            for film in d[cinema]:
                aux_ore = []
                for ora in d[cinema][film]:
                    if ora_min <= ora <= ora_max:
                        aux_ore.append(ora)
                if aux_ore != []:
                    rez.append((film, cinema, aux_ore))
    rez.sort(key=lambda t: (t[0], -len(t[2])))
    return rez

# print(cinema_film(d, "Cinema 1", "Cinema 2", ora_min="14:00", ora_max="22:00"))

