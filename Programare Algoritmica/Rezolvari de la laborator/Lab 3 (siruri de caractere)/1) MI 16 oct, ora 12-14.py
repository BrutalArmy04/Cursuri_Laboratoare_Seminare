# Laborator 3, MI 16 oct 2024, ora 12-14

# #Problema 2
# s = input("s= ")
# i = 0
# while s[i:len(s)-i]:
#     print(s[i:len(s)-i].center(len(s),"*"))
#     i += 1


##Problema 3
## rezolvare cu find()
# s = "abccabcababcc"
# t="abc"
# poz=s.find(t,0)
# gasit=False
# while poz!=-1:
#     print(poz, end=", ")
#     poz=s.find(t,poz+len(t))
#     gasit=True
# if gasit==False:
#     print(f"'{t}' nu are nicio aparitie in \"{s}\" ")
#

## rezolvare cu index()
# s = "abccabcababcc"
# t = "abc"
# poz = -len(t)
# gasit = False
# while True:
#     try:
#         poz = s.index(t, poz + len(t))
#         print(poz, end=", ")
#         gasit = True
#     except ValueError:
#         print("gata cautarea")
#         break
# if gasit == False:
#     print(f"'{t}' nu are nicio aparitie in \"{s}\" ")


# # Problema 4
# prop = "Problemele cu siruri de caracteger nu sunt ggerle!"
# t = "ger"
# s = "re"
# ## a)
# prop2=prop.replace(t, s)
# print(prop2)
#
# ##b)
# p=int(input("nr inlocuiri: "))
# nrAparitii=prop.count(t)
# if p < nrAparitii:
#     prop3=prop.replace(t, s, p)
#     print(f"au fost inlocuite doar primele {p} aparitii")
# else:
#     prop3=prop.replace(t, s, p)
#     print("au fost inlocuite toate aparitiile")
#
# print(prop3)


# #problema 5
# #a)
# # prop="Ana are mere are pere si mai are banane are"
# # s="are"
# # t="MANANCA"
# # prop1 = (" " + prop + " ").replace(" " +  s + " ", f' {t} ')
# # print(prop1)

# #b)
# prop="Ana are mere, are. pere si mai ;are banane si mancare!"
# s="are"
# t="MANANCA"
# prop2=prop
# for x in ",.;!?:":
#     prop2=prop2.replace(x," ")
# prop2 = (" " + prop2 + " ").replace(" " +  s + " ", f' {t} ')
# print(prop2)



# ## Problema 6
# print(ord("A"))
# print(chr(65))
# 
# ## Problema 7
# for x in "blabliblu":
#     if x in "aeiouAEIOU":
#         pass
#     if x.isalpha() and x not in "aeiouAEIOU":
#         pass
# 
# ## problema 8
# L_cuv = prop.split()
# for cuv in L_cuv:
#     if cuv.isdigit():
#         pass

