### Laborator 1 - Grupa 133.2 - VI 4 oct

# # Problema 1 

# x=int(input("valoare lui x este: "))
# y=int(input("valoare lui y este: "))
# s=x+y
# p=x*y
# print(s,p)
# print(s,p,sep=",")

# print(s,p,sep="\n")

# print(f"suma numerelor {x} si {y} este {x+y}, iar produsul este {x*y}")
# print("suma numerelor {x} si {y} este {x+y}, iar produsul este {x*y}")



###############################3
# # Problema 2 

# a,b,c=input("Introduceti trei numere: ").split()
# print(a,b,c)
# a,b,c=int(a),int(b),int(c)
# if 0<=a<24 and 0<=b<60 and 0<=c<60:
#     print(f"{a:02d}:{b:02d}:{c:02d}")
# else:
#     print("datele introduse nu sunt ore, minute si secunde")


# ######################
# # Problema 3

# z=int(input("z="))
# l=int(input("l="))
# a=int(input("a="))
# ok=True
# if l in [1,3,5,7,8,10,12]: #luna cu 31 de zile
#     if 1<=z<31:
#         z=z+1
#     elif z==31:
#         if l==12:
#             z=1
#             l=1
#             a=a+1
#         else:
#             l=l+1
#             z=1
#     else:
#         ok=False
        

# elif l in [4,6,9,11]: #luna cu 30 de zile
#     if 1<=z<30:
#         z=z+1
#     elif z==30:
#         z=1
#         l=l+1
#     else:
#         ok=False
    
# elif l==2: #februarie
#     if a%4==0 and a%100!=0 or a%400==0: 
#         #an bisect, 29 zile
#         if 1<=z<29:
#             z=z+1
#         elif z==29:
#             z=1
#             l=l+1
#         else:
#             ok=False
#     else:
#         #an nu e bisect, 28 zile
#         if 1<=z<28:
#             z=z+1
#         elif z==28:
#             z=1
#             l=l+1
#         else:
#             ok=False
        
# else:
#     ok=False

# if ok==False:
#     print("Datele introduse nu sunt corecte.")
# else:
#     print(f"{z:02d}.{l:02d}.{a:04d}")
    
    

# nr = 43.23371345
# print(f"{nr:.3f}")

