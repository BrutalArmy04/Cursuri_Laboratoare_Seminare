### Laborator 1 - Grupa 132.1 - MI 2 oct
# # Problema 1 

# x = int(input("Introdu un numar: "))
# y = int(input("Introdu un alt numar: "))

# sum = x +  y
# prod = x * y

# print(sum, prod)
# print(sum, prod, sep = ",")

# print(sum, prod, sep = "\n")

# print(f"Suma numerelor  '{x }' si \" {y} \" este {x + y}, iar produsul este {x * y}.")
# print("Suma numerelor {x} si {y} este {x + y}, iar produsul este {x * y}.")


# ################################################
# # Problema 2
# # numere=input("Introduceti 3 numere: ").split()
# # print(numere)
# a,b,c=input("Introduceti 3 numere: ").split()
# print(a,b,c)
# a,b,c=int(a), int(b), int(c)
# if 0<=a<24 and 0<=b<60 and 0<=c<60: 
#     print(f"{a:02d}:{b:02d}:{c:02d}")
# else:
#     print("Numerele introduse nu pot fi ore, minute, secunde.")
    



################################################
# # Problema 3
# z=int(input("Zi= "))
# l=int(input("Luna= "))
# a=int(input("An= "))
# ok=True
# if l in [1,3,5,7,8,10,12]:
#     #luna cu 31 zile
#     if 1<=z<=30:
#         z=z+1
#     elif z==31:
#         if l!=12:
#             z=1
#             l+=1
#         else:
#             z=1
#             l=1
#             a=a+1
#     else:
#         print("Zi incorecta")
#         ok=False
    
# elif l in [4,6,9,11]:
#     #luna cu 30 zile
#     if 1<=z<=29:
#         z+=1
#     elif z==30:
#         z=1
#         l+=1
#     else:
#         print("Zi incorecta")
#         ok=False
    
# elif l==2:
#     #febriuarie
#     if a%4==0 and a%100!=0 or a%400==0:
#         #an bisect, max 29 zile
#         if 1<=z<=28:
#             z+=1
#         elif z==29:
#             z=1
#             l+=1
#         else:
#             print("Zi incorecta")
#             ok=False
#     else:
#         #an nu este bisect, max 28 zile
#         if 1<=z<=27:
#             z+=1
#         elif z==28:
#             z=1
#             l+=1
#         else:
#             print("Zi incorecta")
#             ok=False
        
# else:
#     print("Luna incorecta")
#     ok=False

# if ok==True:
#     print(f"{z:02d}.{l:02d}.{a:04d}")
# else:
#     print("Data incorecta")


# {x:.3f}

