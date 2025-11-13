## Laborator 6, MI 6 noi, ora 12-14

# L = [4,6,13,17,2,14]

# L.sort()
# print(L)
#
# L2 = sorted(L, reverse=True)
# print(L2)
#
# L = ["ana", "cana", "blabla"]
# L2 = sorted(L, key = len)
# print(L2)

## Problema 1
# L = [4,6,1223,12277,2,7,14, 33, 23]
#
# ## a)
# print(sorted(L, key=str))
#
# ## b)
# print(sorted(L, key= lambda x: str(x)[::-1]))
#
# ## c)
# print(sorted(L, key = lambda x: len(str(x)), reverse=True))
# print(sorted(L, key = lambda x: -len(str(x))))
#
# ## d)
# print(sorted(L, key=lambda x: len(set(str(x)))))
#
# ## e)
# print(sorted(L, key=lambda x : (len(str(x)), -x)))


## Problema 2
## a)
f = open("pb2_elevi.in")
d = {}  # creeaza dictionarul vid
# s=set()-creeaza multimea vida
for linie in f:
    # cnp, nume, prenume, note = linie.split(" ", 3)
    cnp, nume, prenume, note = linie.split(maxsplit=3)  # note este str
    # cnp, nume, prenume, *note = linie.split() ## note este lista
    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]

    d[cnp] = [nume, prenume, L_note]  # cnp-cheia
f.close()
print(d)

## b)
"""
b) Scrieți o funcție care primește ca parametri un cnp și structura 
de date în care s-au memorat datele despre elevi la punctul a) și 
crește cu 1 prima notă a elevului cu cnp-ul primit ca parametru. 
Funcția returnează nota după modificare sau None dacă cnp-ul nu există.
 Apelați funcția pentru un cnp citit de la tastatură.
"""


def creste_nota(cnp, d):
    if cnp not in d:
        return None
    # d[cnp][2][0] += 1

    nota = d[cnp][2][0]
    d[cnp][2][0] = (nota + 1 if nota < 10 else nota)

    return d[cnp][2][0]


# cnp1=int(input("cnp = ")) # 1412900000041
# print(creste_nota(cnp1,d))
# print(d[cnp1])

## c)
"""
Scrieți o funcție care primește ca parametri un cnp, o listă de note 
și structura de date în care s-au memorat datele despre elevi la 
punctul a) și adaugă lista de note la notele elevului  cu cnp-ul
 primit ca parametru. Funcția returnează lista de note după 
 modificare sau None dacă cnp-ul nu există. Apelați funcția pentru 
 un cnp citit de la tastatură si lista l_note=[10,8].
"""


def adauga_note(cnp, L_note, d):
    if cnp not in d:
        return None
    d[cnp][2].extend(L_note)
    ##sau
    # d[cnp][2] += L_note
    return d[cnp][2]


# cnp1=int(input("cnp = ")) # 2402900000041
# l_note=[10,8]
#
# print( adauga_note(cnp1,l_note,d) )
# print(d[cnp1])

## d)
"""
Scrieți o funcție care primește ca parametri un cnp și structura
 de date în care s-au memorat datele despre elevi la punctul a)
  și șterge informațiile despre elevul cu acest cnp. Apelați 
  funcția pentru un cnp citit de la tastatură (dacă cnp-ul nu 
  este în listă funcția nu va modifica nimic și nu va da eroare) 
"""


def sterge_elev(cnp, d):
    if cnp in d:
        del d[cnp]


# cnp1=int(input("cnp = ")) # 2402900000041
# sterge_elev(cnp1,d)
# print(d)

## e)
"""
Folosind structura de date în care s-au memorat datele despre 
elevi la punctul a) (nu citind din nou datele) construiți în 
memorie o lista de liste cu elevii din fișier, un element din 
lista fiind de forma [nume, prenume, lista de note] ordonată 
descrescător după medie și, în caz de egalitate, după nume și
 afișați elementele listei în fișierul „elevi.out”.
 """

# L_rez= sorted(d.values(),
#               key = lambda t: (-sum(t[2])/len(t[2]), t[0]))
# print(L_rez)
#
# g=open("pb2_elevi.out",'w')
# for elev in L_rez:
#     g.write(str(elev)+'\n')
#
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

import random
import string

# random.choices(string.ascii_letters , k=3)
# print(random.choices(string.ascii_letters, k=3))


def genereaza_coduri(d):
    for cnp in d:
        cod = "".join(random.choices(string.ascii_letters, k=3)
                      + random.choices("0123456789", k=3))
        d[cnp].append(cod)


# genereaza_coduri(d)
# print(d)

