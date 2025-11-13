# Laborator 2, VI 11 oct 2024, ora 16-18

# # Problema 1 
# n= int(input("numarul este: "))
# copie=n
# ogl=0
# while n!=0:
#     ogl=ogl*10+ n%10
#     n=n//10
# if ogl==copie:
#     print(f"numarul {copie} este palindrom")
# else:
#     print(f"numarul {copie} nu este palindrom")



# # Problema 2 

# L,l = input("dimensiunile sunt: ").split()

# l = int(l)
# L = int(L)

# cl = l
# cL = L
# while l != 0:
#     r = L % l
#     L = l
#     l = r  
#   # print(l,L,r)

# print(f"folosim {cl*cL//L**2} placi patrate de latura {L} cm")



# # Problema 3 

# a,b=input("capetele intervalului sunt: ").split()
# a,b=int(a),int(b)
# f1=f2=1
# f3=1
# while f3<a:
#     f3=f1+f2
#     f1=f2
#     f2=f3
# if f3<=b:
#     print(f"cel mai mic numar Fibonacci din intervalul [{a},{b}] este {f3}")
# else:
#     print(f"nu exista niciun numar Fibonacci in intervalul [{a},{b}]")


# # Problema 4 
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(0,100,5):
#     if a<=i<=b:
#         continue
#     print(i, end=' ')
# print()
# for i in range(95,-1,-5):
#     if not a<=i<=b:
#         print(i, end=' ')



# # Problema 5 
# n=int(input("n= "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end = ' ')
#     print()
        
        
    
# # Problema 10 

# n = int(input("numarul de studenti: "))
# a = int(input("ora sosirii: "))
# b = int(input("ora plecarii: "))

# for _ in range(n-1):
#     a2 = int(input("ora sosirii: "))
#     b2 = int(input("ora plecarii: "))
#     a , b = max(a , a2) , min(b , b2)
#     if a >= b:
#         print("nu exista interval orar comun")
#         break
# else:
#     print(f"intervalul orar comun este de la {a} la {b}")


## Probleme 6-9, 11-final (singuri)