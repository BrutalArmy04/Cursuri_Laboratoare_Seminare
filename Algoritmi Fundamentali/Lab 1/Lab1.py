#Ex A

def orientare(parametru):
    if m[b][a] == 0:
        return parametru
    else:
        return m[b][a]

def lista_de_adiacenta(d, y, m):
    for i in range(y):
        for j in range(y):
            if m[i][j] == 1:
                if i not in d.keys():
                     d[i] = [j]
                else:
                    d[i].append(j)
    return d

parametru = int(input("parametru (0 pt orientat, 1 pt neorientat)= "))
f = open("D:\Facultate\Algoritmi Fundamentali\Lab 1\prob1.txt", 'r') 
s = False 
m = []
d = {}
for linie in f.readlines():
    if s == True:
        a, b = linie.strip().split()
        a = int(a)
        b = int(b)
        m[a][b] = 1
        m[b][a] = orientare(parametru)
    else:
        x, y = linie.strip().split()
        x = int(x)
        y = int(y)
        m = [[0 for i in range(y)] for j in range(y)]
        s = True

d = lista_de_adiacenta(d, y, m)
print(d)
#for linie in m: 
    #for elem in linie: 
        #print(elem, end=" ") 
    #print() 
f.close()

# pentru multigrafuri as salva ca tupluri instantele duble

#B

from collections import deque # structura de date, double-ended queue, coada in 2 sensuri


print("Introduceti N M s x:")
N, M, S, X = map(int, input().split())
graf = [[] for _ in range(N + 1)]
print(f"Introduceti {M} arce (cate unul pe linie):")
for _ in range(M):
    x, y = map(int, input().split())
    graf[x].append(y)
    
dist = [-1] * (N + 1)   #drum minim
parent = [0] * (N + 1)
queue = deque()
    
dist[S] = 0
parent[S] = 0
queue.append(S)
    
while queue:
    node = queue.popleft()
        
    if node == X:
        break
            
    for nr in graf[node]:
        if dist[nr] == -1:
            dist[nr] = dist[node] + 1
            parent[nr] = node
            queue.append(nr)
    
if dist[X] == -1:
    print(f"Nu există drum de la {S} la {X}")
else:
    #refac drumul
    drum = []
    current = X
    while current != 0:
        drum.append(current)
        current = parent[current]
    drum.reverse()
        
    print(f"Drum minim de la {S} la {X}:")
    print(" -> ".join(map(str, drum)))
    print(f"Lungime drum: {dist[X]} arce")


#C



with open('dfs.in', 'r') as f:
    lines = f.readlines()
    
first_line = lines[0].split()
N = int(first_line[0])
M = int(first_line[1])
    
# Păstrăm lista originală de muchii
muchii = []
graf = [[] for _ in range(N + 1)]
    
for i in range(1, M + 1):
    line = lines[i].split()
    x = int(line[0])
    y = int(line[1])
    muchii.append((x, y))
    graf[x].append(y)
    graf[y].append(x)

# DFS pentru componente și clasificare
visited = [False] * (N + 1)
parent = [0] * (N + 1)
discovery_time = [0] * (N + 1)
time = 0
tree_edges = []
back_edges = []
components = 0
    
for i in range(1, N + 1):
    if not visited[i]:
        components += 1
        stack = [(i, 0)]  # (nod, părinte, luata ca un fel de stiva)
        visited[i] = True
        parent[i] = 0
        time += 1
        discovery_time[i] = time
            
        while stack:
            nod, par = stack[-1]
                
            # Căutăm următorul vecin
            if graf[nod]:
                neighbor = graf[nod].pop()
                    
                if neighbor == par:
                    continue
                    
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = nod
                    time += 1
                    discovery_time[neighbor] = time
                    stack.append((neighbor, nod))
                    tree_edges.append((nod, neighbor))
                else:
                    # Muchie de întoarcere
                    back_edges.append((nod, neighbor))
            else:
                stack.pop()
    
# Scriere rezultate
with open('dfs.out', 'w') as f:
    f.write(f"Numar componente conexe: {components}\n")
    f.write(f"Muchii de arbore ({len(tree_edges)}): {tree_edges}\n")
    f.write(f"Muchii de intoarcere ({len(back_edges)}): {back_edges}\n")
        
    if back_edges:
        f.write("Graful contine ciclu\n")
    else:
        f.write("Graful este aciclic\n")






