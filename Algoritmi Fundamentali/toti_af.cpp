#include <iostream>
#include <queue>
#include <vector>
#include <climits>
#include <stack>
#include <algorithm>
using namespace std;


vector <int> BFS (vector<vector<int>> const& graph, const int source, bool is_matrix, vector <int>& neighbour)
{
    for (auto i = 0; i < graph.size(); i++)
    neighbour[i] = -1;
    vector <int> distance(graph.size(), INT_MAX);
    vector <int> color(graph.size(), 0);
    queue<int> q;
    vector <int> result;

    color[source] = 1;   //  we are working with it right now
    distance[source] = 0;
    q.push(source);

    while (!q.empty())
    {
        int u = q.front();
        if (is_matrix == 1)
        {
        for (int v = 0; v < graph.size(); v++)
        if (graph[u][v] > 0)
            {
                if (color[v]==0)
                {
                    color[v] = 1;
                    distance[v] = distance[u] + 1;
                    neighbour[v] = u;
                    q.push(v);
                }

            }
        }
        else
        {
            for (int v: graph[u])
            if (color[v]==0)
                {
                    color[v] = 1;
                    distance[v] = distance[u] + 1;
                    neighbour[v] = u;
                    q.push(v);
                }
        }
        result.push_back(u);
        q.pop();
        color[u] = 2;

    }
    return result;

}       



void visiting(int u, vector <int> & color, vector <int> & distance, int &time, 
    vector<vector<int>> const& graph, vector <int> &timespan, const bool is_matrix)
{
    color[u] = 1;
    distance[u] = time++;
    if (is_matrix == 1)
    {
        for (auto v = 0; v < graph.size(); v++)
        if (graph[u][v] == 1 && color[v] == 0)
        visiting(v, color, distance, time, graph, timespan, is_matrix);
    }
    else
    {
        for (int v : graph[u])
        if (color[v] == 0)
        visiting(v, color, distance, time, graph, timespan, is_matrix);
    }
    color[u] = 2;
    timespan[u] = time++;

}


void DFS (vector<vector<int>> const& graph, const bool is_matrix)
{
    vector <int> color(graph.size(), 0);
    //vector <int> neighbour(graph.size(), -1);
    vector <int> distance(graph.size(), 0);
    vector <int> timespan(graph.size(), 0);

    int time = 0;

    for (int u = 0; u < graph.size(); u++)
        if (color[u] == 0)
        visiting(u, color, distance, time, graph, timespan, is_matrix);

}

vector <int> topological_sorting(vector<vector<int>> const& graph, const int source, bool is_matrix)
{
    vector <int> grades(graph.size(), 0);
    for (int i = 0; i<graph.size(); i++)
    if (is_matrix == 1)
    {   
    for (int j = 0; j<graph.size(); j++)
    if (graph[i][j]==1)
    grades[j]++;
    }
    else
    {
        for (int j : graph[i])
        grades[j]++;
    } 
    queue <int> q;
    vector <int> result;
    for (int i = 0; i<graph.size(); i++)
        if (grades[i] == 0)
        q.push(i);
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        result.push_back(u);

        if (is_matrix == 1)
        {
        for (int v = 0; v < graph.size(); v++)
        {
        if (graph[u][v] == 1)
        {
        grades[v]--;
        if (grades[v] == 0)
        q.push(v);
    }
        }
        }
        else
        {
            for (int v : graph[u])
            {
                grades[v]--;
                if (grades[v] == 0)
                q.push(v);
            }
        }
    }

    if (result.size() == graph.size())
    return result;
    else
    return result = {};
}

void visiting_ce(int u, vector <int> &color, vector <int> &disc_time, int &time,
     vector<vector<int>> const& graph, vector <int> &low_link_value, bool is_matrix, int parent, vector <pair<int, int>>& result)
{


    color[u] = 1;
    disc_time[u] =low_link_value[u] = time++;
    if (is_matrix == 1)
    {
        for (auto v = 0; v < graph.size(); v++)
        if (graph[u][v] == 1 && color[v] == 0 && v!=parent)
       { 
        visiting_ce(v, color, disc_time, time, graph, low_link_value, is_matrix, u, result);
        low_link_value[u] = min(low_link_value[u], low_link_value[v]);
        if (low_link_value[v] > disc_time[u])
        result.push_back({u,v});

    
    }
    else if (v!=parent && graph[u][v] == 1)
    low_link_value[u] = min(low_link_value[u], disc_time[v]);

    }
    else
    {
        for (int v : graph[u])
        if (color[v] == 0 && v!=parent)
        {
            visiting_ce(v, color, disc_time, time, graph, low_link_value, is_matrix, u, result);
            low_link_value[u] = min(low_link_value[u], low_link_value[v]);
            if (low_link_value[v] > disc_time[u])
            {
                result.push_back({u,v});
            }
        }
        else if (v!=parent)
        low_link_value[u] = min(low_link_value[u], disc_time[v]);
    }
    color[u] = 2;

}


