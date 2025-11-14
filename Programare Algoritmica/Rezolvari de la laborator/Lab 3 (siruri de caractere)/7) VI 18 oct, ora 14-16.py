# Laborator 3, VI 18 oct 2024, ora 14-16

# # Problema 2
#
# # print("anaana".center(20, "*"))
#
# s = input("Un cuvant s: ")
# p = 0
# while p < (len(s)+1) // 2:
#     print(s[p:len(s)-p].center(len(s), "*"))
#     p = p+1


# Problema 3

# # rezolvare cu find()
# s = "abccabcababcc"
# t = "abc"
#
# poz = s.find(t)
# if poz == -1:
#     print(f"Subsirul '{t}' nu se gaseste deloc in \"{s}\".")
# else:
#     while poz != -1:
#         print(poz, end=', ')
#         poz=s.find(t, poz+len(t))

# # rezolvare cu index()
# s = "abccabcababcc"
# t = "abcd"
# poz = - len(t)
# gasit = False
# while True:
#     try:
#         poz = s.index(t, poz + len(t))
#         print(poz, end=', ')
#         gasit = True
#     except ValueError:
#         print("Gata cautarea.")
#         break
# if not gasit:
#     print(f"Subsirul '{t}' nu se gaseste deloc in \"{s}\".")


# # Problema 4
# prop = "Problemele cu siruri de caracteger nu sunt ggerle!"
# t = "ger"
# s = "re"
#
# # a)
# prop2=prop.replace(t, s)
# print(prop2)
#
# # b)
# nr_inlocuiri=int(input("Introduceti numarul de inlocuiri: "))
# nr_aparitii=prop.count(t)
# prop3=prop.replace(t, s, nr_inlocuiri)
# print(prop3)
# if nr_aparitii>nr_inlocuiri:
#     print(f"Sirul '{prop}' contine prea multe greseli. Au fost corectare primele {nr_inlocuiri} greseli.")
# else:
#     print("Toate greselile au fost corectate.")


# Problema 5

# # punctul a)
# prop = "Mancare Ana are mere si mancare sau are"
# s = "are"
# t = "VREA"
#
# poz = prop.find(s)
# while poz != -1:
#     if (poz == 0 or prop[poz-1] == ' ') \
#         and (poz+len(s) == len(prop) or prop[poz+len(s)] == ' '):
#         prop = prop[:poz] + t + prop[poz+len(s):]
#         poz = prop.find(s,poz+len(t))
#     else:
#         poz = prop.find(s, poz + len(s))
# print(prop)


# #punctul b)
# prop = "Mancare Ana, ;are. mere si mancare sau ?are,"
# s = "are"
# t = "VREA"
#
# poz = prop.find(s)
# while poz != -1:
#     if (poz == 0 or prop[poz-1] in ' .,;:?!') \
#         and (poz+len(s) == len(prop) or prop[poz+len(s)] in ' .,;:?!'):
#         prop = prop[:poz] + t + prop[poz+len(s):]
#         poz = prop.find(s,poz+len(t))
#     else:
#         poz = prop.find(s, poz + len(s))
# print(prop)



# # Problema 6
# print(ord("A"))
# print(chr(65))
#
# for x in text:
#     if x.isalpha():
#         if x.isupper():
#             #litera mare
#         elif x.islower():
#             #litera mica

# # Problema 7
#
# for x in text:
#     if x in "aeiouAEIOU":
#         # vocala
#     elif x.isalpha() and x not in "aeiouAEIOU":
#         # consoana
#
# apa => apapapa => ApA

# ## Problema 8
# 
# L_cuv = text.split()
# for cuv in L_cuv:
#     if cuv.isdigit():
#         pass
