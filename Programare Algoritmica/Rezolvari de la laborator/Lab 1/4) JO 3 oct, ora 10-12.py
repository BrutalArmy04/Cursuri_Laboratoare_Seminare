###Laborator 1 - Grupa 134.1 - JO 3 oct

# # Problema 1 

# x = int(input('x = ')) 
# y = int(input('y = '))

# sum = x + y
# prod = x * y

# print(sum, prod)
# print(sum, prod, sep=',')

# print(sum, prod, sep='\n')
# print(sum)
# print(prod)


# print(f'suma numerelor {x} si {y} este {x + y}, iar produsul este {x * y}')
# print('suma numerelor {x} si {y} este {x + y}, iar produsul este {x * y}')


# ##############################3
# # Problema 2

# a,b,c=input("introduceti 3 numere: ").split()
# a,b,c=int(a),int(b),int(c)
# if 0<=a<24 and 0<=b<60 and 0<=c<60 :
#     print(f'{a:02d}:{b:02d}:{c:02d}')
# else: 
#     print("numerele nu pot reprezenta ore,minute si secunde")
    

##########################
# # Problema 3

# z= int(input('Ziua = '))
# l= int(input('Luna ='))
# a= int(input('An = '))
# ok=True
# if l in [1,3,5,7,8,10,12] :
#     #31 de zile
#     if 1<=z<=30: 
#         z+=1
#     elif z==31:
#         z=1
#         if l==12:
#             a+=1
#             l=1
#         else :
#             l+=1
#     else:
#         ok=False
        
# elif l in [4,6,9,11]:
#     #30 de zile
#     if 1<=z<=29: 
#         z+=1
#     elif z==30:
#         z=1
#         l+=1
#     else:
#         ok=False
        
# elif l==2 :
#     #februarie
#     if a%4==0 and a%100!=0 or a%400==0 :
#         #an bisect 29 zile
#         if 1<=z<=28 :
#             z+=1
#         elif z==29 :
#             z=1
#             l+=1
#         else:
#             ok=False
#     else:
#         #an nu e bisect 28 zile
#         if 1<=z<=27 :
#             z+=1
#         elif z==28 :
#             z=1
#             l+=1
#         else:
#             ok=False
            
# else :
#     ok=False
    
# if ok==False :
#     print("Nu ati introdus o data corecta.")
# else :
#     print(f'{z:02d}.{l:02d}.{a:04d}')
    

# {nr:.3f}




