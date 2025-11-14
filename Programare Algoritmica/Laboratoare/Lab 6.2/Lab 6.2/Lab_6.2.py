import random
import string

# #d = {} dictionar vid
# #m = set() multimea
# d = {}
# f = open('elevi.in', 'r')
# for linie in f:
#     # cnp, nume, prenume, *note = linie.split(' ', 3) 
#     # cnp, nume, prenume, *note = linie.split(maxsplit=3) 
#     # cnp = int(cnp)
#     # L_note = [int(x) for x in note.split()]
#     # d[cnp] = [nume, prenume, L_note]
#     # cnp, nume, prenume, *note = linie.split() #note este o lista de str
#     # print(cnp, nume, prenume, note, sep = '\n')
#     cnp, nume, prenume, note = linie.split(' ', 3)
#     cnp, nume, prenume, note = linie.split(maxsplit=3)  # note este str

#     cnp = int(cnp)
#     L_note = [int(x) for x in note.split()]
#     d[cnp] = [nume, prenume, L_note]
# f.close()
# print(d)

# def creare_nota(cnp, d):
#     if cnp not in d:
#         return None
#     d[cnp][2] += 1
#     return d[cnp][2][0]

# # cnp = 2501910000034
# # print(creare_nota(cnp, d))

# def adauga_nota(cnp, L, d):
#     if cnp in d.keys():
#         #d[cnp][2]+=L
#         d[cnp][2].extend(L)
#         return d[cnp][2]
# # cnp = 2501910000034
# # print(adauga_nota(cnp, [10,8], d))
# # print(d)

# def sterge_elev(cnp, d):
#     if cnp in d:
#         del d[cnp]
# # cnp = 250410000034
# # sterge_elev(cnp, d)
# # print(d)

# Lrez = sorted(d.values(), key = lambda L: (-sum(L[2])/(len(L[2])), L[0]))
# print(Lrez)
# g = open('elevi.out', 'w')
# for elev in Lrez:
#     g.write(str(elev) + '\n')
# g.close()

# #f e pe wapp la tudor



#Problema 3

# f = open("rime.txt", 'r')
# L_cuv = f.read().split()
# f.close()
# print(L_cuv)
# p = 2
# d = {}
# for cuv in L_cuv:
#     sufix = cuv[-p:]
#     if sufix not in d.keys():
#         d[sufix] = [cuv]
#     else:
#         d[sufix].append(cuv)
# print(d)
# L_rez = sorted(d.values(), key = lambda L_cuv : -len(L_cuv))
# print(L_rez)

# g = open ('rimes.txt', 'w')
# for L_cuv in L_rez:
#     g.write(sorted(L_cuv, reverse = True) + '\n')
# g.close()

# Problema 4
f = open("rime.txt", 'r')
L_cuv = f.read().split()
f.close()
print(L_cuv)
d={}
for cuv in L_cuv:
     litere = frozenset(cuv)
     if litere not in d.keys():
         d[litere] = [cuv]
     else:
        d[litere].append(cuv)
print(d)
L_rez = [sorted(L_cuv, reverse = True) for litere, L_cuv in sorted(d.items()), key = lambda t : -len(t[0]) if len(L_cuv) >= 2]