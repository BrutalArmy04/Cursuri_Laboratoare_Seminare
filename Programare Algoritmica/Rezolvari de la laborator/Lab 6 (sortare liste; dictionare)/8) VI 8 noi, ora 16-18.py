## Laborator 6, VI 8 noi, ora 16-18

# L = [4,6,13,17,2,14]
#
# L.sort(reverse=True)
# print(L)
#
# L2 = sorted(L, reverse=True)
# print(L2)

# L = [4,6,13,173,2,142, 189, 2222]
#
# ## a)
# print(sorted(L, key = str))
#
# ## b)
# print(sorted(L, key = lambda x: str(x)[::-1]))
#
# ## c)
# print(sorted(L, key = lambda x: len(str(x)), reverse=True ))
# print(sorted(L, key = lambda x: -len(str(x)) ))
#
# ## d)
# print(sorted(L, key = lambda x:  len(set(str(x)))))
#
# ## e)
# print(sorted(L, key = lambda x: (len(str(x)), -x) ))

# d = {} ## dictionar vid
# m = set() ## multimea vida

## Problema 2

f = open("pb2_elevi.in")
d = {}
for linie in f:
    # cnp, nume, prenume, *note = linie.split() #note este o lista de str-uri
    #cnp, nume, prenume, note = linie.split(' ', 3) #note este str
    cnp, nume, prenume, note = linie.split(maxsplit = 3) #note este str

    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]
    d[cnp] = [nume, prenume, L_note]

f.close()
# print(d)



## b)
"""
b) Scrieți o funcție care primește ca parametri un cnp și structura 
de date în care s-au memorat datele despre elevi la punctul a) și 
crește cu 1 prima notă a elevului cu cnp-ul primit ca parametru. 
Funcția returnează nota după modificare sau None dacă cnp-ul nu există.
 Apelați funcția pentru un cnp citit de la tastatură.
"""


def cresteNota(cnp, d):
    if cnp not in d:
        return None
    d[cnp][2][0] += 1
    return d[cnp][2][0]

# cnp = int(input("Cnp-ul este: "))
# print(cresteNota(cnp, d))
# print(d)



## c)
"""
Scrieți o funcție care primește ca parametri un cnp, o listă de note 
și structura de date în care s-au memorat datele despre elevi la 
punctul a) și adaugă lista de note la notele elevului  cu cnp-ul
 primit ca parametru. Funcția returnează lista de note după 
 modificare sau None dacă cnp-ul nu există. Apelați funcția pentru 
 un cnp citit de la tastatură si lista l_note=[10,8].
"""

def adaugaNote(cnp, L_note, d):
    if cnp in d:
        # d[cnp][2].extend(L_note)
        d[cnp][2] += L_note
        return d[cnp][2]

# cnp = int(input("Cnp-ul este: "))
# print(adaugaNote(cnp, [10, 8], d))
# print(d)



## d)
"""
Scrieți o funcție care primește ca parametri un cnp și structura
 de date în care s-au memorat datele despre elevi la punctul a)
  și șterge informațiile despre elevul cu acest cnp. Apelați 
  funcția pentru un cnp citit de la tastatură (dacă cnp-ul nu 
  este în listă funcția nu va modifica nimic și nu va da eroare) 
"""

def stergeElev(cnp, d):
    if cnp in d:
        del d[cnp]

# cnp = int(input("Cnp-ul este: "))
# print(stergeElev(cnp, d))
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
# L_rez = sorted(d.values(),
#                key = lambda L: (-sum(L[2]) / len(L[2]), L[0]))
# print(L_rez)


# g = open('pb2_elevi.out', 'w')
# for elev in L_rez:
#     g.write(str(elev) + '\n')
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
# def genereaza_coduri(d):
#     for cnp in d:
#         cod = "".join(random.choices(string.ascii_letters , k=3)
#                       + random.choices("1234567890" , k=3))
#         d[cnp].append(cod)
#
# genereaza_coduri(d)
# print(d)


# ## Problema 3
#
# f=open("pb3.in")
# Lcuv=f.read().split()
# f.close()
# print(Lcuv)
#
# p=int(input("p="))
# d={}
# for cuv in Lcuv:
#     sufix=cuv[-p:]
#     if sufix not in d:
#         d[sufix]=[cuv]
#     else:
#         d[sufix]+=[cuv]
#         #d[sufix].append(cuv)
# print(d)
#
# L_rez=sorted(d.values(), key= lambda L: -len(L))
# print(*L_rez, sep='\n')
# g=open("pb3_rime.txt",'w')
# for L in L_rez:
#     g.write(" ".join(sorted(L, reverse=True))+'\n')
# g.close()



# ## Problema4
# f=open("pb4.in")
# Lcuv=f.read().split()
# f.close()
# print(Lcuv)
# 
# 
# d={}
# for cuv in Lcuv:
#     litere=frozenset(cuv)
#     if litere not in d:
#         d[litere]=[cuv]
#     else:
#         d[litere]+=[cuv]
#         #d[litere].append(cuv)
# print(d)
# 
# L_rez=[sorted(Lcuv, key=lambda x : (len(x), x))
#        for litere, Lcuv in sorted(d.items(),
#                                   key= lambda t: -len(t[0]) )
#        if len(Lcuv)>=2]
# print(*L_rez,sep='\n')
# 
# 
# g=open("pb4.out",'w')
# g.write("\n".join([" ".join(lista) for lista in L_rez]))
# g.close()

