## Laborator 5, MI 30 oct, ora 12-14

## Problema 1
# #open-functie, close-metoda
# f=open("pb1.in", 'r')
# text=f.read()
# f.close()
#
# g=open("pb1.out", 'w')
# g.write(text)
# g.close()


# f=open("pb1.in", 'r')
# g=open("pb1.out", 'w')
# text=f.readline()
# while text!="":
#     g.write(text)
#     text=f.readline()
# g.write(text)
# f.close()
# g.close()

# f=open("pb1.in", 'r')
# L_linii=f.readlines()
# f.close()
# g=open("pb1.out", 'w')
# g.writelines(L_linii)
# g.close()


# ## Problema 2
# nota=1
# f=open("pb2_test.in", 'r')
# g=open("pb2_test.out", 'w')
# for linie in f:
#     aux,rez=linie.split('=')
#     a,b=aux.split('*')
#     a,b,rez=int(a), int(b), int(rez)
#     if a*b==rez:
#         nota+=1
#         g.write(f"{linie.strip()} Corect\n")
#     else:
#         g.write(f"{linie.strip()} Gresit {a*b}\n")
# g.write(f"nota este {nota}")
# f.close()
# g.close()


## Problema 3
"""
Se citesc m, n și o matrice cu m linii și n coloane,
elementele unei linii fiind date pe o linie
(elementele unei linii date pe o linie separate cu spațiu).
Să se creeze o listă cu maximele de pe fiecare linie
(folosind și comprehensiune)
"""

# m,n = [int(x) for x in input('m si n = ').split()]
# matr = [ [int(x) for x in input(f"linia {i}:").split()  ] for i in range(m)]
# # for linie in matr:
# #     print(*linie)
#
# # print(*matr, sep='\n')
#
# L_maxime = [max(linie)  for linie in matr]
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
# f=open("pb4.in")
# m,n=[int(x) for x in f.readline().split()]
# matr=[[int(x) for x in linie.split()] for linie in f]
# # print(matr)
# f.close()
#
# k=int(input("k = "))
# # matr.insert(k+1,[0]*n)
#
# matr[k+1:k+1] = [[0]*n]
#
# # print(matr)
#
# g=open("pb4.out", 'w')
# # g.writelines([" ".join([str(x) for x in linie ])+"\n" for linie in matr])
#
# g.write("\n".join([" ".join([str(x) for x in linie ]) for linie in matr]))
# g.close()


## Problema 5
"""
Se consideră tabloul bidimensional cu m linii şi n coloane, 
care conţine doar valorile {0,1,2}. Să se determine 
câte linii au produsul elementelor maxim (folosind și comprehensiune) 
"""
# f=open("pb5.in")
# matr=[[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# f.close()
#
# # print(eval(f"{3}*{4}*{2}"))
#
# L_produse=[eval("*".join([str(x) for x in linie])) for linie in matr]
# print(L_produse)
#
# nrlinii=L_produse.count(max(L_produse))
# print(nrlinii)


## Problema 6 => TEMA...
"""
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii 
fiind date pe o linie separate cu spațiu. Se citește în plus un număr natural k. 
Să se permute fiecare linie a matricei circular la dreapta cu k poziții 
(Echivalent: Să se permute coloanele matricei circular spre dreapta cu k poziții)
"""

# f = open("pb7.in")
# matr = [[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# f.close()
# nr_coloane = len(matr[0])
#
# k = int(input("k= "))
# k = k % nr_coloane

## ... TO DO TEMA


## OBSERVATIE
# L=[1,2,3,4,5,6]
# # for x in L :
# #     if x%2==0:
# #         x=x*(-1) ## NU se modifica lista
#
# for i in range(len(L)):
#     if L[i] % 2 == 0:
#         L[i]=-L[i] ## se modifica lista
#
# print(L)


## Problema 7
"""
Matricea transpusa (folosind comprehension)
"""

# f=open("pb7.in")
# matr=[[int(x) for x in linie.split()] for linie in f]
# print(*matr, sep="\n")
# f.close()
#
# nr_linii = len(matr)
# nr_coloane = len(matr[0])
#
# transpusa = [ [matr[i][j] for i in range(nr_linii)] for j in range(nr_coloane)]
# print()
# print(*transpusa, sep="\n")


## PB 6, 8-final => TEMA
