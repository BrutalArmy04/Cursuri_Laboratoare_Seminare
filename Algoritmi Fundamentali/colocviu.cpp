//var 3 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <climits>
using namespace std;

int matrix[10001][10001];
int main() {
    
    int nodes, y;
    cin>>nodes;

    vector <int> node_values;
    for (int i = 0; i < nodes; i++)
    {
        cin>>y;
        node_values.push_back(y);
    }


    int a, b;
     for (int i = 0; i < nodes - 1; i++)
    {
         cin>>a>>b;
         matrix[a][b] = 1;
    }

   
     vector <int> parent(nodes, 0);

     parent[0] = -1;

     int sum_max = INT_MIN;

     vector <int> level(nodes, -1);

     int u;

     level[0] = 0;

     queue <int> q;

     q.push(1);

     while (!q.empty())
     {
         u = q.front();
         q.pop();
         if (level[u-1] == -1 && u!=1)
         level[u-1] = level[parent[u-1]] + 1;
         for (int v = 1; v <= nodes; v++)
         if (matrix[u][v] == 1)
         {
             parent[v-1] = u;
             q.push(v);
         }
     }

     for (int i = 0; i < nodes; i++)
     for (int j = 0; j < nodes && j!=i; j++)
     if (abs(level[i]-level[j])<=1)
     if (node_values[i] + node_values[j] > sum_max)
     sum_max = node_values[i] + node_values[j];

     cout<<sum_max;

     return 0;
}



