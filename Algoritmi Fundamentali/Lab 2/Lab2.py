#Ex1




from collections import defaultdict, deque

n, m = map(int, input().split())
graf = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graf[a].append(b)
    graf[b].append(a)
prieten = [0] * (n + 1)  
def bipartite():
        for start in range(1, n + 1):
            if prieten[start] != 0:  
                continue  
            # BFS
            queue = deque([start])
            prieten[start] = 1  # Fac prietenia
            while queue:
                current = queue.popleft()
                current_color = prieten[current]
                # Verific
                for friend in graf[current]:
                    if prieten[friend] == 0: 
                        prieten[friend] = 3 - current_color  # Schimb culoarea
                        queue.append(friend)
                    elif prieten[friend] == current_color:  
                        return False  
        
        return True

if bipartite():
    print(' '.join(str(prieten[i]) for i in range(1, n + 1)))
else:
    print("Imposibil")

#Ex2   

from collections import deque, defaultdict
import sys

def topological_sort(n, edges):
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1
    
    #caut noduri cu grad interior 0 (indegree)
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else None

def find_cycle(n, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
    
    visited = [0] * (n + 1)  # 0 = nevizitat, 1 in curs de vizitare, 2 vizittat
    parent = [-1] * (n + 1)
    cycle_start, cycle_end = -1, -1
    
    def dfs(node):
        nonlocal cycle_start, cycle_end
        visited[node] = 1 
        
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                parent[neighbor] = node
                if dfs(neighbor):
                    return True
            elif visited[neighbor] == 1:
                cycle_start = neighbor
                cycle_end = node
                return True
        
        visited[node] = 2  
        return False
    
    for i in range(1, n + 1):
        if visited[i] == 0 and dfs(i):
            cycle = []
            node = cycle_end
            while node != cycle_start:
                cycle.append(node)
                node = parent[node]
            cycle.append(cycle_start)
            cycle.append(cycle[0]) 
            return cycle[::-1]
    
    return None

def main():
    input = sys.stdin.read().split()
    n, m = int(input[0]), int(input[1])
    edges = []
    
    idx = 2
    for _ in range(m):
        a, b = int(input[idx]), int(input[idx + 1])
        edges.append((a, b))
        idx += 2
    
    result = topological_sort(n, edges)
    
    if result is not None:
        print(" ".join(map(str, result)))
    else:
        print("Imposibil")
        cycle = find_cycle(n, edges)
        if cycle:
            print("Ciclu:", " ".join(map(str, cycle)))

if __name__ == "__main__":
    main()


#Ex 3

from collections import deque
import sys

def count_rooms(n, m, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    room_count = 0
    
    def bfs(i, j):
        queue = deque([(i, j)])
        visited[i][j] = True
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n and 0 <= ny < m and 
                    not visited[nx][ny] and grid[nx][ny] == '.'):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and not visited[i][j]:
                room_count += 1
                bfs(i, j)
    
    return room_count

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    
    for i in range(1, n + 1):
        grid.append(list(data[i].strip()))
    
    result = count_rooms(n, m, grid)
    print(result)

if __name__ == "__main__":
    main()

#Ex 4

import sys
sys.setrecursionlimit(300000)

def kosaraju(n, edges):
    # graful si graful invers
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]
    
    for a, b in edges:
        graph[a].append(b)
        reverse_graph[b].append(a)
    
    # DFS pe primul graf
    visited = [False] * (n + 1)
    order = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        order.append(node)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    
    # DFS pe al doilea graf
    visited = [False] * (n + 1)
    components = [0] * (n + 1)
    current_component = 0
    
    def dfs2(node):
        visited[node] = True
        components[node] = current_component
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor)
    
    # parcurs invers in functie de cum se termina
    for node in reversed(order):
        if not visited[node]:
            current_component += 1
            dfs2(node)
    
    return current_component, components[1:]

def main():
    input = sys.stdin.read().split()
    n, m = int(input[0]), int(input[1])
    edges = []
    
    idx = 2
    for _ in range(m):
        a, b = int(input[idx]), int(input[idx + 1])
        edges.append((a, b))
        idx += 2
    
    k, labels = kosaraju(n, edges)
    print(k)
    print(" ".join(map(str, labels)))

if __name__ == "__main__":
    main()

#Ex 5

from collections import defaultdict
import sys

def find_articulation_points(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    ids = [0] * (n + 1)
    low = [0] * (n + 1)
    visited = [False] * (n + 1)
    is_articulation = [False] * (n + 1)
    id_counter = 0
    
    def dfs(node, parent, root):
        nonlocal id_counter
        visited[node] = True
        ids[node] = low[node] = id_counter
        id_counter += 1
        
        child_count = 0
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            
            if not visited[neighbor]:
                child_count += 1
                dfs(neighbor, node, root)
                low[node] = min(low[node], low[neighbor])
                
                # am gasit articulatie
                if parent != -1 and low[neighbor] >= ids[node]:
                    is_articulation[node] = True
                # radacina nu mai multi copii
                if parent == -1 and child_count > 1:
                    is_articulation[node] = True
            else:
                low[node] = min(low[node], ids[neighbor])
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1, i)
    
    return sum(is_articulation)

def main():
    while True:
        data = sys.stdin.readline().split()
        if not data:
            continue
        
        n, m = map(int, data)
        if n == 0 and m == 0:
            break
        
        edges = []
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        
        result = find_articulation_points(n, edges)
        print(result)

if __name__ == "__main__":
    main()

#Ex 6

from collections import deque
import sys

def distances_to_control_points(n, edges, control_points):
    """
    Multi-source BFS from all control points to find minimum distances.
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # initializez distante
    dist = [-1] * (n + 1)
    queue = deque()
    
    # pornesc DFS din toate punctele
    for cp in control_points:
        dist[cp] = 0
        queue.append(cp)
    
    # DFS din mai multe surse
    while queue:
        node = queue.popleft()
        current_dist = dist[node]
        
        for neighbor in graph[node]:
            if dist[neighbor] == -1:  
                dist[neighbor] = current_dist + 1
                queue.append(neighbor)
    
    return dist[1:]

def main():
    with open('graf.in', 'r') as f:
        data = f.read().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    
    idx = 2
    for _ in range(m):
        u, v = int(data[idx]), int(data[idx + 1])
        edges.append((u, v))
        idx += 2
    
    # puncte de control
    control_points = list(map(int, data[idx:]))
    
    result = distances_to_control_points(n, edges, control_points)
    
    with open('graf.out', 'w') as f:
        f.write(" ".join(map(str, result)))

if __name__ == "__main__":
    main()



