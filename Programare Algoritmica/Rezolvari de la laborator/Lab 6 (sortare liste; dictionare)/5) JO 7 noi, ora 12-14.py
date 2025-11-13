## Laborator 6, JO 7 noi, ora 12-14

# L = [4,6,13,17,2,14]
#
# L.sort()
# print(L)
#
# L2 = sorted(L, reverse=True)
# print(L2)
#

# ## Problema 1
#
# L = [4,6,13,17,2,14]
#
# ## a)
# print(sorted(L, key=str))
#
# ## b)
# print(sorted(L, key = lambda x: str(x)[::-1]))
#
# ## c)
# print(sorted(L, key = lambda x: len(str(x)), reverse=True))
# print(sorted(L, key = lambda x: -len(str(x)) ))
#
# ## d)
# L = [4,6,13,173,2,142, 189, 2222]
# print(sorted(L, key = lambda x: len(set(str(x))) ))
#
# ## e)
# print(sorted(L, key = lambda x: (len(str(x)), -x)  ))


# d = {} ## dictionar vid
# m = set() ## multimea vida

## Problema 2

## a)
# t = ([1,2,3], [4,5])
# # t[0] = [10, 11]
# t[0][0] = 13
# print(t)

f = open("pb2_elevi.in")
D = {}
for linie in f:
    # cnp, nume, prenume, *note = linie.split() #note = lista de str-uri
    # cnp, nume, prenume, note = linie.split(" ", 3) #note=str
    cnp, nume, prenume, note = linie.split(maxsplit=3) #note = str
    cnp=int(cnp)
    L_note=[int(x) for x in note.split()]
    D[cnp]=[nume,prenume,L_note]
f.close()
# print(D)


## b)
"""
b) Scrieți o funcție care primește ca parametri un cnp și structura 
de date în care s-au memorat datele despre elevi la punctul a) și 
crește cu 1 prima notă a elevului cu cnp-ul primit ca parametru. 
Funcția returnează nota după modificare sau None dacă cnp-ul nu există.
 Apelați funcția pentru un cnp citit de la tastatură.
"""
def creste_nota(cnp,d):
    if cnp not in d:
        return None
    d[cnp][2][0]+=1
    return d[cnp][2][0]

# cnp= int(input("cnp = "))
# print(creste_nota(cnp,D))
# print(D)


## c)
"""
Scrieți o funcție care primește ca parametri un cnp, o listă de note 
și structura de date în care s-au memorat datele despre elevi la 
punctul a) și adaugă lista de note la notele elevului  cu cnp-ul
 primit ca parametru. Funcția returnează lista de note după 
 modificare sau None dacă cnp-ul nu există. Apelați funcția pentru 
 un cnp citit de la tastatură si lista l_note=[10,8].
"""

def adaugaNote(cnp, L_note, D):
    if cnp in D:
        D[cnp][2].extend(L_note)
        # sau
        # D[cnp][2] += L_note
        return D[cnp][2]

# cnp= int(input("cnp = "))
# print(adaugaNote(cnp, [10, 8], D))
# print(D)

## d)
"""
Scrieți o funcție care primește ca parametri un cnp și structura
 de date în care s-au memorat datele despre elevi la punctul a)
  și șterge informațiile despre elevul cu acest cnp. Apelați 
  funcția pentru un cnp citit de la tastatură (dacă cnp-ul nu 
  este în listă funcția nu va modifica nimic și nu va da eroare) 
"""

def stergeElev(cnp, D):
    if cnp in D:
        del D[cnp]

# cnp= int(input("cnp = "))
# print(stergeElev(cnp, D))
# print(D)



## e)
"""
Folosind structura de date în care s-au memorat datele despre 
elevi la punctul a) (nu citind din nou datele) construiți în 
memorie o lista de liste cu elevii din fișier, un element din 
lista fiind de forma [nume, prenume, lista de note] ordonată 
descrescător după medie și, în caz de egalitate, după nume și
 afișați elementele listei în fișierul „elevi.out”.
 """

# L_rez = sorted(D.values(),
#                key = lambda L: (-sum(L[2]) / len(L[2]), L[0]))
# # print(L_rez)
#
# g = open("pb2_elevi.out", "w")
# for elev in L_rez:
#     g.write(str(elev) + "\n")
# g.close()


## f)
"""
Scrieți o funcție care primește ca parametru structura de
 date în care s-au memorat datele despre elevi la punctul a) 
 și adaugă la informațiile asociate unui student un
  cod de lungime 6 generat aleator care conține 3 litere urmate
   de 3 cifre. Exemplu de apel: 
genereaza_coduri(d) 
print(d)
"""
# import random
# import string
#
# # print(random.choices(string.ascii_letters , k=3))
#
# def genereaza_coduri(D):
#     for cnp in D:
#         cod = ''.join(random.choices(string.ascii_letters , k=3)
#                       + random.choices("0123456789" , k=3))
#         (D[cnp].append(cod))
#
# genereaza_coduri(D)
# print(D)



# ## Problema 3
# f = open("pb3.in", "r")
# L_cuv = f.read().split()
# f.close()
#
# p = int(input("p = "))
# D = {}
# for cuv in L_cuv:
#     if cuv[-p:] not in D:
#         D[cuv[-p:]] = [cuv]
#     else:
#         # D[cuv[-p:]] += [cuv]
#         # sau
#         D[cuv[-p:]].append(cuv)
# # print(D)
#
# L_rez = sorted(D.values(), key = lambda L: -len(L))
# # print(L_rez)
#
# g = open("pb3_rime.txt", "w")
# for L in L_rez:
#     g.write(" ".join(sorted(L, reverse = True)) + "\n")
# g.close()


# ## Problema 4
#
# f = open("pb4.in", "r")
# L_cuv = f.read().split()
# f.close()
#
# d={}
# for cuv in L_cuv:
#     litere=frozenset(cuv)
#     if litere not in d:
#         d[litere]=[cuv]
#     else:
#         d[litere].append(cuv)
# print(d)
#
# rez= [sorted(L_cuv, key= len)
#     for litere, L_cuv in sorted(d.items(),
#                     key=lambda t: -len(t[0]))
#		if len(L_cuv) >= 2]
# print(rez)

