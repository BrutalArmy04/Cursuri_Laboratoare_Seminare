## Laborator 5, VI 1 noi, ora 14-16
#
# ##problema 1
# ##Varianta 1
# f=open('pb1.in',"r")
# text=f.read()
# f.close()
#
# g=open("pb1.out",'w')
# g.write(text)
# g.close()


##varianta 2
# f=open("pb1.in",'r')
# g=open('pb1.out','w')
# while True:
#     linie=f.readline()
#     if linie=='':
#         f.close()
#         g.close()
#         break
#     g.write(linie)


# ##varianta 3
# f=open('pb1.in','r')
# L_linii=f.readlines()
# f.close()
#
# with open('pb1.out','w') as g:
#     # g.writelines(L_linii)
#     g.write(''.join(L_linii))


# ## Problema 2
# f = open("pb2_test.in",'r')
# g = open("pb2_test.out",'w')
# nota = 1
# for linie in f:
#     calcul,rez = linie.split("=")
#     a,b = calcul.split("*")
#     a,b,rez = int(a),int(b),int(rez)
#     if a * b == rez:
#         nota = nota + 1
#         g.write(f"{linie.strip()} Corect\n")
#     else:
#         g.write(f"{linie.strip()} Gresit {a*b}\n")
# g.write(f"Nota {nota}")


## Problema 3
"""
Se citesc m, n și o matrice cu m linii și n coloane,
elementele unei linii fiind date pe o linie
(elementele unei linii date pe o linie separate cu spațiu).
Să se creeze o listă cu maximele de pe fiecare linie
(folosind și comprehensiune)
"""

# m, n = [int(x) for x in input("m, n= ").split()]
# Matr = [[int(x) for x in input(f"Linia {i}: ").split()]
#         for i in range(m)]
# # print(Matr)
#
# # for linie in Matr:
# #     print(linie)
#
# # for linie in Matr:
# #     for x in linie:
# #         print(x, end=' ')
# #     print()
#
# for linie in Matr:
#     print(*linie)
#
# print()
#
# L_maxime = [max(linie) for linie in Matr]
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
# m,n = [int(x) for x in f.readline().split()]
# Matr = [[int(x) for x in linie.split()]for linie in f]
# f.close()
# print(*Matr, sep="\n")
# print()
#
# k = int(input("k= "))
# # ## V1
# # Matr.insert(k+1, [0]*n)
#
# ## V2
# Matr[k+1:k+1] = [[0]*n]
# # print(*Matr, sep="\n")
#
# g = open("pb4.out", "w")
# ##V1
# # g.writelines([" ".join([str(x) for x in linie]) +"\n"
# #               for linie in Matr])
# g.write("\n".join([" ".join([str(x) for x in linie])
#               for linie in Matr]))
# g.close()


## Problema 5
"""
Se consideră tabloul bidimensional cu m linii şi n coloane, 
care conţine doar valorile {0,1,2}. Să se determine 
câte linii au produsul elementelor maxim (folosind și comprehensiune) 
"""

# f = open("pb5.in")
# matr = [[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# print()
# f.close()
#
#
# # print(eval(f"{3}*{4}*{2}"))
#
# L_produse=[eval("*".join([str(x) for x in linie ]))
#            for linie in matr]
# print(L_produse)
# r=L_produse.count(max(L_produse))
# print(r)


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
# nr_col = len(matr[0])
#
# matr_trans = [ [matr[i][j]  for i in range(nr_linii)]
#                for j in range(nr_col)   ]
# print(*matr_trans, sep="\n")



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
