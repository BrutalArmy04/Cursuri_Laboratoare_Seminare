# Laborator 2, JO 10 oct 2024, ora 12-14

# ## Problema 1 
# n=int(input("n= "))
# aux = n
# ogl=0
# while aux!=0:
#     ogl = ogl*10 + aux%10
#     aux=aux//10
# if ogl == n:
#     print(f"{n} este palindrom")
# else:
#     print(f"{n} nu este palindrom")



## Problema 2 
# l1 = int(input("L1 = "))
# l2 = int(input("L2 = "))
# a = l1
# b = l2
# while b > 0:
#     r = a % b
#     a = b
#     b = r
#     #print(a, b, r)
# print(f"Folosim {l1 * l2 // (a * a)} placi patrate de latura {a} cm.")



# ## Problema 3 

# a=int(input("a= "))
# b=int(input("b= "))
# f1=f2=1
# f3=1
# while f3<a :
#     f3=f1+f2
#     f1=f2
#     f2=f3
# if f3>b:
#     print(f"in intervalul [{a},{b}] nu exista niciun numar Fibonacci")
# else:
#     print(f"cel mai mic numar Fibonacci din intervalul [{a},{b}] este {f3}")
   


# ## Problema 4 

# a = int(input("a = "))
# b = int(input("b = "))

# for i in range(0, 100, 5):
#     if a <= i <= b:
#         continue
#     print(i, end=' ')

# print()

# for i in range(95, -1, -5):
#     if not a <= i <= b:
#         print(i, end=' ')


## Problema 5 

# n=int(input("n= "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


# ## Problema 10 
# n=int(input("n="))

# a=int(input("a="))
# b=int(input("b="))

# for _ in range(n-1):
#     x=int(input("x="))
#     y=int(input("y="))
#     a,b=max(a,x),min(b,y)
#     if a>=b:
#         print("Stundentii nu sunt simultan prezenti.")
#         break
# else:
#     print(f"Stundentii sunt simultan prezenti in intervalul [{a}, {b}].")


## Probleme 6-9, 11-final (singuri)