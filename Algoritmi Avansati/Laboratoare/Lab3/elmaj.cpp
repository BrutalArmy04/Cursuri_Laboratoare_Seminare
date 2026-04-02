#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

int main() {
    freopen("elmaj.in", "r", stdin);
    freopen("elmaj.out", "w", stdout);

    int n;
    if (scanf("%d", &n) != 1 || n == 0) {
        printf("-1\n");
        return 0;
    }

    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &v[i]);
    }

    srand(time(NULL));
    int prag = n / 2 + 1;

    for (int step = 0; step < 20; ++step) {
        int idx = ((rand() << 15) ^ rand()) % n;
        if (idx < 0) idx += n; 

        int candidat = v[idx];
        int aparitii = 0;

        for (int i = 0; i < n; ++i) {
            if (v[i] == candidat) {
                aparitii++;
            }
        }

        if (aparitii >= prag) {
            printf("%d %d\n", candidat, aparitii);
            return 0;
        }
    }

    printf("-1\n");
    return 0;
}