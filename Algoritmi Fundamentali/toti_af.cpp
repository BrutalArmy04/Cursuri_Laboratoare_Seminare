#include <iostream>
#include <queue>
#include <vector>
#include <climits>
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