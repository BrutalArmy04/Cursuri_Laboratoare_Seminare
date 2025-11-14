#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <set>
#include <string>
using namespace std;

int main() {
    //Problema 1
    /*vector <int> v;
      int n, k;
    cin >> n >> k;
    for(int i=0 ; i<n ; i++){
        int x; 
        cin >>x;
        v.push_back(x);
    }    
    
    make_heap(v.begin(), v.end());
    vector<int> x;
    for (int i= 0; i < k; i++){
        pop_heap(v.begin(), v.end()); 
        x.push_back(v.back()); 
        v.pop_back(); 
        
    }
    
    reverse(x.begin(), x.end());
    
    for(int num : x) {
        cout << num << " ";
    }
    cout << '\n';
*/
//Problema 2
/*int Q;
    cin >> Q;
    set<int> d;
    for (int i = 0; i < Q; ++i) {
        int cmd;
        cin >> cmd;
        if (cmd == 0) {
            int x;
            cin >> x;
            d.insert(x);
        } else if (cmd == 1) {
            int x;
            cin >> x;
            if (d.find(x) != d.end()) {
                cout << "DA" << endl;
            } else {
                cout << "NU" << endl;
            }
        } else if (cmd == 2) {
            for (int x : d) {
                cout << x << " ";
            }
            cout << endl;
        }
    }
    */
    //Problema 3
   /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    /*unordered_map<string, pair<string, int>> m; 
    unordered_map<string, int> t;   
    int n;
    cin >> n;
    string cmd;

    for (int i = 0; i < n; ++i) {
        cin >> cmd;

        if (cmd == "ADD") {
            string titlu, categorie;
            int k;
            cin >> titlu >> categorie >> k;

            if (m.count(titlu)) {
                if (m[titlu].first != categorie) {
                    cout << "INVALID\n";
                } else {
                    m[titlu].second += k;
                    t[categorie] += k;
                }
            } else {
                m[titlu] = {categorie, k};
                t[categorie] += k;
            }

        } else if (cmd == "REMOVE") {
            string titlu;
            int k;
            cin >> titlu >> k;

            if (m.count(titlu)) {
                string categorie = m[titlu].first;
                int &cnt = m[titlu].second;

                if (cnt <= k) {
                    t[categorie] -= cnt;
                    m.erase(titlu);
                } else {
                    cnt -= k;
                    t[categorie] -= k;
                }
            }

        } else if (cmd == "CHECK") {
            string titlu;
            cin >> titlu;

            if (m.count(titlu)) {
                cout << m[titlu].first << "\n";
            } else {
                cout << "NU\n";
            }

        } else if (cmd == "COUNT") {
            string categorie;
            cin >> categorie;

            if (t.count(categorie)) {
                cout << t[categorie] << "\n";
            } else {
                cout << "0\n";
            }
        }
    }*/
    return 0;
}


 








    