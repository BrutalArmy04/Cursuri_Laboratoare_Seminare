#include <iostream>
using namespace std;


// Structura pentru a grupa datele unui spectacol
struct Spectacol {
    int id;
    int start; 
    int final; };


int main() {
    int n;
    Spectacol S[100]; 
    cin >> n;
    for (int i = 0; i < n; i++) {
        S[i].id = i + 1; // Salvăm numărul spectacolului (1, 2, 3...)
        cin >> S[i].start >> S[i].final;
    }


    // Sortare crescătoare după ora de final (Metoda Bulelor)
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (S[j].final > S[j+1].final) {
                // Interschimbăm structurile complet
                Spectacol aux = S[j];
                S[j] = S[j+1];
                S[j+1] = aux;
            }
        }
    }


    // Pasul Greedy: Alegem primul spectacol (cel care se termină cel mai repede)
    cout << "Spectacolele alese sunt ";
    int ultimul_f = S[0].final;
    cout << S[0].id << " ";
    int count = 1;


    // Verificăm restul spectacolelor
    for (int i = 1; i < n; i++) {
        // Dacă spectacolul curent începe după sau exact când se termină ultimul ales
        if (S[i].start >= ultimul_f) {
            cout << S[i].id << " ";
            ultimul_f = S[i].final; // Actualizăm ora de final curentă
            count++;
        }
    }


    cout << "\nNumarul de spectacole este " << count << "\n";


    return 0;
}
