# Prob 1

from collections import deque
import sys

def read_network(file_path):
    with open(file_path, 'r') as f:
        data = list(map(int, f.read().strip().split()))
    idx = 0
    n = data[idx]; idx += 1
    s = data[idx]; idx += 1
    t = data[idx]; idx += 1
    m = data[idx]; idx += 1
    edges = []
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    capacity = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = data[idx]; idx += 1
        v = data[idx]; idx += 1
        cap = data[idx]; idx += 1
        fl = data[idx]; idx += 1
        edges.append((u, v, cap, fl))
        capacity[u][v] = cap
        graph[u][v] = fl
        graph[v][u] = -fl  # pentru flux invers în matricea de flux
    return n, s, t, m, edges, graph, capacity

def is_valid_flow(n, s, t, edges, graph, capacity):
    # Verificare mărginire
    for u, v, cap, fl in edges:
        if fl < 0 or fl > cap:
            return False, f"Fluxul pe arcul ({u},{v}) nu respectă capacitatea."
    # Verificare conservare
    for node in range(1, n + 1):
        if node == s or node == t:
            continue
        inflow = sum(graph[v][node] if graph[v][node] > 0 else 0 for v in range(1, n + 1))
        outflow = sum(graph[node][v] if graph[node][v] > 0 else 0 for v in range(1, n + 1))
        if inflow != outflow:
            return False, f"Nodul {node} nu conservă fluxul."
    return True, "DA"

def edmonds_karp(n, s, t, capacity, graph):
    parent = [0] * (n + 1)
    max_flow = 0
    while True:
        # BFS pentru găsire drum de ameliorare
        for i in range(n + 1):
            parent[i] = -1
        parent[s] = s
        q = deque([s])
        while q:
            u = q.popleft()
            for v in range(1, n + 1):
                if parent[v] == -1 and capacity[u][v] - graph[u][v] > 0:
                    parent[v] = u
                    q.append(v)
        if parent[t] == -1:
            break
        # Calculăm capacitatea reziduală minimă pe drum
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - graph[u][v])
            v = u
        # Actualizăm fluxul
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] += path_flow
            graph[v][u] -= path_flow
            v = u
        max_flow += path_flow
    return max_flow, graph

def min_cut(n, s, capacity, graph):
    # BFS în graful rezidual
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        for v in range(1, n + 1):
            if not visited[v] and capacity[u][v] - graph[u][v] > 0:
                visited[v] = True
                q.append(v)
    cut_edges = []
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if visited[u] and not visited[v] and capacity[u][v] > 0:
                cut_edges.append((u, v))
    cut_capacity = sum(capacity[u][v] for u, v in cut_edges)
    return cut_capacity, cut_edges

def solve_flux_maxim(file_path):
    n, s, t, m, edges, graph, capacity = read_network(file_path)
    valid, msg = is_valid_flow(n, s, t, edges, graph, capacity)
    print(msg)
    if not valid:
        return
    max_flow, new_graph = edmonds_karp(n, s, t, capacity, graph)
    print(max_flow)
    # Afișăm fluxul pe arce
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if new_graph[u][v] > 0 and capacity[u][v] > 0:
                print(u, v, new_graph[u][v], end=' ')
    print()
    cut_cap, cut_edges = min_cut(n, s, capacity, new_graph)
    print(cut_cap)
    for u, v in cut_edges:
        print(u, v, end=' ')
    print()

if __name__ == "__main__":
    solve_flux_maxim("retea.in")

# Prob 2

from collections import deque

def read_graph(file_path):
    with open(file_path, 'r') as f:
        data = list(map(int, f.read().strip().split()))
    idx = 0
    n = data[idx]; idx += 1
    m = data[idx]; idx += 1
    edges = []
    for _ in range(m):
        u = data[idx]; idx += 1
        v = data[idx]; idx += 1
        edges.append((u, v))
    return n, m, edges

def is_bipartite(n, edges):
    color = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    for start in range(1, n + 1):
        if color[start] == -1:
            color[start] = 0
            parent = [-1] * (n + 1)
            parent[start] = start
            q = deque([start])

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        parent[v] = u
                        q.append(v)

                    elif color[v] == color[u]:
                        path_u = [u]
                        x = u
                        while parent[x] != x:
                            x = parent[x]
                            path_u.append(x)

                        path_v = [v]
                        y = v
                        while parent[y] != y:
                            y = parent[y]
                            path_v.append(y)

                        i = len(path_u) - 1
                        j = len(path_v) - 1
                        while i >= 0 and j >= 0 and path_u[i] == path_v[j]:
                            i -= 1
                            j -= 1

                        cycle = path_u[:i+2] + path_v[j+1::-1]
                        return False, color, cycle

    return True, color, []

