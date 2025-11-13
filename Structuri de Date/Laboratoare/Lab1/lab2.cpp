/*
#include <iostream>

using namespace std;

// Stiva
struct nod
{
    int val;
    nod *next;
};

nod *head = NULL;

void insert(int val)
{
    if (head == NULL)
    {
        nod *ins = new nod();
        ins->val = val;
        ins->next = NULL;
        head = ins;
    }
    else
    {
        nod *ins = new nod();
        ins->val = val;
        ins->next = head;
        head = ins;
    }
}

int pop()
{
    int cop_int = head->val;
    nod *cop_nod = head->next;
    delete head;
    head = cop_nod;
    return cop_int;
}

// coada
struct nodD
{
    int val;
    nodD *next, *prev;
};

nodD *headD = NULL, *tailD = NULL;

void insertD(int val)
{
    if (headD == NULL)
    {
        nodD *ins = new nodD();
        ins->next = NULL;
        ins->prev = NULL;
        ins->val = val;
        headD = ins;
        tailD = ins;
    }
    else
    {
        nodD *ins = new nodD();
        ins->val = val;
        ins->next = headD;
        ins->prev = NULL;
        headD->prev = ins;
        headD = ins;
    }
}

int popD()
{
    int cop_int = tailD->val;
    nodD *cop_prev = tailD->prev;
    delete tailD;
    tailD = cop_prev;
    if (tailD != NULL)
        tailD->next = NULL;
    return cop_int;
}

int main()
{
    insertD(5);
    insertD(4);
    insertD(1);
    insertD(2);
    insertD(3);
    cout << popD() << '\n'
         << popD() << '\n'
         << popD() << '\n'
         << popD() << '\n'

*/





/*



#include <iostream>
using namespace std;

struct nod
{
    int val;
    nod *next;
};

nod* head;

void insert(int val)
{
    nod* ins = new nod();
    ins->val = val;
    if (head == NULL)
    {
        ins->next = NULL;
    }
    else
    {
        ins->next = head;
    }
    head = ins;
}

int pop()
{
    int cop_val = head->val;
    nod* cop_nod = head->next;
    delete head;
    head = cop_nod;
    return cop_val;
}

struct nodD
{
    int val;
    nodD *next, *prev;
};

nodD *headD = NULL, *tailD = NULL;

void insertD(int val)
{
    nodD *ins = new nodD();
    ins->val = val;
    if (headD == NULL)
    {
        ins->next = NULL;
        ins->prev = NULL;
        tailD = ins;
    }
    else
    {
        ins->next = headD;
        ins->prev = NULL;
        headD->prev = ins;
    }
    headD = ins;
}

int popD()
{
    int cop_val = tailD->val;
    nodD *cop_prev = tailD->prev;
    delete tailD;
    tailD = cop_prev;
    if (tailD != NULL)
        tailD->next = NULL;
    return cop_val;
}

int main()
{
    insertD(5);
    insertD(4);
    insertD(1);
    insertD(2);
    insertD(3);
    cout << popD() << '\n'
         << popD() << '\n'
         << popD() << '\n'
         << popD() << '\n';

}
*/
#include <iostream>
using namespace std;


struct nodD
{
    int val;
    nodD *next, *prev;
};

nodD *headD = NULL, *tailD = NULL;

void insertD(int val)
{
    nodD *ins = new nodD();
    ins->val = val;
    if (headD == NULL)
    {
        ins->next = NULL;
        ins->prev = NULL;
        tailD = ins;
    }
    else
    {
        ins->next = headD;
        ins->prev = NULL;
        headD->prev = ins;
    }
    headD = ins;
}

int popD()
{
    int cop_val = tailD->val;
    nodD *cop_prev = tailD->prev;
    delete tailD;
    tailD = cop_prev;
    if (tailD != NULL)
        tailD->next = NULL;
    return cop_val;
}
/*The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain. */
void insert_sort()
{
    nodD *current = headD ->next;
    while (current != NULL)
    {
        nodD *next = current->next;
        nodD *prev = current->prev;
        while (prev != NULL && prev->val > current->val)
        {
            prev = prev->prev;
        }
        if (prev == NULL)
        {
            current->next = headD;
            headD->prev = current;
            headD = current;
            current->prev = NULL;
        }
        else
        {
            current->next = prev->next;
            if (prev->next != NULL)
                prev->next->prev = current;
            prev->next = current;
            current->prev = prev;
        }
        current = next;
}}

