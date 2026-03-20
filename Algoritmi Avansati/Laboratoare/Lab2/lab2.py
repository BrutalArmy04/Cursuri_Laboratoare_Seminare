import math

def ex1():
    a, b = map(float, input().split())
    p = int(input())
    m = int(input())
    l = math.ceil(math.log2((b-a)*10**p))
    d = (b-a)/2**l

    for _ in range(m):
        c = input()
        x = input().strip()
        if c == "TO":
            x = float(x)
            binar = bin(math.floor((x-a) / d))[2:]
            print(binar.zfill(l))
        elif c == "FROM":
            x = int(x, 2)
            x = a + x * d
            print(x)

def ex2f(a, b, c, x):
    return a * x**2 + b * x + c

def ex2():
    a,b,c = map(float, input().split())
    n = int(input())
    l_val = list(map(float, input().split()))
    l_sum = [ex2f(a, b, c, i) for i in l_val]
    suma = sum(l_sum)
    l_final = [i/suma for i in l_sum]
    p_curent = 0
    print(f"{p_curent:.6f}")
    for prob in l_final:
        p_curent += prob
        print(f"{p_curent:.6f}")

def ex3():
    n = int(input())
    a = input()
    b = input()
    nr_rupere = int(input())
    c = a[:nr_rupere] + b[nr_rupere:]
    d = b[:nr_rupere] + a[nr_rupere:]
    print(c)
    print(d)


def ex4():
    l, k = map(int, input().split())
    c_str = input()
    c_val = int(c_str, 2)
    indici = list(map(int, input().split()))
    for idx in indici:
        masca = 1 << (l - 1 - idx)
        c_val = c_val ^ masca
    rezultat = bin(c_val)[2:].zfill(l)
    print(rezultat)

ex4()