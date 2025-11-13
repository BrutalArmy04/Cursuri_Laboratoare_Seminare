# Laborator 3, JO 17 oct 2024, ora 12-14

## Problema 2

# s=input("sir=")
# for i in range((len(s)+1)//2):
#     print(s[i:len(s)-i].center(len(s),"*"))


# # Problema 3
# # rezolvare cu find()
# s = "abccabcababcc"
# t = "abcd"
#
# poz = s.find(t)
# if poz == -1:
#     print(f"\"{t}\" nu s-a gasit deloc in '{s}'")
# else:
#     while poz != -1:
#         print(f"{poz}, ",end="")
# #       print(poz, end=", ")
#         poz=s.find(t,poz+len(t))

# # # rezolvare cu index()
# s = "abccabcababcc"
# t = "abc"
# poz = -len(t)
# gasit = False

# while True:
#     try:
#         poz = s.index(t, poz + len(t))
#         print(poz, end=", ")
#         gasit=True
#     except ValueError:
#         print("Gata cautarea.")
#         break
# if not gasit:
#     print(f"\"{t}\" nu s-a gasit deloc in '{s}'")


# ## Problema 4
# prop = "Problemele cu siruri de caracteger nu sunt ggerle!"
# t = "ger"
# s = "re"
#
# #a)
# prop2 = prop.replace(t, s)
# print(prop2)
#
# #b)
# nrInlocuiri = int(input("numarul de inlocuiri: "))
# nrAparitii = prop.count(t)
#
# prop3 = prop.replace(t, s, nrInlocuiri)
# print(prop3)
# if nrInlocuiri < nrAparitii:
#     print(f"sirul avea prea multe greseli, au fost inlocuite doar {nrInlocuiri}")
# else:
#     print("au fost corectate toate greselile")


## Problema 5
# # # punctul a)
# prop="Mancare Ana are mere si mancare sau are"
# s="are"
# t="VREA"
# poz = prop.find(s)
# while poz != -1:
#     if (poz == 0 or prop[poz-1]==" ") \
#         and (poz+len(s) == len(prop) or prop[poz+len(s)]==" "):
#         prop = prop[:poz] + t + prop[poz+len(s):]
#     poz = prop.find(s,poz+len(t))
# print(prop)


#punctul b)
# prop="Mancare Ana .!are mere si mancare!? sau are?!."
# s="are"
# t="VREA"
#
# poz = prop.find(s)
# while poz != -1:
#     if (poz == 0 or prop[poz-1] in " ?!.;:,") \
#         and (poz+len(s) == len(prop) or prop[poz+len(s)] in " ?!.;:,"):
#         prop = prop[:poz] + t + prop[poz+len(s):]
#     poz = prop.find(s,poz+len(t))
# print(prop)


# ## Problema 6
# print(ord("A"))
# print(chr(65))
# 
# for x in text:
#     if x.isalpha():
#         pass
# 
# ## Problema 7
# for x in text:
#     if x in "aeiouAEIOU":
#         # vocala
#         pass
#     if x.isalpha() and x not in "aeiouAEIOU":
#         # consoana
#         pass
# 
# # apa => apapapa => ApA
# 
# ## Problema 8
# L_cuv = prop.split()
# for cuv in L_cuv:
#     if x.isdigit():
#         pass
# 

