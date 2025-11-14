# #Prob 1

# def completare(M, i, j, d):
#     global k
#     if d == 1:
#         M[i][j] = k
#         k += 1
#         return
#     completare(M, i, j+d//2, d//2)
#     completare(M, i+d//2, j, d//2)
#     completare(M, i, j, d//2)
#     completare(M, i+d//2, j+d//2, d//2)

# n = int(input("n= "))
# M = [[0]*2**n for i in range (2**n)]
# k = 1
# completare(M, 0, 0, 2**n)
# dim_max = len(str(k))
# for linie in M:
#     for elem in linie:
#         print(str(elem).rjust(dim_max), end = " ")
#     print()



# #Prob 4

# import random
# def quickselect(A, k, f_pivot = random.choice):
#     pivot = f_pivot(A)

#     L = [x for x in A if x < pivot]
#     E = [x for x in A if x == pivot]
#     G = [x for x in A if x > pivot]

#     if k < len(L):
#         return quickselect(L, k, f_pivot)



#     #mediana medianelor

# def mediana(A):
#     if len(A)<=5:
#         return sorted(A)[len(A)//2]
#     grupuri = [ sorted(A[i:i+5]) for i in range(0, len(A)-rest, 5)]
#     mediane = [ grup[2]]

#     #rip