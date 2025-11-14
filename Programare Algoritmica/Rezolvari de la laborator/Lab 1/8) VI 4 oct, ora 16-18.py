### Laborator 1 - Grupa 131.2 - VI 4 oct

# # Problema 1 
# a = int(input("Primul numar:"))
# b = int(input("Al doilea numar:"))
# suma = a + b
# produs = a * b   
# print(suma,produs)
# print(suma,produs, sep = ',')

# print(suma,produs, sep='\n')

# print(suma)
# print(produs)

# print(f"Suma numerelor {a} si {b} este {a+b}, iar produsul este {a*b}")
# print("Suma numerelor {a} si {b} este {a+b}, iar produsul este {a*b}")



# ##################

# # Problema 2 
# a,b,c = input("Introduceti trei numere: ").split()

# print(a,b,c)
# print(type(a))

# a,b,c = int(a), int(b), int(c)

# if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 59:
#     print(f"{a:02d}:{b:02d}:{c:02d}")
# else:
#     print("datele sunt incorecte")



# #####################
# # Problema 3 

# z=int(input("Zi= "))
# l=int(input("Luna= "))
# a=int(input("An= "))
# ok=True
# if l in [1,3,5,7,8,10,12]:
#     #31 de zile
#     if 1<=z<=30:
#         z=z+1
#     elif z==31:
#         if l==12:
#             z=1
#             l=1
#             a+=1
#         else:
#             z=1
#             l=l+1
#     else:
#         ok=False
    
# elif l in [4,6,9,11]:
#     #30 de zile
#     if 1<=z<=29:
#         z=z+1
#     elif z==30:
#         z=1
#         l=l+1
#     else:
#         ok=False
    
# elif l==2:
#     #februarie
#     if a%4==0 and a%100!=0 or a%400==0:
#         #an bisect,29 de zile
#         if 1<=z<=28:
#             z=z+1
#         elif z==29:
#             z=1
#             l=l+1
#         else:
#             ok=False
#     else:
#         #anul nu e bisect, 28 zile
#         if 1<=z<=27:
#             z=z+1
#         elif z==28:
#             z=1
#             l=l+1
#         else:
#             ok=False
# else:
#     ok=False


# if ok==False:
#     print("data incorecta")
# else:
#     print(f"{z:02d}.{l:02d}.{a:04d}")
    


# nr = 23.123724235
# print(f"{nr:.3f}")
    
