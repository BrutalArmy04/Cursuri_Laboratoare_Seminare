# Laborator 2, JO 10 oct 2024, ora 14-16

# # Problema 1 

# n = int(input("n= "))
# ogl = 0
# cn = n
# while n:
#     ogl = ogl*10 + n%10
#     n //= 10
# if cn == ogl:
#     print(f'{cn} este palindrom')
# else:
#     print(f'{cn} nu este palindrom')



# Problema 2 

# L1, L2 = input("Introduceti dimensiunile:").split()
# L1, L2 = int(L1), int(L2)
# aux1, aux2 = L1, L2
# while aux2:
#     r = aux1 % aux2
#     aux1 = aux2
#     aux2 = r
# print(f"Folosim { L1 * L2 // (aux1 * aux1) } placi patrate de latura {aux1} cm")
    


# # Problema 3 
# a, b = input('Introduceti doua numere: ').split()
# a, b = int(a), int(b)
# f1, f2 = 0, 1
# f3 = 0
# while f3 < a:
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
# if f3 <= b:
#     print(f'Cel mai mic numar Fibonacci din intervalul [{a}, {b}] este {f3}')
# else:
#     print(f'Nu exista niciun numar Fibonacci in intervalul [{a}, {b}].')



# # Problema 4 
# a,b = input("Introduceti capetele: ").split()
# a,b = int(a),int(b)
# for x in range(0,100,5):
#     if a<=x<=b:
#         continue
#     print(x, end=" ")
# print()
# for x in range(95,-1,-5):
#     if not a<=x<=b:
#         print(x, end=" ")



# # Problema 5 
# n=int(input("n= "))
# for x in range(1, n+1):
#     for y in range(1, x+1):
#         print(y, end=" ")
#     print()


# # Problema 10 
# n = int(input('Introduceti numarul de studenti: '))
# a, b = input('Primul interval: ').split()
# a, b = int(a), int(b)
# for _ in range(n - 1):
#     a2, b2 = input('Alt interval: ').split()
#     a2, b2 = int(a2), int(b2)
#     a, b = max(a, a2), min(b, b2)
#     if a >= b:
#         print('Studentii nu sunt toti simultan prezenti.')
#         break
# else:
#     print(f'Studentii sunt toti simultan prezenti in intervalul [{a}, {b}].')
    

## Probleme 6-9, 11-final (singuri)
