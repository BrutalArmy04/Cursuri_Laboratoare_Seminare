# Laborator 3, MI 16 oct 2024, ora 14-16

# # Problema 2
# s = input("Introdu un sir de caractere: ")
#
# for i in range(len(s) // 2 + len(s) % 2):
#     print(s[i: len(s) - i].center(len(s), "*"))


# Problem 3

# #rezolvare cu find()
# s = "abccabcababcc"
# t = "abc"
#
# poz = s.find(t)
#
# if poz==-1:
#     print(f"Sirul '{t}' nu se regaseste deloc in \"{s}\" ")
#
# while poz!=-1:
#     print(poz, end=', ')
#     poz = s.find(t, poz+len(t))


# # rezolvare cu index()
#
# s = "abccabcababcc"
# t = "abc"
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
#         print("Gata cautarea")
#         break
# if gasit == False:
#     print(f"Sirul '{t}' nu se regaseste deloc in \"{s}\" ")


# # Problema 4
# # a)
# prop = "Problemele cu siruri de caracteger nu sunt ggerle!"
# t = "ger"
# s = "re"
# prop2 = prop.replace(t, s)
# print(prop2)
#
# #b)
# p=int(input("numar inlocuiri: "))
# nr_aparitii = prop.count(t)
# prop3=prop.replace(t,s,p)
# print(prop3)
#
# if nr_aparitii>p:
#     print(f"textul contine prea multe greseli, au fost inlocuite doar primele {p} greseli")
# else:
#     print("Au fost inlocuite toate greselile")


# Problema 5

# # punctul a)
# prop="Mancare Ana are mere si mancare sau are"
# s="are"
# t="VREA"
#
# poz=prop.find(s)
# while poz != -1:
#     #verificam ca s nu e subcuvant
#     if (poz == 0 or prop[poz-1]== " ") \
#         and (poz + len(s) == len(prop) or prop[poz+len(s)] == " "):
#         prop = prop[:poz] + t + prop[poz + len(s):]
#
#     poz = prop.find(s,poz+len(t))
#
# print(prop)

# # punctul b)
# prop="Mancare, Ana. are? mere si mancare; sau !are"
# s="are"
# t="VREA"
#
# poz=prop.find(s)
# while poz != -1:
#     #verificam ca s nu e subcuvant
#     if (poz == 0 or prop[poz-1] in ",.?!;: ") \
#         and (poz + len(s) == len(prop) or prop[poz+len(s)] in ",.?!;: "):
#         prop = prop[:poz] + t + prop[poz + len(s):]
#
#     poz = prop.find(s,poz+len(t))
#
# print(prop)


# ## Problema 6
# print(ord("A"))
# print(chr(65))
# 
# 
# ## Problema 7
# 
# for x in "blablubli":
#     if x in "aeiouAEIOU":
#         pass
#     if x.isalpha() and x not in "aeiouAEIOU":
#         pass
# 
# # Problema 8 
# L_cuv = prop.split()
# for cuv in L_cuv:
#     if cuv.isdigit():
#         pass