def bipartite_matching(n, edges, color):
    left = [i for i in range(1, n + 1) if color[i] == 0]
    right = [i for i in range(1, n + 1) if color[i] == 1]

    left_idx = {node: i+1 for i, node in enumerate(left)}
    right_idx = {node: i+1+len(left) for i, node in enumerate(right)}

    
    left_rev = {i+1: node for i, node in enumerate(left)}
    right_rev = {i+1+len(left): node for i, node in enumerate(right)}

    total_nodes = len(left) + len(right) + 2
    s = 0
    t = total_nodes - 1

    cap = [[0] * total_nodes for _ in range(total_nodes)]

    # muchii intre stanga si dreapta
    for u, v in edges:
        if u in left_idx and v in right_idx:
            cap[left_idx[u]][right_idx[v]] = 1
        if v in left_idx and u in right_idx:
            cap[left_idx[v]][right_idx[u]] = 1

    # conectez stanga
    for u in left:
        cap[s][left_idx[u]] = 1

    # conectez dreapta
    for v in right:
        cap[right_idx[v]][t] = 1

    # Edmonds–Karp
    flow = [[0] * total_nodes for _ in range(total_nodes)]
    parent = [-1] * total_nodes

    def bfs():
        for i in range(total_nodes):
            parent[i] = -1
        parent[s] = s
        q = deque([s])

        while q:
            u = q.popleft()
            for v in range(total_nodes):
                if parent[v] == -1 and cap[u][v] - flow[u][v] > 0:
                    parent[v] = u
                    if v == t:
                        return True
                    q.append(v)
        return False

    max_flow = 0
    while bfs():
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, cap[u][v] - flow[u][v])
            v = u

        # flux
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow += path_flow

    matching = []
    L = len(left)
    for u in range(1, L+1):
        for v in range(L+1, total_nodes-1):
            if flow[u][v] > 0:
                matching.append((left_rev[u], right_rev[v]))

    return matching

def solve_cuplaj(file_path):
    n, m, edges = read_graph(file_path)
    bipartite, color, odd_cycle = is_bipartite(n, edges)

    if not bipartite:
        print("Graful nu este bipartit.")
        print("Ciclu impar:", " ".join(map(str, odd_cycle)))
        return

    matching = bipartite_matching(n, edges, color)

    for u, v in matching:
        print(u, v)


if __name__ == "__main__":
    solve_cuplaj("graf.in")

# Prob 3

def read_sequences(file_path):
    with open(file_path, 'r') as f:
        data = list(map(int, f.read().strip().split()))
    n = data[0]
    s1 = data[1:1+n]
    s2 = data[1+n:1+2*n]
    return n, s1, s2

