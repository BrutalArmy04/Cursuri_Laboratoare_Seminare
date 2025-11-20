# Ex 1

import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_cost = 0
    
    for u, v, cost in edges:
        if uf.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
            if len(mst) == n - 1:
                break
    
    return mst, total_cost

def read_graph(filename):
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().split())
        edges = []
        for _ in range(m):
            u, v, cost = map(int, f.readline().split())
            edges.append((u-1, v-1, cost))
    return n, edges

if __name__ == "__main__":
    n, edges = read_graph("grafpond.in")
    mst, cost = kruskal(n, edges)
    print("Arborele partial de cost minim (Kruskal):")
    for u, v, c in mst:
        print(f"{u+1} - {v+1}: {c}")
    print(f"Cost total: {cost}")

# b

def kruskal_with_forced_edges(n, edges, forced_edges):
    # Adaugă muchiile forțate
    uf = UnionFind(n)
    mst = []
    total_cost = 0
    
    # Adaugă mai întâi muchiile forțate
    for u, v, cost in forced_edges:
        if uf.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
    
    # Sortează restul muchiilor
    remaining_edges = [edge for edge in edges if edge not in forced_edges]
    remaining_edges.sort(key=lambda x: x[2])
    
    # Completează MST cu restul muchiilor
    for u, v, cost in remaining_edges:
        if uf.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
            if len(mst) == n - 1:
                break
    
    return mst, total_cost

def solve_1b():
    n, edges = read_graph("grafpond.in")
    
    print("Introduceti cele 3 muchii obligatorii (format: u v cost):")
    forced_edges = []
    for i in range(3):
        u, v, cost = map(int, input().split())
        forced_edges.append((u-1, v-1, cost))
    
    mst, cost = kruskal_with_forced_edges(n, edges, forced_edges)
    
    if len(mst) == n - 1:
        print("Arborele partial cu muchiile obligatorii:")
        for u, v, c in mst:
            print(f"{u+1} - {v+1}: {c}")
        print(f"Cost total: {cost}")
    else:
        print("Nu exista arbore partial care sa contina toate muchiile obligatorii")


# Ex 2

import heapq

def prim(n, edges):
    # Construim lista de adiacență
    graph = [[] for _ in range(n)]
    for u, v, cost in edges:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    visited = [False] * n
    min_heap = []
    mst = []
    total_cost = 0
    
    # Începem de la nodul 0
    heapq.heappush(min_heap, (0, 0, -1))  # (cost, current, parent)
    
    while min_heap and len(mst) < n - 1:
        cost, u, parent = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, cost))
            total_cost += cost
        
        for v, edge_cost in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_cost, v, u))
    
    return mst, total_cost

def solve_2():
    n, edges = read_graph("grafpond.in")
    mst, cost = prim(n, edges)
    print("Arborele partial de cost minim (Prim):")
    for u, v, c in mst:
        print(f"{u+1} - {v+1}: {c}")
    print(f"Cost total: {cost}")

# Tema 1

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def clustering_kruskal(words, k):
    n = len(words)
    if k >= n:
        return [[word] for word in words], 0
    
    # Construim toate muchiile
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = levenshtein_distance(words[i], words[j])
            edges.append((i, j, dist))
    
    # Sortam muchiile dupa distanta
    edges.sort(key=lambda x: x[2])
    
    # Algoritmul Kruskal modificat pentru clustering
    uf = UnionFind(n)
    mst_edges = []
    
    for u, v, dist in edges:
        if uf.find(u) != uf.find(v):
            if n - len(mst_edges) == k:  # Am ajuns la k componente
                separation_degree = dist
                break
            uf.union(u, v)
            mst_edges.append((u, v, dist))
    else:
        separation_degree = edges[-1][2] if edges else 0
    
    # Grupam cuvintele dupa componentele conexe
    clusters = {}
    for i in range(n):
        root = uf.find(i)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(words[i])
    
    return list(clusters.values()), separation_degree

def solve_clustering():
    with open("cuvinte.in", "r") as f:
        words = f.read().strip().split()
    
    k = int(input("Introduceti k: "))
    
    clusters, separation_degree = clustering_kruskal(words, k)
    
    print("\nClasele:")
    for i, cluster in enumerate(clusters):
        print(f"Clasa {i+1}: {' '.join(cluster)}")
    print(f"Gradul de separare: {separation_degree}")

# Tema 2    

def minimum_cost_to_connect_all_special_nodes(n, edges, special_nodes):
    # Construim graful
    graph = [[] for _ in range(n)]
    for u, v, cost in edges:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    # Folosim Prim pornind de la toate nodurile speciale simultan
    visited = [False] * n
    min_heap = []
    total_cost = 0
    
    # Adaugam toate nodurile speciale in heap
    for node in special_nodes:
        heapq.heappush(min_heap, (0, node))
    
    while min_heap:
        cost, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += cost
        
        for v, edge_cost in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_cost, v))
    
    return total_cost

# Tema 3

def dynamic_mst(n, original_edges, new_edges):
    # MST original
    original_mst, original_cost = kruskal(n, original_edges)
    
    results = []
    
    for new_edge in new_edges:
        # Adaugam muchia noua la lista de muchii
        all_edges = original_edges + [new_edge]
        
        # Calculam noul MST
        new_mst, new_cost = kruskal(n, all_edges)
        
        # Reducerea de cost
        cost_reduction = original_cost - new_cost
        results.append(max(0, cost_reduction))
    
    return results

# Tema 4

def second_best_mst(n, edges):
    # MST principal
    mst, mst_cost = kruskal(n, edges)
    
    # Construim lista de adiacenta pentru MST
    mst_graph = [[] for _ in range(n)]
    for u, v, cost in mst:
        mst_graph[u].append((v, cost))
        mst_graph[v].append((u, cost))
    
    second_best_cost = float('inf')
    
    # Pentru fiecare muchie din MST, incercam sa o inlocuim
    for i in range(len(mst)):
        # Excludem muchia i din MST
        temp_edges = [edge for j, edge in enumerate(edges) if edge != mst[i]]
        
        # Calculam noul MST fara muchia i
        new_mst, new_cost = kruskal(n, temp_edges)
        
        if len(new_mst) == n - 1:  # Daca inca avem un arbore
            second_best_cost = min(second_best_cost, new_cost)
    
    return second_best_cost if second_best_cost != float('inf') else mst_cost



