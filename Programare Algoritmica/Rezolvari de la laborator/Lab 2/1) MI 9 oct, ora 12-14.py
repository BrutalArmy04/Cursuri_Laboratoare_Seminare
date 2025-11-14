### Laborator 2, MI 9 oct 2024, ora 12-14
## Problema 1 

# n=int(input("Numarul n este= "))
# x=n 
# ogl=0
# while n!=0:
#     ogl = ogl * 10 + n % 10
#     n = n // 10
# if ogl==x:
#     print(f'{x} este palindrom')
# else:
#     print(f'{x} nu este palindrom')



## Problema 2 

# L1 = int(input("lungimea este "))
# L2 = int(input("latimea este "))

# l1, l2 = L1, L2

# while l1 != l2:
#     if l1 > l2:
#         l1 -= l2
#     else:
#         l2 -= l1

# nr_placi = (L1 * L2) // (l1 * l1)

# print(f"folosim {nr_placi} placi de latura {l1}")



# # Problema 3 

# a=int(input("a= "))
# b=int(input("b= "))
# x,y=0,1
# z = 0

# while a>x+y:
#     x, y, z = y, z, y+z
#     if b<z:
#         break
# if a<=z<=b:
#     print(z)
# else:
#     print("Numarul nu exista")



# # Problema 4 

# # for x in range(a, b, p):
# #     pass

# a = int(input("Dati capatul inferior: "))
# b = int(input("Dati capatul superior: "))

# for x in range (0, 100, 5):
#     if a <= x <= b:
#         continue
#     print(x, end=" ")
    
# print()
    
# for x in range(95, -1, -5):
#     if a <= x <= b:
#         continue
#     print(x, end= " ")
        
        
        
# # Problema 5 
# n=int(input("n= "))
# for x in range(1, n+1):
#     for y in range(1, x+1):
#         print(y, end=" ")
#     print()
    


# # Problema 10
# n=int(input("n= "))
# x=int(input("x= "))
# y=int(input("y= "))

# for i in range(n-1):
#     a=int(input("a= "))
#     b=int(input("b= "))
#     x,y=max(x,a),min(y,b)
#     if x>=y:
#         print("studentii nu pot fi prezenti simultan")
#         break
# else:
#     print(f"studentii pot fi prezenti simultan in intervalul [{x}, {y}]")
    


### Probleme 6 - 9, 11-final (singuri)
