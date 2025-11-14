# Laborator 2, VI 11 oct 2024, ora 14-16

# # Problema 1 
# n=int(input("n= "))
# cn=n
# ogl=0
# while cn:
#     ogl = ogl*10 + cn%10
#     cn//=10
# if n==ogl:
#     print(f"Numarul {n} este palindrom")
# else:
#     print(f"Numarul {n} nu este palindrom")



# # Problema 2
# l1,l2=input("introduceti dimensiunile: ").split()
# l1=int(l1)
# l2=int(l2)
# cl1=l1
# cl2=l2
# while cl2:
#     r=cl1%cl2
#     cl1=cl2
#     cl2=r
#   # print(cl1,cl2,r)
# print(f"folosim {l1*l2//cl1**2} placute patrate de latura {cl1} cm")



# # Problema 3 
# a = int(input("prima valoare: "))
# b = int(input("a doua valoare: "))
# f1 = 0 
# f2 = 1 
# f3 = 0 
# while f3<a:
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
# if f3<= b:
#     print(f"cel mai mic numar Fibonacci din intervalul [{a},{b}] este {f3}")
# else:
#     print(f"nu exista niciun numar Fibonacci in intervalul [{a},{b}]")




# # Problema 4 

# a, b = input("Introduceti cele doua numere: ").split()
# a=int(a)
# b=int(b)

# for i in range(0, 100, 5):
#     if a<=i<=b:
#         continue
#     print(i, end=" ")
    
# print()
    
# for i in range(95, -1, -5):
#     if not a<=i<=b:
#         print(i, end=" ")



# # Problema 5 
# n=int(input("se citeste: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(f"{j} ", end="")
#     print()
    

# # Problema 10 
# n=int(input("nr studenti= "))
# a,b=input("primul interval: ").split()
# a=int(a)
# b=int(b)
# for i in range(1,n):
#     a2,b2=input("primul interval: ").split()
#     a2=int(a2)
#     b2=int(b2)
#     a,b=max(a,a2),min(b,b2)
#     if a>=b:
#         print("studentii nu sunt prezenti simultan")
#         break
# else:
#     print(f"studentii sunt prezenti simultan in intervalul [{a},{b}]")
    
    
## Probleme 6-9, 11-final (singuri)