vector <pair<int, int>> critical_edges(vector<vector<int>> const &graph, bool is_matrix, int source)
{
    vector <int> disc_time(graph.size(), 0);
    vector <int> low_link_value(graph.size(), 0);
    vector <pair<int, int>> result;
    //vector <int> neighbour(graph.size(), 0);
    vector <int> color(graph.size(), 0);

    int time = 0;
    for (int u = 0; u < graph.size(); u++)
        if (color[u] == 0)
        visiting_ce(u, color, disc_time, time, graph, low_link_value, is_matrix, -1, result);
    
    return result;

}

vector<vector<int>> trasp_matrix(vector<vector<int>> graph)
{
    for (auto i = 0; i<graph.size(); i++)
    for (auto j = 0; j<graph.size(); j++)
    if (i<j)
    swap(graph[i][j], graph[j][i]);
    return graph;
}

void visiting_Kosaraju(int u, vector <int> & color, vector <int> & distance, int &time, 
    vector<vector<int>> const& graph, vector <int> &timespan, stack <int>& st, int run, vector <int> &comp)
{
    color[u] = 1;
    cout<<u<<" ";
    distance[u] = time++;
        for (auto v = 0; v < graph.size(); v++)
        if (graph[u][v] == 1 && color[v] == 0)
        visiting_Kosaraju(v, color, distance, time, graph, timespan, st, run, comp);
   
    color[u] = 2;
    timespan[u] = time++;
    if (run == 1)
    st.push(u);
    else
    comp.push_back(u);

}


void DFS_Kosaraju (vector<vector<int>> const& graph, stack <int>& st, int run, vector <vector<int>>& result)
{
    vector <int> color(graph.size(), 0);
    //vector <int> neighbour(graph.size(), -1);
    vector <int> distance(graph.size(), 0);
    vector <int> timespan(graph.size(), 0);
    vector <int> comp;

    int time = 0;
    if (run == 1)
    {    for (int u = 0; u < graph.size(); u++)
            if (color[u] == 0)
                {
                visiting_Kosaraju(u, color, distance, time, graph, timespan, st, 1, comp);}
            }
    else if (run == 2)
    {
            while (!st.empty())
    {
        int u = st.top();
        st.pop();
        if (color[u] == 0)
            {
                comp = {};
                visiting_Kosaraju(u, color, distance, time, graph, timespan, st, 2, comp);
                result.push_back(comp);
            }

    }
    }
}
vector <vector<int>> Kosaraju(vector<vector<int>>& graph)
{
    stack <int> st;
    vector <vector<int>> result;
    DFS_Kosaraju(graph, st, 1, result);
    vector<vector<int>> tr_graph = trasp_matrix(graph);
    DFS_Kosaraju(tr_graph, st, 2, result);
    return result;

}

bool Havel_Hakimi(vector <int> grades)
{
    int sum = 0, value;
    for (auto i: grades)
        sum += i;
    if (sum%2==1)
    return 0;

    sort(grades.begin(), grades.end(), greater<int>());

    for (int i = 0; i<grades.size() - 1; i++)
    {
        value = grades[i];
        grades[i] = 0;
        if (value > grades.size() - 1 - i)
        return 0;
        int j = i + 1;
        while (value!=0)
        {
            if (grades[j] == 0)
            return 0;
            --grades[j++];
            value--;
        }
        sort(grades.begin() + 1 + i, grades.end(), greater<int>());
    }
    return 1;
}


