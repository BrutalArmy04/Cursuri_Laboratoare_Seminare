# Laborator 2, MI 9 oct 2024, ora 14-16

## Problema 1 

# n=int(input("Introdu un numar n: "))
# x=n
# inv=0

# while x:
#     inv=inv*10+x%10
#     x=x//10
    
# if n==inv:
#     print(f"{n} este palindrom")
# else:
#     print(f"{n} nu este palindrom")
    


# ## Problema 2 

# l1 = int(input("Introduceti lungimea: "))
# l2 = int(input("Introduceti latimea: "))

# cl1=l1
# cl2=l2

# while cl2:
#     aux=cl1%cl2
#     cl1=cl2
#     cl2=aux
    
# print(f"Folosim {l1*l2//(cl1*cl1)} placi patrate de latura {cl1} cm")



# ## Problema 3
# a = int(input('Introdu limita inferioara: '))
# b = int(input('Introdu limita superioara: '))

# x = 1
# y = 1
# z = 1

# while z < a:
#     z = x + y
#     x = y
#     y = z
    
# if z <= b:
#     print(f'Cel mai mic numar Fibonacci din intervalul [{a}, {b}] este {z}')
# else:
#     print(f'Nu exista niciun numar Fibonacci in intervalul [{a}, {b}]')



# ## Problema 4 
# a,b=input("Valorile: ").split()
# a,b=int(a),int(b)
# for x in range(0,100,5):
#     if a<=x<=b:
#         continue
#     print(x, end=" ")
# print()

# for x in range(95,-1,-5):
#     if a<=x<=b:
#         continue
#     print(x, end=" ")



# ## Problema 5  

# n = int(input("n = "))
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print(y, end = " ")
#     print()



# ## Problema 10 

# n=int(input("n="))
# a=int(input("Cap interval stanga: "))
# b=int(input("Cap interval dreapta: "))
# for i in range(2, n+1):
#     x=int(input(f"Cap interval stanga {i}: "))
#     y=int(input(f"Cap interval dreapta {i}: "))
#     a,b=max(a,x),min(b,y)
#     if a>=b:
#         print("Studentii nu pot fi simultan prezenti")
#         break
# else:
#     print(f"Studentii sunt simultan prezenti in intervalul [{a}, {b}]")
        


## Probleme 6-9, 11-final (singuri)
