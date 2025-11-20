# Ex 1

from collections import deque, defaultdict

def critical_path_method():
    """
    Complexitate: O(m + n)
    Corectitudine: 
    - Folosim sortare topologica pentru a procesa activitatile in ordinea dependintelor
    - Calculam timpul minim de start (earliest_start) parcurgand in ordinea topologica
    - Calculam timpul maxim de start (latest_start) parcurgand in ordine inversa
    - Activitatile critice sunt cele unde earliest_start = latest_start
    - Algoritmul este corect deoarece respecta toate constrangerile de precedenta
    """
    with open("activitati.in", "r") as f:
        n = int(f.readline())
        durations = list(map(int, f.readline().split()))
        m = int(f.readline())
        
        graph = defaultdict(list)
        in_degree = [0] * n
        dependencies = []
        
        for _ in range(m):
            i, j = map(int, f.readline().split())
            graph[i-1].append(j-1)
            in_degree[j-1] += 1
            dependencies.append((i-1, j-1))
    
    # Calculam timpul minim de start pentru fiecare activitate - O(n)
    earliest_start = [0] * n
    topo_order = []
    queue = deque()
    
    # Gasim activitatile fara dependinte - O(n)
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    # Sortare topologica - O(m + n)
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
            # Actualizam timpul de start
            if earliest_start[v] < earliest_start[u] + durations[u]:
                earliest_start[v] = earliest_start[u] + durations[u]
    
    # Timpul minim de finalizare - O(n)
    min_completion_time = max(earliest_start[i] + durations[i] for i in range(n))
    
    # Calculam timpul cel mai tarziu de start - O(n)
    latest_start = [min_completion_time] * n
    for i in range(n):
        latest_start[i] -= durations[i]
    
    # Parcurgem in ordine inversa - O(m + n)
    for u in reversed(topo_order):
        for v in graph[u]:
            if latest_start[u] > latest_start[v] - durations[u]:
                latest_start[u] = latest_start[v] - durations[u]
    
    # Gasim activitatile critice - O(n)
    critical_activities = []
    for i in range(n):
        if earliest_start[i] == latest_start[i]:
            critical_activities.append(i + 1)
    
    # Afisare rezultate
    print(f"Timp minim {min_completion_time}")
    print(f"Activitati critice: {' '.join(map(str, critical_activities))}")
    
    for i in range(n):
        print(f"{i+1}: {earliest_start[i]} {earliest_start[i] + durations[i]}")

critical_path_method()

# Ex 2


import heapq


def dijkstra_nearest_control_point():
    """
    Complexitate: O(m log n)
    Corectitudine:
    - Algoritmul lui Dijkstra este corect pentru grafuri cu ponderi pozitive
    - Folosim un min-heap pentru a extrage mereu nodul cu distanta minima
    - Pastram un vector de parinti pentru a reconstrui drumul
    - Verificam toate punctele de control pentru a gasi cel mai apropiat
    - Algoritmul garanteaza gasirea drumului minim datorita proprietatii de greedy
    """
    with open("grafpond.in", "r") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n)]
        
        for _ in range(m):  # O(m)
            u, v, cost = map(int, f.readline().split())
            graph[u-1].append((v-1, cost))
            graph[v-1].append((u-1, cost))
        
        k = int(f.readline())
        control_points = list(map(int, f.readline().split()))
        s = int(f.readline()) - 1
    
    # Dijkstra - O(m log n)
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[s] = 0
    heap = [(0, s)]
    
    while heap:  # O(m) iteratii
        current_dist, u = heapq.heappop(heap)  # O(log n)
        
        if current_dist > dist[u]:
            continue
        
        for v, cost in graph[u]:  # O(grad(u)) total O(m)
            new_dist = current_dist + cost
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(heap, (new_dist, v))  # O(log n)
    
    # Gasim cel mai apropiat punct de control - O(k)
    nearest_control = None
    min_dist = float('inf')
    
    for cp in control_points:
        cp_idx = cp - 1
        if dist[cp_idx] < min_dist:
            min_dist = dist[cp_idx]
            nearest_control = cp_idx
    
    # Reconstruim drumul - O(n)
    path = []
    current = nearest_control
    while current != -1:
        path.append(current + 1)
        current = parent[current]
    path.reverse()
    
    print(f"Cel mai apropiat punct de control: {nearest_control + 1}")
    print(f"Drum minim: {' '.join(map(str, path))}")
    print(f"Cost: {min_dist}")

dijkstra_nearest_control_point()

# Ex 3

import heapq

