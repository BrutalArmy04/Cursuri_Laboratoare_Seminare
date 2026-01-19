#include <iostream>
#include <queue>
#include <vector>
#include <climits>
#include <stack>
#include <algorithm>
using namespace std;


void BFS (vector<vector<int>> const& graph, const int source, bool is_matrix)
{
    vector <int> neighbour(graph.size(), -1);
    vector <int> distance(graph.size(), INT_MAX);
    vector <int> color(graph.size(), 0);
    queue<int> q;

    color[source] = 1;   //  we are working with it right now
    distance[source] = 0;
    q.push(source);

    while (!q.empty())
    {
        int u = q.front();
        if (is_matrix == 1)
        {
        for (int v = 0; v < graph.size(); v++)
        if (graph[u][v] == 1)
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
        q.pop();
        color[u] = 2;

    }

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
     vector<vector<int>> const& graph, vector <int> &low_link_value, bool is_matrix, int parent)
{
    color[u] = 1;
    disc_time[u] =low_link_value[u] = time++;
    if (is_matrix == 1)
    {
        for (auto v = 0; v < graph.size(); v++)
        if (graph[u][v] == 1 && color[v] == 0 && v!=parent)
       { 
        visiting_ce(v, color, disc_time, time, graph, low_link_value, is_matrix, u);
        low_link_value[u] = min(low_link_value[u], low_link_value[v]);
        if (low_link_value[v] > disc_time[u])
        cout<<u<<"->"<<v;

    
    }
    else if (v!=parent)
    low_link_value[u] = min(low_link_value[u], disc_time[v]);

    }
    else
    {
        for (int v : graph[u])
        if (color[v] == 0 && v!=parent)
        {
            visiting_ce(v, color, disc_time, time, graph, low_link_value, is_matrix, u);
            low_link_value[u] = min(low_link_value[u], low_link_value[v]);
            if (low_link_value[v] > disc_time[u])
            cout<<u<<"->"<<v;
        }
        else if (v!=parent)
        low_link_value[u] = min(low_link_value[u], disc_time[v]);
    }
    color[u] = 2;
}


void critical_edges(vector<vector<int>> const &graph, bool is_matrix, int source)
{
    vector <int> disc_time(graph.size(), 0);
    vector <int> low_link_value(graph.size(), 0);

    //vector <int> neighbour(graph.size(), 0);
    vector <int> color(graph.size(), 0);

    int time = 0;
    for (int u = 0; u < graph.size(); u++)
        if (color[u] == 0)
        visiting_ce(u, color, disc_time, time, graph, low_link_value, is_matrix, -1);

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
    vector<vector<int>> const& graph, vector <int> &timespan, stack <int>& st, int run)
{
    color[u] = 1;
    cout<<u<<" ";
    distance[u] = time++;
        for (auto v = 0; v < graph.size(); v++)
        if (graph[u][v] == 1 && color[v] == 0)
        visiting_Kosaraju(v, color, distance, time, graph, timespan, st, run);
   
    color[u] = 2;
    timespan[u] = time++;
    if (run == 1)
    st.push(u);

}


void DFS_Kosaraju (vector<vector<int>> const& graph, stack <int>& st, int run)
{
    vector <int> color(graph.size(), 0);
    //vector <int> neighbour(graph.size(), -1);
    vector <int> distance(graph.size(), 0);
    vector <int> timespan(graph.size(), 0);

    int time = 0;
    if (run == 1)
    {    for (int u = 0; u < graph.size(); u++)
            if (color[u] == 0)
            
                visiting_Kosaraju(u, color, distance, time, graph, timespan, st, 1);}
    else if (run == 2)
    {
            while (!st.empty())
    {
        int u = st.top();
        st.pop();
        if (color[u] == 0)
            visiting_Kosaraju(u, color, distance, time, graph, timespan, st, 2);

    }
    }

}

void Kosaraju(vector<vector<int>>& graph)
{
    stack <int> st;
    DFS_Kosaraju(graph, st, 1);
    vector<vector<int>> tr_graph = trasp_matrix(graph);
    DFS_Kosaraju(tr_graph, st, 2);

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