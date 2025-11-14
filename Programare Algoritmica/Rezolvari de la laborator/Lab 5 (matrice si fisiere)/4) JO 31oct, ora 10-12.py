## Laborator 5, JO 31oct, ora 10-12

## Problema 1
##Varianta1
# f = open('pb1.in', 'r')
#
# text = f.read()
# f.close()
#
# g = open('pb1.out', 'w')
# g.write(text)
# g.close()

##Varianta2
# f = open('pb1.in','r')
# g=open('pb1.out', 'a')
# while True:
#      linie = f.readline()
#      if linie == "":
#          f.close()
#          g.close()
#          break
#      g.write(linie)

##Varianta3
# with open('pb1.in','r') as f:
#     L_linii = f.readlines()
# with open('pb1.out','w') as g:
#     #g.writelines(L_linii)
#
#     g.write("".join(L_linii))


# ## Problema 2
#
# f = open("pb2_test.in")
# g = open("pb2_test.out", "w")
# nota = 1
#
# for linie in f:
#     aux, rez = linie.split("=")
#     x, y = aux.split("*")
#     x, y, rez = int(x), int(y), int(rez)
#     if x * y == rez:
#         nota = nota + 1
#         g.write(f"{linie.strip()} Corect\n")
#     else:
#         g.write(f"{linie.strip()} Gresit {x * y}\n")
#
# g.write(f"nota {nota}")
# g.close()
# f.close()


## Problema 3
"""
Se citesc m, n și o matrice cu m linii și n coloane,
elementele unei linii fiind date pe o linie
(elementele unei linii date pe o linie separate cu spațiu).
Să se creeze o listă cu maximele de pe fiecare linie
(folosind și comprehensiune)
"""

# m, n = [int(x) for x in input("m, n = ").split()]
# matr = [ [int(x) for x in input(f"linia {i}: ").split()] for i in range(m)]
# # print(matr)
#
# for linie in matr:
#     print(*linie)
#
# # print(*matr, sep = "\n")
#
# L_max = [max(linie) for linie in matr]
# print(L_max)


## Problema 4
"""
Se citesc m, n și o matrice cu m linii și n coloane, 
elementele unei linii fiind date pe o linie 
(elementele unei linii date pe o linie separate cu spațiu). 
Se citește în plus un număr natural k. 
Să se insereze o linie nouă cu toate elementele 0 
între liniile k și k+1 ale matricei.
"""

# with open("pb4.in", "r") as f:
#     m, n = [int(x) for x in f.readline().split()]
#     matr = [[int(x) for x in linie.split()] for linie in f]
#     print(matr)
#
# # ## Varianta 1
# # k = int(input("k= "))
# # matr[k + 1:k + 1] = [[0] * len(matr[0])]
# # print(matr)
#
# ##Varianta 2
# k = int(input("k= "))
# matr.insert(k+1, [0]*n)
# print(matr)
#
# with open("pb4.out", "w") as g:
#     # g.writelines([" ".join([str(x) for x in linie]) + '\n' for linie in matr ])
#
#     g.write("\n".join([" ".join([str(x) for x in linie]) for linie in matr]))


## Problema 5
"""
Se consideră tabloul bidimensional cu m linii şi n coloane, 
care conţine doar valorile {0,1,2}. Să se determine 
câte linii au produsul elementelor maxim (folosind și comprehensiune) 
"""

# f = open("pb5.in")
# matr = [[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# f.close()
#
# print(eval(f"{3}*{4}*{2}"))
#
# L_produs = [eval("*".join([str(x) for x in linie]))for linie in matr]
# print(L_produs)
# rez = L_produs.count(max(L_produs))
# print(rez)


## Problema 7
"""
Matricea transpusa (folosind comprehension)
"""

# f = open("pb7.in")
# matr = [[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# f.close()
#
# nr_linii = len(matr)
# nr_coloane = len(matr[0])
#
# transpusa = [[matr[i][j] for i in range(nr_linii)] for j in range(nr_coloane)]
# print(*transpusa, sep="\n")



# # OBSERVATIE
# L = [1, 2, 3, 4, 5, 6]
# # for x in L:
# #     if x % 2 == 0:
# #         x = -x ## NU se modifica lista
# # print(L)
#
# for i in range(len(L)):
#     if L[i] % 2 == 0 :
#         L[i] = -L[i]
# print(L)



# ## Problema 6
# """
# Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii
# fiind date pe o linie separate cu spațiu. Se citește în plus un număr natural k.
# Să se permute fiecare linie a matricei circular la dreapta cu k poziții
# (Echivalent: Să se permute coloanele matricei circular spre dreapta cu k poziții)
# """
#
# f = open("pb7.in")
# matr = [[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# f.close()
# nr_coloane = len(matr[0])
#
# k = int(input("k= "))
# k = k % nr_coloane
#
# # L = [ 1,2,3,4,5,6,7,8] k=2 -> [7,8,1,2,3,4,5,6]
# matr2 = [ linie[-k:] + linie[:-k] for linie in matr]
# print(*matr2, sep='\n')


## Problema 8

## Să se determine numărul de valori pare din matrice (folosind și comprehensiune)

# with open("pb4.in", "r") as f:
#     m, n = [int(x) for x in f.readline().split()]
#     matr = [[int(x) for x in linie.split()] for linie in f]
#     print(matr)
#
# L_pare = [x for linie in matr for x in linie if x % 2 == 0]
#
# print(L_pare)
# print(f"matricea contine {len(L_pare)} numere pare, suma lor este {sum(L_pare)}")


## Problema 9

## Să se determine pentru fiecare linie, cea mai mică valoare care se poate obține
# adunând elementele de pe linie, cu excepția unuia. (folosind și comprehensiune)

# with open("pb4.in", "r") as f:
#     m, n = [int(x) for x in f.readline().split()]
#     matr = [[int(x) for x in linie.split()] for linie in f]
#     print(matr)
#
# L_sume = [sum(linie) - max(linie) for linie in matr ]
# print(L_sume)


## PB 10-final => TEMA

