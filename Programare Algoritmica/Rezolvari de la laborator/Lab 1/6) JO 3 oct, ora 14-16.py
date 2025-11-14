### Laborator 1 - Grupa 134.2 - JO 3 oct
# # Problema 1 

# x = int(input('x = ')) 
# y = int(input('y = '))
# suma = x + y
# prod = x*y
# print(suma, prod)
# print(suma, prod, sep = ',')

# print(suma, prod, sep = '\n')

# print(f'suma numerelor {x} si {y} este {x + y}, iar produsul este {x*y}')
# print('suma numerelor {x} si {y} este {x + y}, iar produsul este {x*y}')



# ###############
# # Problema 2

# a, b, c = input('introduceti 3 numere: ').split()
# #print(a, b, c)
# #print(type(a))
# a, b, c =int(a), int(b), int(c)

# if 0<=a<24 and 0<=b<60 and 0<=c<60:
#     print(f'{a:02d}:{b:02d}:{c:02d}')
# else:
#     print("Date invalide")
    
    

# #########################
# # Problema 3
# z = int(input("zi = "))
# l = int(input("luna = "))
# a = int(input("an = "))
# ok = True

# if l in [1, 3, 5, 7, 8, 10, 12]:
#     #31 de zile
#     if 1<=z<31:
#         z+=1
#     elif z == 31:
#         z=1
#         if l == 12:
#             l = 1
#             a+=1
#         else:
#             l+=1
#     else:
#         ok = False
        
# elif l in [4, 6, 9, 11]:
#     #30 de zile
#     if 1<=z<30:
#         z+=1
#     elif z == 30:
#         z=1
#         l+=1
#     else:
#         ok = False
        
# elif l == 2:
#     #februarie
#     if a%4==0 and a%100!=0 or a%400==0:
#         #an bisect 29 de zile
#         if 1<=z<29:
#             z+=1
#         elif z == 29:
#             z=1
#             l+=1
#         else:
#             ok = False
#     else:
#         #anul nu e bisect 28 de zile
#         if 1<=z<28:
#             z+=1
#         elif z == 28:
#             z=1
#             l+=1
#         else:
#             ok = False
# else:
#     ok = False
    
# if ok == False:
#     print("Date incorecte")
# else:
#     print(f"{z:02d}.{l:02d}.{a:04d}")



# nr = 34.2327325436
# print(f"{nr:.3f}")
