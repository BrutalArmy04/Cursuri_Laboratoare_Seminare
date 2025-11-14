## Laborator 5, VI 1 noi, ora 16-18

## Problema 1
## Varianta 1
# f = open("pb1.in","r")
# text = f.read()
# f.close()
#
# g = open("pb1.out","w")
# g.write(text)
# g.close()

## Varianta 2
# f = open("pb1.in","r")
# g = open("pb1.out","w")
#
# while True:
#     linie = f.readline()
#     if linie == "":
#         f.close()
#         g.close()
#         break
#     g.write(linie)

## Varianta 3
# f = open("pb1.in","r")
# L_linii = f.readlines()
# f.close()
#
# with open("pb1.out","w") as g:
#     #g.writelines(L_linii)
#     g.write("".join(L_linii))



# ## Problema 2
# fin = open("pb2_test.in")
# fout = open("pb2_test.out", "w")
# nota = 1
# for linie in fin:
#     aux, rez = linie.split("=")
#     rez = int(rez)
#     a, b = [int(x) for x in aux.split("*")]
#     if a * b == rez:
#         nota += 1
#         fout.write(f"{linie.strip()} Corect\n")
#     else:
#         fout.write(f"{linie.strip()} Gresit {a * b}\n")
# fout.write(f"Nota {nota}")
#
# # print("aababacccabbadddabcaaa".strip("ab"))



## Problema 3
"""
Se citesc m, n și o matrice cu m linii și n coloane,
elementele unei linii fiind date pe o linie
(elementele unei linii date pe o linie separate cu spațiu).
Să se creeze o listă cu maximele de pe fiecare linie
(folosind și comprehensiune)
"""
# m,n = [int(x) for x in input("m,n= ").split()]
# matr= [[int(x) for x in input(f"linia {i}: ").split()]
#        for i in range(m)]
# # print(matr)
#
# # for linie in matr :
# #     print(linie)
#
# # for linie in matr :
# #     for x in linie :
# #         print(x,end=" ")
# #     print()
#
# # print(*matr,sep="\n")
#
# for linie in matr :
#     print(*linie)
#
# L_maxime= [max(linie) for linie in matr]
# print(L_maxime)


## Problema 4
"""
Se citesc m, n și o matrice cu m linii și n coloane, 
elementele unei linii fiind date pe o linie 
(elementele unei linii date pe o linie separate cu spațiu). 
Se citește în plus un număr natural k. 
Să se insereze o linie nouă cu toate elementele 0 
între liniile k și k+1 ale matricei.
"""

# f = open("pb4.in", "r")
# m ,n = [int(x) for x in f.readline().split()]
#
# matrix = [[int(x) for x in linie.split()]for linie in f]
# f.close()
# print(*matrix, sep="\n")
# print()
#
# k = int(input("k= "))
#
# ## Varianta 1 (insert)
# # matrix.insert(k + 1, [0] * n)
#
# ## Varianta 2 (feliere)
# matrix[k+1:k+1] = [[0] * n]
# print(*matrix, sep="\n")
#
# g = open("pb4.out", "w")
# #Varianta 1
# #
# # g.writelines([" ".join([str(x) for x in linie]) + "\n"
# #               for linie in matrix])
#
# #Varianta 2
# g.write("\n".join([" ".join([str(x) for x in linie])
#               for linie in matrix]))


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
# # print(eval(f"{3}*{4}*{2}"))
#
# L_produse = [eval("*".join([str(x) for x in linie]))
#              for linie in matr]
# print(L_produse)
#
# rez = L_produse.count(max(L_produse))
# print(rez)


## Problema 7
"""
Matricea transpusa (folosind comprehension)
"""

# f = open("pb7.in")
# matr = [[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# print()
# f.close()
#
# nr_linii = len(matr)
# nr_coloane = len(matr[0])
#
# transpusa = [[matr[i][j] for i in range(nr_linii)]
#              for j in range(nr_coloane)   ]
#
# print(*transpusa, sep="\n")


#  # OBSERVATIE
# L = [1, 2, 3, 4, 5, 6]
# # for x in L:
# #     if x % 2 == 0:
# #         x = -x ## NU se modifica lista
# # print(L)
# #
# for i in range(len(L)):
#     if L[i] % 2 == 0 :
#         L[i] = -L[i]
# print(L)


## PB 6, 8-final => TEMA

