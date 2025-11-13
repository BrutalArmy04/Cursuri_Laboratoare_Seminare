# Laborator 2, JO 10 oct 2024, ora 10-12

# ## Problema 1 

# n=int(input("n=: "))
 
# cn=n
# ogl = 0
# while cn!=0:
#     ogl = ogl * 10 + cn % 10
#     cn = cn // 10 
     
# if ogl == n:
#     print(f"{n} este palindrom")
# else :
#     print(f"{n} nu este palindrom")



# ## Problema 2 

# l1 = int(input("l1 = "))
# l2 = int(input("l2 = "))
# cl1 = l1
# cl2 = l2

# while cl1 != cl2:
#     if cl1 > cl2:
#         cl1 = cl1 - cl2
#     else:
#         cl2 = cl2 - cl1
    
        
# print(f"folosim {l1*l2 // (cl1*cl1)} placi patrate de latura {cl1} cm")



# ## Problema 3 
# a = int(input("a= "))
# b = int(input("b= "))

# nr1 = 0
# nr2 = 1
# nr3 = 0

# while nr3 < a:
#     nr3 = nr1 + nr2
#     nr1 = nr2
#     nr2 = nr3

# if nr3 <= b:
#     print(f"cel mai mic numar Fibonacci din intervalul [{a}, {b}] este {nr3}")
# else:
#     print(f"nu exista niciun numar Fibonacci in intervalul [{a}, {b}]")



# ## Problema 4 

# a=int(input('a= '))
# b=int(input('b= '))
# for x in range(0,96,5):
#     if a<=x<=b:
#         continue
#     print(x,end=' ')
# print()

# for x in range(95,-1,-5):
#     if a<=x<=b:
#         continue
#     print(x,end=' ')
    
    

# ## Problema 5 

# n=int(input("n="))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()   
    

# ## Problema 10 
# n = int(input("Numarul de studenti este "))

# a = int(input("a = "))
# b = int(input("b = "))

# for i in range(1,n):
#     x,y = input("Introduceti urm interval: ").split()
#     x=int(x)
#     y=int(y)

#     a,b=max(a,x),min(b,y)
    
#     if a >= b:
#         print("Studenti nu sunt prezenti simultan!")
#         break
# else:
#     print(f'Studenti sunt prezenti in intervalul [{a},{b}].')


## Probleme 6-9, 11-final (singuri)