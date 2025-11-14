# Laborator 2, MI 9 oct 2024, ora 16-18

# # Problema 1 

# n = int(input("Introduceti numarul: "))
# aux, ogl = n, 0

# while aux:
#     ogl = 10 * ogl + aux % 10
#     aux //= 10

# if ogl == n:
#     print(f"Numarul { n } este palindrom")
# else:
#     print(f"Numarul { n } nu este palindrom")



## Problema 2

# L1 = int(input('L1 = '))
# L2 = int(input('L2 = '))
# aux1, aux2 = L1, L2
# while aux1 != aux2:
#     if aux2 > aux1:
#         aux2 -= aux1
#     else:
#         aux1 -= aux2

# print(f'Folosim {L1 * L2 // (aux1 * aux1)} placi patrate cu latura {aux1}')



# ## Problema 3 

# a=int(input("a= "))
# b=int(input("b= "))
# f1=1
# f2=1
# f3=1
# while f3<a:
#     f3=f1+f2
#     f1=f2
#     f2=f3
# if f3<=b:
#     print(f'cel mai mic numar Fibonacci din intervalul [{a}, {b}] este {f3}')
# else:
#     print(f'nu exista numar Fibonacci in intervalul [{a}, {b}]')


# ## Problema 4 
# a, b=input("Introdu doua numere: ").split()
# a, b=int(a), int(b)
# for i in range(0, 100, 5):
#     if a<=i<=b:
#         continue
#     print(i, end=" ")
# print()

# for i in range(95, -1, -5):
#     if a<=i<=b:
#         continue
#     print(i, end=" ")
    
    

# ## Problema 5

# n=int(input("n= "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
  
    

# ## Problema 10 

# n=int(input("nr studenti: "))

# a,b=input("intervalul [a,b]: ").split()
# a, b= int(a), int(b)

# for i in range(1, n):
#     a1, b1=input("intervalul [a,b]: ").split()
#     a1, b1= int(a1), int(b1)
    
#     a, b = max(a, a1), min(b, b1)
    
#     if a>=b:
#         print("studenti nu sunt simultan prezenti")
#         break
# else:
#     print(f"studentii sunt simultan prezenti in intervalul [{a}, {b}]")



## Probleme 6-9, 11-final (singuri)
