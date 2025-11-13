### Laborator 1 - Grupa 132.2 - JO 3 oct
# # Problema 1 
# x=int(input("x = "))
# y=int(input("y = "))
# sum=x+y
# prod=x*y

# print(sum,prod)
# print(sum,prod,sep=",")
# print(sum,",",prod,sep="")

# print(sum,prod,sep="\n")

# print(f"Suma numerelor '{x}' si \"{y}\" este {x+y}, iar produsul este {x*y}.")
# print("Suma numerelor '{x}' si \"{y}\" este {x+y}, iar produsul este {x*y}.")



# #############################
# # Problema 2 
# a,b,c=input("introduceti 3 numere: ").split()
# print(a,b,c)
# print(type(a))
# a,b,c=int(a),int(b),int(c)

# if 0<=a<24 and 0<=b<60 and 0<=c<60 :
#     print(f"{a:02d}:{b:02d}:{c:02d}")
# else:
#     print("nu este ora valida")


#################################
# Problema 3

# z=int(input("z= "))
# l=int(input("l= "))
# a=int(input("a= "))

# ok=True
# if l in [1,3,5,7,8,10,12] :
#     #31 zile
#     if 1<=z<31 :
#         z+=1
#     elif z==31:
#         z=1
#         if l==12:
#             l=1
#             a+=1
#         else:
#             l+=1
#     else:
#         ok=False
        
# elif l in [4,6,9,11]:
#     #30zile
#     if 1<=z<30 :
#         z+=1
#     elif z==30:
#         z=1
#         l+=1
#     else:
#         ok=False
        
# elif l==2:
#     #febr
#     if a%4==0 and a%100!=0 or a%400==0:
#         #an bisect, 29zile
#         if 1<=z<29 :
#             z+=1
#         elif z==29:
#             z=1
#             l+=1
#         else:
#             ok=False
#     else:
#         #an nu e bisect, 28zile
#         if 1<=z<28 :
#             z+=1
#         elif z==28:
#             z=1
#             l+=1
#         else:
#             ok=False
# else :
#     ok=False

# if ok==True:
#     print(f"{z:02d}.{l:02d}.{a:04d}")
# else:
#     print("Data introdusa este invalida!")




# nr = 3.3436547658
# print(f"{nr:.3f}")

