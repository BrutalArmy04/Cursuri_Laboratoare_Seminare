# Laborator 3, JO 17 oct 2024, ora 10-12

## # Problema 2
# s = input("Sir de caractere: ")
#
# for i in range((len(s)+1)//2):
#     print(s[i:len(s)-i].center(len(s),"*"))

## Problema 3
## rezolvare cu find()
# s = "abccabcababcc"
# t = "abc"
#
# poz = s.find(t)
#
# if poz == -1:
#     print(f"Subsirul {t} nu are nicio aparitie in {s}")
#
# else:
#     while poz != -1:
#         print(poz, end=', ')
#         poz = s.find(t, poz+len(t))

## rezolvare cu index()
# s = "abccabcababcc"
# t = "abcd"
#
# poz = -len(t)
# gasit = False
#
# while True:
#     try:
#         poz = s.index(t, poz + len(t))
#         print(poz, end=', ')
#         gasit = True
#     except ValueError:
#         print("Gata Cautarea")
#         break
#
# if not gasit:
#     print(f"Subsirul {t} nu are nicio aparitie in {s}")


## Problema 4
# prop = "Problemele cu siruri de caracteger nu sunt ggerle!"
# t = "ger"
# s = "re"
# #a)
# prop2 = prop.replace(t,s)
# print(prop2)
# #b)
# n = int(input("Numar modificari: "))
# nr_Aparitii = prop.count(t)
# prop3 = prop.replace(t,s,n)
# print(prop3)
# if n < nr_Aparitii:
#     print(f"Sirul continea prea multe greseli. Au fost corectate doar primele {n}")
# else:
#     print("Au fost corectate toate greselile")


# # Problema 5
# # # punctul a)
# prop="Mancare Ana are mere si mancare sau are"
# s="are"
# t="VREA"
#
# poz = prop.find(s)
# if poz == -1:
#     print(f"Subsirul '{s}' nu se gaseste deloc in \"{prop}\" ")
# else:
#     while poz != -1:
#         if (poz == 0 or prop[poz-1]==' ') \
#             and (poz + len(s) == len(prop) or prop[poz+len(s)] == ' '):
#             prop = prop[:poz] + t + prop[poz+len(s):]
#         poz = prop.find(s, poz+len(t))
#     print(prop)


# ## Problema 6
# print(ord("A"))
# print(chr(65))
# for x in sir:
#     if x.isalpha():
#         if x.isupper():
#             pass
# 
# ## Problema 7
# for x in text:
#     if x in "aeiouAEIOU":
#         pass # vocala
#     if x.isalpha() and x not in "aeiouAEIOU":
#         pass # consoana
# 
# ## Problema 8
# L_cuv = prop.split()
# for cuv in L_cuv:
#     if cuv.isdigit():
#         pass
# 
