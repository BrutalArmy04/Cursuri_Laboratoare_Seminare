### Laborator 1 - Grupa 133.1 - MI 2 oct
# # Problema 1 
# x=int(input('x= '))
# y=int(input('y= '))
# suma=x+y
# produs=x*y

# print(suma, produs)
# print(suma, produs, sep=',')

# print(suma, produs, sep='\n')

# print(f'suma numerelor {x} si {y} este {x+y}, iar produsul este {x*y} ')
# print('suma numerelor {x} si {y} este {x+y}, iar produsul este {x*y} ')



# ####################################3
# # Problema 2  
# # numere = input('trei numere: ').split()
# # print(numere)

# a,b,c = input('trei numere: ').split()
# print(a,b,c)
# a,b,c = int(a), int(b), int(c)

# if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 59:
#     print(f"{a:02d} : {b:02d} : {c:02d}")
# else:
#     print("Data incorecta")
    
### n = 5
### x = 0 if n % 2 == 0 else 7
### print(x)



####################################3
# # Problema 3 

# z=int(input("z= "))
# l=int(input("l= "))
# a=int(input("a= "))
# ok=True
# if l in [1,3,5,7,8,10,12]:
#     #luna cu 31 de zile 
#     if 1<=z<=30:
#         z+=1
#     elif z==31:
#         if l==12:
#             a+=1
#         z=1
#         l=l%12+1
#     else:
#         ok=False

# elif l in [4,6,9,11]:
#     #luna cu 30 de zile 
#     if 1<=z<=29:
#         z+=1
#     elif z==30:
#         z=1
#         l+=1
#     else: 
#         ok=False
        
# elif l==2:
#     #februarie
#     if a%4==0 and a%100!=0 or a%400==0:
#         #an bisect, 29 zile
#         if 1<=z<29: 
#             z+=1
#         elif z==29:
#             z=1
#             l+=1
#         else: 
#             ok=False
#     else: 
#         #anul nu e bisect, 28 zile
#         if 1<=z<28: 
#             z+=1
#         elif z==28:
#             z=1
#             l+=1
#         else: 
#             ok=False
        
# else: 
#     print("Luna incorecta")

# if ok==True:
#     print(f'{z:02d}.{l:02d}.{a:04d}')
# else: 
#     print("date incorecte")


# nr = 23.44444
# print(f"{nr:.2f}")



