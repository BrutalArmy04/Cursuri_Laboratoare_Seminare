import random

def ex1():

    with open("elmaj.in", "r") as f:
        data = f.read().split()        
    if not data:
        return
        
    n = int(data[0])
    if n == 0:
        with open("elmaj.out", "w") as f:
            f.write("-1\n")
        return
        
    prag = n // 2 + 1
    
    for _ in range(20):
        idx_aleator = random.randint(1, n)
        candidat = data[idx_aleator]
        
        aparitii = 0
        for i in range(1, n + 1):
            if data[i] == candidat:
                aparitii += 1
                
        if aparitii >= prag:
            with open("elmaj.out", "w") as f:
                f.write(f"{candidat} {aparitii}\n")
            return
            
    with open("elmaj.out", "w") as f:
        f.write("-1\n")

ex1()

def freivalds(A, B, C, n, k=5):
    for _ in range(k):
        r = [random.randint(0, 1) for _ in range(n)]
        
        Br = [0] * n
        for i in range(n):
            for j in range(n):
                Br[i] += B[i][j] * r[j]
                
        ABr = [0] * n
        for i in range(n):
            for j in range(n):
                ABr[i] += A[i][j] * Br[j]
                
        Cr = [0] * n
        for i in range(n):
            for j in range(n):
                Cr[i] += C[i][j] * r[j]
                
        for i in range(n):
            if ABr[i] != Cr[i]:
                return False
                
    return True

def ex2():
    
    n = int(input().strip())
    A = [[int(x) for x in input().split()] for _ in range(n)]
    B = [[int(x) for x in input().split()] for _ in range(n)]
    C = [[int(x) for x in input().split()] for _ in range(n)]

    if freivalds(A, B, C, n):
        print("YES")
    else:
        print("NO")

#ex2()