struct Edge {
    int u, v;  
    int weight; 
    
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

int find(vector <int>& color, int const i)
{
    if (color[i] == i)
    return i;
    else
    return color[i] = find(color, color[i]);
}

void unite(vector <int> & color, const int i, const int j)
{
    color[find(color, j)] = find(color, i);

}

vector <Edge> Kruskal(vector <Edge> Edge_List, int nodes)
{
    sort(Edge_List.begin(), Edge_List.end());
    vector <int> color;
    for (int i = 0; i<nodes; i++)
        color.push_back(i);
    vector <Edge> result;
    int k = 0;
    for (int i = 0; i<Edge_List.size(); i++)
    if (find(color, Edge_List[i].u)!=find(color, Edge_List[i].v))
    {
        unite(color, Edge_List[i].u, Edge_List[i].v);
        result.push_back(Edge_List[i]); 
    }
    return result;
}


vector <Edge> Prim (vector <Edge> Edge_List, int const& nodes, int const &start)
{
    vector<vector<pair<int, int>>> adj(nodes);
    
    for (auto& edge : Edge_List) {
        adj[edge.u].push_back({edge.weight, edge.v});
        adj[edge.v].push_back({edge.weight, edge.u});
    }
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector <bool> visited(nodes, 0);
    vector <int> distance(nodes, INT_MAX);
    distance[start] = 0;
    pq.push({0, start});
    vector <Edge> result;
    pair <int, int> u;  // cost, index
    vector <int> parent(nodes, -1);
    while (!pq.empty())
    {
        u = pq.top();
        pq.pop();
        if(visited[u.second] == 0)
        {
            visited[u.second] = 1;
            distance[u.second] = u.first;
            if (parent[u.second]!=-1)
            {
                Edge add;
                add.weight = u.first;
                add.u = parent[u.second];
                add.v = u.second;
                result.push_back(add);

            }
            
            for (auto x : adj[u.second])
            {
                if (visited[x.second]==0 && x.first < distance[x.second])
                {
                parent[x.second] = u.second;
                distance[x.second] = x.first;
                pq.push({x.first, x.second});
            }

            }
        }
    }
    return result;

}

vector <int> Dijkstra(vector <Edge> Edge_List, int const& start, int const& nodes)
{
    vector<vector<pair<int, int>>> adj(nodes);
    vector <int> distance(nodes, INT_MAX);
    vector <int> parent(nodes, 0);
    for (auto& edge : Edge_List) {
        adj[edge.u].push_back({edge.weight, edge.v});
        
    }
    distance[start] = 0;

    priority_queue< pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;

    pq.push({0, start});
    pair <int, int> u;  // cost, index
    while (!pq.empty())
    {
        u = pq.top();
        pq.pop();

        for (auto x : adj[u.second])

        if (distance[u.second] + x.first< distance[x.second])
        {
            parent[x.second] = u.second;
            distance[x.second] = x.first + distance[u.second];
            pq.push({distance[x.second], x.second});
        }
    }

    return distance;
}

vector <int> Bellman_Ford(int nodes, vector <Edge> Edge_List, int source)

{
    vector <int> distance(nodes, INT_MAX);
    vector <int> parent(nodes, 0);

    distance[source] = 0;


    for (int k = 0; k < nodes-1; k++)
    for (auto& x: Edge_List)
    if (distance[x.u] + x.weight < distance[x.v] && distance[x.u]!=INT_MAX)
    {
        distance[x.v] = distance[x.u] + x.weight;
        parent[x.v] = x.u;
    }
    for (auto& x: Edge_List)
    if (distance[x.u] + x.weight < distance[x.v] && distance[x.u]!=INT_MAX)
    {
        return {};
    }
    return distance;
}

vector <int> min_dist_in_acyclic_graphs(int source, vector <Edge> Edge_List, int nodes, vector<vector<int>> graph)
{

    vector <int> distance(nodes, INT_MAX);
    vector <int> parent(nodes, 0);
    vector <int> top_sort = topological_sorting(graph, source, 1);
    distance[source] = 0;
    vector<vector<pair<int, int>>> adj(nodes);

    for (auto& edge : Edge_List) 
        adj[edge.u].push_back({edge.weight, edge.v});
        
    for (auto u:top_sort)
    {
        for (auto x : adj[u])
        {
            if (distance[u] + x.first < distance[x.second] && distance[u]!=INT_MAX)
            {
                distance[x.second] = distance[u] + x.first;
                parent[x.second] = u;
            }
        }
    }

    return distance;
}


vector <vector<long long>> Floyd_Warshall (vector <Edge> Edge_List, int nodes, vector<vector<int>> graph)
{
    vector<vector<long long>> distance(nodes, vector<long long>(nodes, INT_MAX));
    vector<vector<int>> parent(nodes, vector<int>(nodes, -1));
    for (int i = 0; i < nodes; i++)
    for (int j = 0; j < nodes; j++)
    {
        distance[i][i] = 0;
        if (graph[i][j] == 1)
        parent[i][j] = i;
    }
    for (auto x : Edge_List)
    {
        if (graph[x.u][x.v] == 1)
        distance[x.u][x.v] = x.weight;
    }


    for (int k = 0; k < nodes; k++)
    for (int i = 0; i < nodes; i++)
    for (int j = 0; j < nodes; j++)
    {
        if (distance[i][k] != INT_MAX && distance[k][j] != INT_MAX)
        if ( distance[i][j] > distance[i][k] + distance[k][j])       
        {
            distance[i][j] = distance[i][k] + distance[k][j];
            parent[i][j] = parent[k][j];
        }
    }
    return distance;

}


int Ford_Fulkenson(vector <Edge> EdgeList, int nodes, int s, int t) // maximum flow
{
    vector<vector<int>> rGraph(nodes, vector<int>(nodes, 0));
    for (Edge edge : EdgeList)
    rGraph[edge.u][edge.v] = edge.weight;
    vector <int> neighbour(nodes);

    vector <int> BFS_vector = BFS(rGraph, s, 1, neighbour);
    int flow = 0;


    while(neighbour[t]!=-1) 
    {
        int path_flow = INT_MAX;
        for (int v = t; v!=s; v = neighbour[v])
        {
            if (path_flow > rGraph[neighbour[v]][v])
            path_flow = rGraph[neighbour[v]][v];

            
        }
        flow += path_flow;


        for (int v = t; v!=s; v = neighbour[v])
        {
            rGraph[neighbour[v]][v] -= path_flow;
            rGraph[v][neighbour[v]] += path_flow;
        }
        BFS_vector = BFS(rGraph, s, 1, neighbour);

        
    }

    return flow;
}


vector <int> Hierholzer (vector<vector<int>> graph, int nodes, int start)   // eulerian circuits
{
    vector <int> circuit;
    stack <int> current_path;

    current_path.push(start);

    while (!current_path.empty())
    {
        int u = current_path.top();
        bool found_neighbour = 0;
        for (int v = 0; v < nodes; v++)
        {
            if (graph[u][v] == 1)
            {

                found_neighbour = 1;
                graph[u][v] = 0;
                current_path.push(v);
                break;

            }
        }

        if (found_neighbour == 0)
        {
        current_path.pop();
        circuit.push_back(u);
    }
    }

    reverse(circuit.begin(), circuit.end());
    return circuit;
}

pair<int, vector<int>> hamiltonian_min_cost(int n, const vector<vector<int>>& adj) {

    vector<vector<int>> dp(1 << n, vector<int>(n, INT_MAX));

    dp[1][0] = 0;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if (dp[mask][i] == INT_MAX) continue;

            for (int j = 0; j < n; ++j) {
                if (!((mask >> j) & 1) && adj[i][j] != INT_MAX) {
                    int new_mask = mask | (1 << j);
                    if (dp[mask][i] + adj[i][j] < dp[new_mask][j]) {
                        dp[new_mask][j] = dp[mask][i] + adj[i][j];
                    }
                }
            }
        }
    }

    int full_mask = (1 << n) - 1;
    int min_cost = INT_MAX;
    int last_node = -1;

    for (int i = 0; i < n; ++i) {
        if (dp[full_mask][i] != INT_MAX && adj[i][0] != INT_MAX) {
            int total = dp[full_mask][i] + adj[i][0];
            if (total < min_cost) {
                min_cost = total;
                last_node = i;
            }
        }
    }

    if (min_cost == INT_MAX) {
        return {-1, {}}; 
    }

    vector<int> path;
    int mask = full_mask;
    int node = last_node;

    while (mask > 0) {
        path.push_back(node);
        int prev_mask = mask ^ (1 << node);
        int prev_node = -1;

        if (node == 0 && prev_mask == 0) break; 

        for (int i = 0; i < n; ++i) {
            if ((prev_mask >> i) & 1) {
                if (adj[i][node] != INT_MAX && dp[prev_mask][i] + adj[i][node] == dp[mask][node]) {
                    prev_node = i;
                    break;
                }
            }
        }

        if (prev_node == -1) break;

        mask = prev_mask;
        node = prev_node;
    }

    reverse(path.begin(), path.end());
    return {min_cost, path};
}