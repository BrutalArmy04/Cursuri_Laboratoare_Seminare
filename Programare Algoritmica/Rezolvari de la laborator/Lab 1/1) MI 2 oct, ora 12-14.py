### Laborator 1 - Grupa 131.1 - MI 2 oct
# # problema 1

# x = int(input("primul numar = "))
# y = int(input("al doilea numar = "))

# s = x + y
# p = x * y

# print(s, p)
# print(s, p, sep=",")

# print(s)
# print(p)
# print(s, p, sep="\n")

# print(f'suma numerelor {x} si {y} este {x + y}, iar produsul este {x * y}')
# print('suma numerelor {x} si {y} este {x + y}, iar produsul este {x * y}')



# ##############################
# # Problema 2 
# numere=input("introduceti 3 numere naturale: ")

# # L=numere.split()
# # print(L)

# a,b,c=numere.split()
# # print(a,b,c, sep="; ")
# a,b,c=int(a),int(b),int(c)
# print(a,b,c,sep="; ")

# if 0<=a<=23 and 0<=b<=59 and 0<=c<=59 :
#     print(f'{a:02d} : {b:02d} : {c:02d}')
# else :
#     print("numerele nu pot reprezenta ore, minute si secunde")
    

####################################
# # Problema 3 
# z = int(input("Ziua este "))
# l = int(input("Luna este "))
# a = int(input("Anul este "))
# ok = True
# if z<1 or l<1:
#     print("Ziua si luna incorecte")
#     exit()
    
# if l==1 or l==3 or l==5 or l==7 or l==8 or l==10 or l==12:
#     #31 de zile
#     if z>31:
#         ok=False
#     if z!=31:
#         z+=1
#     elif l!=12:
#         z=1
#         l+=1
#     else:
#         z=1
#         l=1
#         a+=1
#         #z,l ,a = 1 , 1 , a+1
        
# elif l==4 or l==6 or l==9 or l==11:
#     #30 de zile
#     if z>30:
#         ok=False
#     elif z!=30:
#         z+=1
#     else:
#         z=1
#         l+=1
    
# elif l==2:
#     #februarie
#     if (a%4==0 and a%100!=0) or a%400==0:
#         #bisect max 29 zile
#         if z>29:
#             ok=False
#         elif z!=29:
#             z+=1
#         else:
#             z=1
#             l+=1
#     else:
#         #nebisect max 28 zile
#         if z>28:
#             ok=False
#         elif z!=28:
#             z+=1
#         else:
#             z=1
#             l+=1
# else:
#     print(f'luna {l} este invalida')

# if ok==False:
#     print("Data incorect introdusa")
# else:
#     print(f'{z}.{l}.{a}')
#     print(z , l , a, sep=".")


################################
# 2 zecimale float
# {nr:.2f}