void print()
{
    nodD *current = headD;
    while (current != NULL)
    {
        cout << current->val << " ";
        current = current->next;
    }
    cout << endl;
}

int main()
{
    insertD(5);
    insertD(4);
    insertD(1);
    insertD(2);
    insertD(3);
    insert_sort();
    print();
    
}

/*
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("pb1_colocviu.in");
    std::vector<int> v;
    int n; fin>>n;
    int k; fin>>k;
    for(int i=0 ; i<n ; i++){
        int x; fin >>x;
        v.push_back(x);
    }    
    for(auto& x : v)
        cout << x << " ";
    cout << '\n';
    
    std::make_heap(v.begin(), v.end());

    for (int i= 0; i < k; i++){
        std::pop_heap(v.begin(), v.end()); //mută maximul la final, dar nu îl șterge
        cout << v.back() << " ";
        v.pop_back(); //terge ultimul element (care a fost mutat de pop_heap)
    }
    cout << '\n';

    return 0;
}
*/

/*#include <iostream>   
#include <set>        
#include <string>     
#include <fstream>
int main() {
    std::ifstream fin("pb2.in");
    int n;                       
    fin >> n;

    std::set<int> arbori;      

    for (int i = 0; i < n; ++i) {
        std::string op;  //numele operației: Adauga/Cauta/Arata
        fin >> op;

        if (op == "Adauga") {
            int x;
            fin >> x;
            arbori.insert(x);   
        }
        else if (op == "Cauta") {
            int x;
            fin >> x;
            std::cout << (arbori.count(x) ? "DA" : "NU") << '\n';
        }
        else if (op == "Arata") {
            bool first = true;
            for (int x : arbori) {
                if (!first) std::cout << ' ';
                std::cout << x;
                first = false;
            }
            std::cout << '\n';
        }
    }
    return 0;
}*/

/*#include <iostream>
#include <unordered_map>
#include <string>
#include <fstream>

using namespace std;

unordered_map<string, pair<string, int>> titluri; // titlu -> (categorie, nr exemplare)
unordered_map<string, int> total_per_categorie;   // categorie -> total exemplare

int main() {
    ifstream fin("pb3.in");
    int n;
    fin >> n;
    string cmd;

    for (int i = 0; i < n; ++i) {
        fin >> cmd;

        if (cmd == "ADD") {
            string titlu, categorie;
            int k;
            fin >> titlu >> categorie >> k;

            if (titluri.count(titlu)) {
                if (titluri[titlu].first != categorie) {
                    cout << "INVALID\n";
                } else {
                    titluri[titlu].second += k;
                    total_per_categorie[categorie] += k;
                }
            } else {
                titluri[titlu] = {categorie, k};
                total_per_categorie[categorie] += k;
            }

        } else if (cmd == "REMOVE") {
            string titlu;
            int k;
            fin >> titlu >> k;

            if (titluri.count(titlu)) {
                string categorie = titluri[titlu].first;
                int &cnt = titluri[titlu].second;

                if (cnt <= k) {
                    total_per_categorie[categorie] -= cnt;
                    titluri.erase(titlu);
                } else {
                    cnt -= k;
                    total_per_categorie[categorie] -= k;
                }
            }

        } else if (cmd == "CHECK") {
            string titlu;
            fin >> titlu;

            if (titluri.count(titlu)) {
                cout << titluri[titlu].first << "\n";
            } else {
                cout << "NU\n";
            }

        } else if (cmd == "COUNT") {
            string categorie;
            fin >> categorie;

            if (total_per_categorie.count(categorie)) {
                cout << total_per_categorie[categorie] << "\n";
            } else {
                cout << "0\n";
            }
        }
    }
    return 0;
}*/