def maximum_safety_path():
    """
    Complexitate: O(m log n)
    Corectitudine:
    - Transformăm problema de maximizare a produsului în minimizare a sumei de logaritmi
    - Probabilitatea drumului = produs(probabilități muchii)
    - log(probabilitate) = sum(log(probabilități)) → transformă produsul în sumă
    - Folosim -log(probabilitate) pentru a transforma maximizarea în minimizare
    - Dijkstra funcționează deoarece ponderile transformate sunt pozitive
    """
    with open("retea.in", "r") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n)]
        
        for _ in range(m):  # O(m)
            i, j, p = map(int, f.readline().split())
            # Probabilitatea = 2^(-p), deci -log2(prob) = p
            weight = p  # Transformare corecta pentru Dijkstra
            graph[i-1].append((j-1, weight))
    
    s = int(input("Varf start: ")) - 1
    t = int(input("Varf destinatie: ")) - 1
    
    # Dijkstra pentru drum de siguranta maxima - O(m log n)
    dist = [float('inf')] * n
    parent = [-1] * n
    safety = [0.0] * n
    dist[s] = 0
    safety[s] = 1.0
    
    heap = [(0, s)]
    
    while heap:  # O(m) iteratii
        current_dist, u = heapq.heappop(heap)  # O(log n)
        
        if current_dist > dist[u]:
            continue
        
        for v, p in graph[u]:  # O(grad(u)) total O(m)
            new_dist = current_dist + p
            new_safety = safety[u] * (2 ** -p)
            
            if new_dist < dist[v]:
                dist[v] = new_dist
                safety[v] = new_safety
                parent[v] = u
                heapq.heappush(heap, (new_dist, v))  # O(log n)
    
    # Reconstruim drumul - O(n)
    path = []
    current = t
    while current != -1:
        path.append(current + 1)
        current = parent[current]
    path.reverse()
    
    print(f"Drum de siguranță maximă: {' '.join(map(str, path))}")
    print(f"Siguranța drumului: {safety[t]:.6f}")

maximum_safety_path()

# Ex 4

def multi_source_dijkstra():
    """
    Complexitate: O(m log n)
    Corectitudine:
    - Inițializăm heap-ul cu toate sursele la distanța 0
    - Algoritmul lui Dijkstra se extinde natural de la o sursă la multiple surse
    - Fiecare nod va fi atribuit sursei care minimizează distanța
    - Algoritmul este corect deoarece distanța minimă de la orice sursă este calculată corect
    - Proprietatea de optimalitate a lui Dijkstra se menține
    """
    with open("catun.in", "r") as f:
        n, m, k = map(int, f.readline().split())
        graph = [[] for _ in range(n)]
        
        for _ in range(m):  # O(m)
            u, v, cost = map(int, f.readline().split())
            graph[u-1].append((v-1, cost))
            graph[v-1].append((u-1, cost))
        
        sources = list(map(int, f.readline().split()))
    
    # Dijkstra multi-source - O(m log n)
    dist = [float('inf')] * n
    source_node = [-1] * n
    heap = []
    
    # Initializare surse - O(k log n)
    for s in sources:
        s_idx = s - 1
        dist[s_idx] = 0
        source_node[s_idx] = s_idx
        heapq.heappush(heap, (0, s_idx, s_idx))
    
    while heap:  # O(m) iteratii
        current_dist, u, source = heapq.heappop(heap)  # O(log n)
        
        if current_dist > dist[u]:
            continue
        
        for v, cost in graph[u]:  # O(grad(u)) total O(m)
            new_dist = current_dist + cost
            if new_dist < dist[v]:
                dist[v] = new_dist
                source_node[v] = source
                heapq.heappush(heap, (new_dist, v, source))  # O(log n)
    
    # Afisare rezultate - O(n)
    print("Drumuri minime din surse multiple:")
    for i in range(n):
        if source_node[i] != -1 and source_node[i] != i:
            print(f"Nod {i+1} -> Sursa cea mai apropiata: {source_node[i] + 1}, Distanta: {dist[i]}")

multi_source_dijkstra()

# Ex 5

def bellman_ford():
    """
    Complexitate: O(n * m)
    Corectitudine:
    - Algoritmul Bellman-Ford relaxează toate muchiile de n-1 ori
    - După n-1 iterații, dacă mai poate fi făcută o relaxare, există circuit negativ
    - Algoritmul detectează corect circuitele negative accesibile din sursă
    - Reconstrucția circuitului se face urmărind părinții
    - Pentru grafuri fără circuite negative, calculează corect drumurile minime
    """
    with open("grafpond.in", "r") as f:
        n, m = map(int, f.readline().split())
        edges = []
        
        for _ in range(m):  # O(m)
            u, v, cost = map(int, f.readline().split())
            edges.append((u-1, v-1, cost))
        
        s = int(input("Varf start: ")) - 1
    
    # Bellman-Ford - O(n * m)
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[s] = 0
    
    # Relaxare muchii - O(n * m)
    for i in range(n-1):  # O(n) iteratii
        updated = False
        for u, v, cost in edges:  # O(m)
            if dist[u] != float('inf') and dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                parent[v] = u
                updated = True
        if not updated:
            break
    
    # Verificare circuite negative - O(m)
    negative_cycle = None
    for u, v, cost in edges:
        if dist[u] != float('inf') and dist[u] + cost < dist[v]:
            # Am gasit circuit negativ
            negative_cycle = []
            # Gasim nodul din circuit - O(n)
            visited = set()
            current = v
            for _ in range(n):
                current = parent[current]
            
            # Reconstruim circuitul - O(n)
            start = current
            while True:
                negative_cycle.append(current + 1)
                current = parent[current]
                if current == start and len(negative_cycle) > 1:
                    break
            negative_cycle.reverse()
            break
    
    if negative_cycle:
        print(f"Circuit de cost negativ: {' '.join(map(str, negative_cycle))}")
    else:
        print("Drumuri minime:")
        for i in range(n):  # O(n)
            if i != s and dist[i] != float('inf'):
                path = []
                current = i
                # Reconstruire drum - O(n)
                while current != -1:
                    path.append(current + 1)
                    current = parent[current]
                path.reverse()
                print(f"Drum: {' '.join(map(str, path))} Cost: {dist[i]}")