def build_graph_from_degrees(n, indeg, outdeg):
    if sum(indeg) != sum(outdeg):
        return None
    # construim rețea flux: 
    # noduri 1..n -> nodurile originale ca surse (outdeg)
    # noduri n+1..2n -> nodurile originale ca destinații (indeg)
    # s = 0, t = 2n+1
    total = 2*n + 2
    s = 0
    t = total - 1
    cap = [[0] * total for _ in range(total)]
    # legăm s la nodurile sursă (outdeg)
    for i in range(1, n+1):
        cap[s][i] = outdeg[i-1]
    # legăm nodurile destinație la t
    for i in range(n+1, 2*n+1):
        cap[i][t] = indeg[i-n-1]
    # legăm fiecare sursă la fiecare destinație (posibil arc)
    for i in range(1, n+1):
        for j in range(n+1, 2*n+1):
            if i != j - n:  # nu buclă
                cap[i][j] = 1
    
    # flux maxim
    flow = [[0] * total for _ in range(total)]
    parent = [0] * total
    
    from collections import deque
    def bfs():
        for i in range(total):
            parent[i] = -1
        parent[s] = s
        q = deque([s])
        while q:
            u = q.popleft()
            for v in range(total):
                if parent[v] == -1 and cap[u][v] - flow[u][v] > 0:
                    parent[v] = u
                    q.append(v)
        return parent[t] != -1
    
    max_flow = 0
    while bfs():
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, cap[u][v] - flow[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u
        max_flow += path_flow
    
    if max_flow != sum(outdeg):
        return None
    
    # construim arcele
    arcs = []
    for i in range(1, n+1):
        for j in range(n+1, 2*n+1):
            if flow[i][j] > 0:
                u = i
                v = j - n
                arcs.append((u, v))
    return arcs

def solve_secvente(file_path):
    n, s1, s2 = read_sequences(file_path)
    arcs = build_graph_from_degrees(n, s1, s2)
    if arcs is None:
        print("NU")
    else:
        for u, v in arcs:
            print(u, v, end=' ')
        print()

if __name__ == "__main__":
    solve_secvente("secvente.in")


# Prob 4


def read_strings(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split()
    return lines[0], lines[1]

def lcs(A, B):
    n, m = len(A), len(B)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # reconstrucție
    i, j = n, m
    res = []
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            res.append(A[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(res))

def solve_lcs(file_path):
    A, B = read_strings(file_path)
    print(lcs(A, B))

if __name__ == "__main__":
    solve_lcs("lcs.in")


# Prob 5

def read_multigraph(file_path):
    with open(file_path, 'r') as f:
        data = list(map(int, f.read().strip().split()))
    n, m = data[0], data[1]
    edges = []
    idx = 2
    for _ in range(m):
        u = data[idx]; idx += 1
        v = data[idx]; idx += 1
        edges.append((u, v))
    return n, m, edges

def eulerian_cycle(n, edges):
    from collections import defaultdict, deque
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    # verificare grade pare
    for d in degree[1:]:
        if d % 2 != 0:
            return None
    # algoritmul lui Hierholzer
    stack = [1]
    circuit = []
    while stack:
        u = stack[-1]
        if adj[u]:
            v = adj[u].pop()
            # eliminăm muchia inversă
            adj[v].remove(u)
            stack.append(v)
        else:
            circuit.append(stack.pop())
    circuit.reverse()
    if len(circuit) != m + 1:
        return None
    return circuit

def solve_euler(file_path):
    n, m, edges = read_multigraph(file_path)
    cycle = eulerian_cycle(n, edges)
    if cycle is None:
        print("Nu este eulerian")
    else:
        print(' '.join(map(str, cycle)))

if __name__ == "__main__":
    solve_euler("graf.in")


# Prob 6

def read_weighted_graph(file_path):
    with open(file_path, 'r') as f:
        data = list(map(int, f.read().strip().split()))
    n, m = data[0], data[1]
    adj = [[float('inf')] * n for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = data[idx]; idx += 1
        v = data[idx]; idx += 1
        w = data[idx]; idx += 1
        adj[u][v] = w
    return n, adj

def hamiltonian_min_cost(n, adj):
    # dp[mask][i] = cost minim pentru a ajunge la i, vizitând nodurile din mask
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # începem de la nodul 0
    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == float('inf'):
                continue
            for j in range(n):
                if not (mask >> j) & 1 and adj[i][j] != float('inf'):
                    new_mask = mask | (1 << j)
                    dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + adj[i][j])
    full_mask = (1 << n) - 1
    min_cost = float('inf')
    last_node = -1
    for i in range(n):
        if dp[full_mask][i] != float('inf') and adj[i][0] != float('inf'):
            total = dp[full_mask][i] + adj[i][0]
            if total < min_cost:
                min_cost = total
                last_node = i
    if min_cost == float('inf'):
        return None, None
    # reconstrucție
    path = []
    mask = full_mask
    node = last_node
    while mask:
        path.append(node)
        prev_mask = mask ^ (1 << node)
        prev_node = -1
        for i in range(n):
            if dp[prev_mask][i] + adj[i][node] == dp[mask][node]:
                prev_node = i
                break
        mask = prev_mask
        node = prev_node
    path.reverse()
    return min_cost, path

def solve_hamilton(file_path):
    n, adj = read_weighted_graph(file_path)
    cost, path = hamiltonian_min_cost(n, adj)
    if cost is None:
        print("Nu este hamiltonian")
    else:
        print(cost)
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    solve_hamilton("graf.in")

