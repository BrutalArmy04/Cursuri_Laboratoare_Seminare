// Lab1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
struct nod {
    nod* st, * dr;
    int val;
};  // putem face asta dar e mai complicat


//vom  folosi vectori: nod i:
//     st : i*2+1
//     dr: i*2+2
//     parinte: (i-1)/2
//     O(nlogn) pt inserare si la fel si pt stergere
//
int heap[100];
int n, k, int v[100000];

void up(int pos)
{
    if (heap[pos] < heap[pos - 1] / 2)
    {
        swap(heap[pos], heap[(pos - 1) / 2]);
        up((pos - 1) / 2);
    }
}
void down(int pos)
{ 
    if (pos * 2 + 2 < k)
    {
        int minim = min(heap[pos * 2 + 1], heap[pos * 2 + 2]);
        if (minim > heap[pos])
            return;
        if (minim == heap[pos * 2 + 1])
        {
            swap(heap[pos], heap[pos * 2 + 1]);
            down(pos * 2 + 1);
        }
        else
        {
            swap(heap[pos], heap[pos * 2 + 2]);
            down(pos * 2 + 2);
        }
    }
    else if (pos * 2 + 1 < k && heap[pos] > heap[pos * 2 + 1])
        {
            swap(heap[pos], heap[pos * 2 + 1]);
    }
}
void inserare(int nr)
{

    heap[k] = nr;
    k++;
    up(k - 1);
}

int extragere()
{
    int r = heap[0];
    swap(heap[0], heap[k - 1]);
    k--;
    down(0);
    return r;
}

void build(int v)
{   
    for (int i = 0; i < n; i++)
        if (heap[0] < v[i])
        down(i);
}
int main()
{   
    cin >> n >> k;
   
    for (int i = 0; i < k; i++)
    {
        cin >> v[i];
    }
    heap[0] = v[0];
    for (int i = 1; i < n; i++)
        heap[i] = (v[1] * heap[i - 1] + v[2]) % v[3];
    build(v);
    while (k)
    {
        cout << extragere() << ' ';
    }
    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