bellman_ford()

# Ex 6

def floyd_warshall():
    """
    Complexitate: O(n^3)
    Corectitudine:
    - Algoritmul calculează toate drumurile minime între oricare două noduri
    - Folosește programare dinamică: dist[i][j] via k
    - Detectează circuite negative verificând dist[i][i] < 0
    - Reconstruiește drumurile folosind matricea next_node
    - Algoritmul este corect datorită substructurii optime a drumurilor minime
    """
    with open("grafpond.in", "r") as f:
        n, m = map(int, f.readline().split())
        
        # Initializeaza matricea de distante - O(n^2)
        dist = [[float('inf')] * n for _ in range(n)]
        next_node = [[-1] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for _ in range(m):  # O(m)
            u, v, cost = map(int, f.readline().split())
            dist[u-1][v-1] = cost
            next_node[u-1][v-1] = v-1
    
    # Algoritmul Floyd-Warshall - O(n^3)
    for k in range(n):  # O(n)
        for i in range(n):  # O(n)
            for j in range(n):  # O(n)
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]
    
    # Verificare circuite negative - O(n)
    has_negative_cycle = False
    for i in range(n):
        if dist[i][i] < 0:
            has_negative_cycle = True
            break
    
    if has_negative_cycle:
        print("Graful contine circuite de cost negativ")
        # Gasim un circuit negativ - O(n^2)
        for i in range(n):
            if dist[i][i] < 0:
                path = []
                current = i
                visited = set()
                # Reconstruim circuitul - O(n)
                while current not in visited:
                    visited.add(current)
                    path.append(current + 1)
                    current = next_node[current][i]
                print(f"Circuit de cost negativ: {' '.join(map(str, path))}")
                break
    else:
        print("Matricea distantelor:")
        for i in range(n):  # O(n^2)
            row = []
            for j in range(n):
                if dist[i][j] == float('inf'):
                    row.append("INF")
                else:
                    row.append(str(dist[i][j]))
            print(' '.join(row))

floyd_warshall()

# b

def graph_center_diameter():
    """
    Complexitate: O(n^3) datorită Floyd-Warshall
    Corectitudine:
    - Folosim Floyd-Warshall pentru a calcula toate distanțele
    - Excentricitatea unui nod = distanța maximă la orice alt nod
    - Raza = excentricitatea minimă, Diametrul = excentricitatea maximă
    - Centrul = nodurile cu excentricitate egală cu raza
    - Algoritmul este corect deoarece calculează exact definițiile matematice
    """
    with open("grafpond.in", "r") as f:
        n, m = map(int, f.readline().split())
        
        # Initializeaza matricea de distante - O(n^2)
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for _ in range(m):  # O(m)
            u, v, cost = map(int, f.readline().split())
            dist[u-1][v-1] = cost
            dist[v-1][u-1] = cost
    
    # Floyd-Warshall pentru graf neorientat - O(n^3)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    
    # Calculam excentricitati - O(n^2)
    eccentricity = [0] * n
    for i in range(n):
        max_dist = 0
        for j in range(n):
            if dist[i][j] != float('inf') and dist[i][j] > max_dist:
                max_dist = dist[i][j]
        eccentricity[i] = max_dist
    
    # Raza, diametrul, centrul - O(n)
    radius = min(eccentricity)
    diameter = max(eccentricity)
    center = [i for i in range(n) if eccentricity[i] == radius]
    
    # Gasim un lant diametral - O(n^2)
    u, v = -1, -1
    max_dist = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf') and dist[i][j] > max_dist:
                max_dist = dist[i][j]
                u, v = i, j
    
    print(f"Raza: {radius}")
    print(f"Centrul: {[c+1 for c in center]}")
    print(f"Diametrul: {diameter}")
    print(f"Lant diametral intre {u+1} si {v+1}")

graph_center_diameter()

