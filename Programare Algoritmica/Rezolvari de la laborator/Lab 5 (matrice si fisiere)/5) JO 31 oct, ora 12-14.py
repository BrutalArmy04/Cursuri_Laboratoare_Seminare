## Laborator 5, JO 31 oct, ora 12-14

## Problema 1

# ##Varianta 1
#
# f=open("pb1.in","r")
# text=f.read()
# f.close()
#
# g=open("pb1.out","w")
# g.write(text)
# g.close()


# ##Varianta 2
#
# f=open("pb1.in")
# g=open("pb1.out","w")
#
# while True:
#     linie = f.readline()
#     if linie == "":
#         f.close()
#         g.close()
#         break
#     g.write(linie)

# ##Varianta 3
#
# with open("pb1.in") as f:
#     L_linii=f.readlines()
# with open("pb1.out","w") as g:
#     # g.writelines(L_linii)
#     g.write("".join(L_linii))


# ## Problema 2
# f = open("pb2_test.in")
# g = open("pb2_test.out", "w")
# nota=1
# for linie in f:
#     aux, rez = linie.split("=")
#     a, b = aux.split("*")
#     a, b, rez = int(a), int(b), int(rez)
#     if a*b==rez:
#         nota+=1
#         g.write(f"{linie.strip()} Corect\n")
#     else:
#         g.write(f"{linie.strip()} Gresit {a*b}\n")
# g.write(f"nota={nota}")


## Problema 3
"""
Se citesc m, n și o matrice cu m linii și n coloane,
elementele unei linii fiind date pe o linie
(elementele unei linii date pe o linie separate cu spațiu).
Să se creeze o listă cu maximele de pe fiecare linie
(folosind și comprehensiune)
"""

# m,n = [int(x) for x in input("m,n: ").split()]
# matr = [[int(x) for x in input(f"linia {i}: ").split()] for i in range(m) ]
# # print(matr)
#
# for linie in matr:
#     print(*linie)
#
# # print(*matr)
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

# f = open("pb4.in")
# m, n = [int(x) for x in f.readline().split()]
# matr = [[int(x) for x in linie.split()] for linie in f]
#
# print(matr)
# f.close()
#
# k = int(input("k = "))

# ## varianta 1
#
# matr[k + 1:k + 1] = [[0]*n]
# print(*matr, sep='\n')


# ## varianta 2
#
# matr.insert(k + 1, [0]*n)
# # print(*matr, sep='\n')
#
#
# with open("pb4.out", 'w') as g:
#     # g.writelines([ ' '.join([str(x) for x in linie])+"\n" for linie in matr])
#     g.write('\n'.join([ ' '.join([str(x) for x in linie]) for linie in matr]))


## Observatie la initializare matrice...
# M =[["a" ]*3 for i in range(2)]
# M[1][0] = "b"
# print(M)


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
# # L = [2,1,2,2,0,1]
# # produs = 1
# # rez = [produs := produs*x for x in L] ## := operatorul morsa / walrus
# # print(rez)
#
#
# # print(eval(f"{3}*{4}*{2}"))
# L_produse=[eval("*".join([str(x) for x in linie])) for linie in matr]
# print(L_produse)
#
# rez=L_produse.count(max(L_produse))
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
#     if L[i] % 2 == 0:
#         L[i] = -L[i] ## se modifica lista
# print(L)


## PB 6, 8-final => TEMA

