
value = []
weight = []
# n = 3
# C = 5
# value = [7, 12, 15]
# weight = [2, 3, 5]
n, C = map(int, input().split())
value = list(map(int, input().split()))
weight = list(map(int, input().split()))

def fractionar(n, c, value, weight):

    sol = []
    for i in range(n):
        frac = value[i]/weight[i]
        sol.append((frac, value[i], weight[i]))
    sol.sort(reverse = True)
    sum = 0
    w = 0
    for x in sol:
        if w + x[2] <= c:
            w += x[2]
            sum += x[1]
        else:
            space = c - w
            sum += x[0] * space
            break
    return sum


#print(round(fractionar(n ,C, value, weight), 3))

def discret(n, c, value, weight):
    sol = [0] * (c + 1)
    
    for i in range(n):
        for w in range(c, weight[i] - 1, -1):
            sol[w] = max(sol[w], sol[w - weight[i]] + value[i])
            
    return sol[c]
    
print(discret(n, C, value, weight))