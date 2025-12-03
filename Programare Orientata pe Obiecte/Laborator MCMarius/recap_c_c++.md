## Introducere/recapitulare C și C++

Limbajul C++ a apărut prin anii 1979-1985, inițial ca o extensie a limbajului C.

Limbajul C a apărut prin anii 1969-1973 ca o îmbunătățire a limbajului B. Limbajul B este o versiune
"simplificată" a limbajului BCPL pentru a ocupa mai puțină memorie ca să aibă loc pe unele calculatoare
de atunci (8 KB). BCPL a apărut la sfârșitul anilor 1960.

#### De ce a fost nevoie de noi limbaje?

Pentru **tipuri de date mai sigure** prin care descriem ce vrem să implementăm. Cu cât punem mai multe informații
despre tipurile de date în cod, cu atât mai mult ne poate ajuta compilatorul să ne semnaleze situațiile când
tipurile de date nu se potrivesc. Asta înseamnă **mai puține bug-uri**.

În limbajele B și BCPL, singurul tip de date era "word" (echivalent cu word-ul hardware din assembly),
adică un număr care poate fi tratat ori ca întreg, ori ca adresă de memorie în funcție de context.

Limbajul C a adăugat mai multe tipuri de date pentru verificarea corectitudinii
tipurilor de date de către compilator.

C++ oferă siguranță și mai mare a tipurilor de date prin cât mai multe verificări
efectuate la pasul de compilare.

#### De ce au (avut) succes C și C++?

C++ a devenit popular datorită C. C a devenit foarte popular datorită legăturii strânse cu **Unix**.
Alte aspecte de interes: **portabilitate, eficiență și performanță**, adică nu trebuie scris cod specific
pentru fiecare arhitectură, consumă puține resurse și merge repede. La vremea când au apărut aceste limbaje,
alternativele pentru cod eficient erau limbajele de asamblare și... cam atât.

Fortran este performant, însă este util doar pentru calcule numerice. C și C++ sunt pentru uz general.

De ce C și nu Pascal? C a apărut din nevoi practice (pentru a rescrie Unix din limbaj de asamblare în C pentru
a fi portabil) și a fost foarte util pentru industrie și cercetare; Pascal a fost creat inițial doar ca
instrument de învățare și nu a avut succes pe termen lung.

#### Ce dezavantaj are acest succes al C și C++?

Trebuie păstrată **compatibilitatea cu versiuni mai vechi** (backwards compatibility).
Codul scris acum câteva zeci de ani ar trebui
să compileze fără (prea multe) modificări și cu versiuni mai noi de compilatoare.

La vremea când a apărut limbajul C, deja erau multe programe scrise în B și BCPL.

Anumite reguli ale limbajului C sunt o consecință a nevoii de a face programe scrise în B și BCPL să
funcționeze în continuare și în C fără prea multe modificări.

Întrucât C++ a fost dezvoltat într-o primă fază ca extensie a limbajului C, și C++ a preluat reguli bizare.

#### De ce C++ e din ce în ce mai complicat?

Cu fiecare versiune, C++ adaugă noi funcționalități pentru a remedia problemele istorice sau alte probleme
introduse în versiuni anterioare.

Cu toate acestea, trebuie păstrată în mare parte compatibilitatea cu versiuni mai vechi de C++ pentru că
altfel nu putem folosi biblioteci externe dezvoltate acum multe zeci de ani.
De asemenea, costul pentru a rescrie diverse biblioteci ar fi prea mare.

#### De ce învățăm C++ în 202x?

~~Pentru că așa e programa.~~ Pentru că nici alternativele nu sunt mai grozave. C++ are avantajul
că este general și e mai ușor ulterior să treci la ceva mai specific.

Dezavantajul este că C++ este _prea_ general. Evident, e mai greu să înveți ceva general decât ceva specific.

[//]: # (
Întrebarea mai bună nu ar fi de ce facem C++ la OOP, ci de ce la specializarea Informatică nu se mai face C.
)

#### Încă mai este C++ un limbaj relevant în 202x?

Încă este
[folosit](https://survey.stackoverflow.co/2025/technology#most-popular-technologies-language-prof),
chiar un pic în creștere față de anii trecuți (2022: 20.17%, 2023: 20.21%, 2024: 20.3%, 2025: 21.8%). Continuă să fie în top 5 în mai multe
clasamente. Versiunile de C++ moderne (>=11) sunt relevante.

Dacă e să ne luăm după anumite sondaje ([2021](https://www.jetbrains.com/lp/devecosystem-2021/cpp/),
[2022](https://www.jetbrains.com/lp/devecosystem-2022/cpp/), [2023](https://www.jetbrains.com/lp/devecosystem-2023/cpp/) - sursa Jetbrains; [2025](https://isocpp.org/files/papers/CppDevSurvey-2025-summary.pdf) - sursa IsoCPP),
doar ~~6%~~ ~~3.4%~~ ~~4.56%~~ 2.9% mai folosesc versiuni vechi de C++ și nu vor să treacă pe versiuni mai noi.

### Noțiuni de bază din C și C++

Rulați exemplele următoare, vedeți ce se întâmplă, apoi faceți câteva modificări, vedeți din nou ce se întâmplă
și încercați să înțelegeți de ce merge sau de ce nu merge.

Orice cod compilat de C/C++ poate fi încadrat în două categorii: executabile sau biblioteci.

Un executabil trebuie să aibă o singură funcție numită `main` care întoarce un număr întreg (`int`). Dacă
executabilul a rulat cu succes, se va întoarce 0.
```c++
int main() {
    return 0;
}
```

Strict pentru funcția `main` există o regulă specială și putem să nu mai punem `return 0` la sfârșit:
```c++
int main() {}
```

**Pentru toate celelalte funcții care nu sunt `void`, trebuie obligatoriu să avem `return` pe toate ramurile
de execuție! Altfel... 🔥️**

#### Spații de nume (namespaces)

Spațiile de nume (namespaces) grupează diverse componente legate între ele sub un singur nume pentru a evita
conflicte de nume cu alte componente din alt spațiu de nume.

**Evitarea conflictelor** este principalul beneficiu al spațiilor de nume. Clauzele `using namespace` elimină
această separare logică și favorizează apariția conflictelor de nume. În acest caz, degeaba mai avem namespaces
dacă punem totul la grămadă.

**Toți** identificatorii din [această listă](https://en.cppreference.com/w/cpp/symbol_index) devin
vizibili în fișierul în care scriem `using namespace std` și în **toate fișierele** care includ acest fișier
în mod direct sau **indirect**.

Din acest motiv, nu voi folosi `using namespace std;`. Nu vreau să îmi pierd timpul cu erori ușor de prevenit.

Singurele excepții sunt namespace-urile mici, de exemplu `using namespace std::literals;`.

**Nu folosiți `using namespace std;` în fișiere header!** În fișierele .cpp nu prea contează, dar prefer să
folosesc aceleași convenții peste tot. Detalii la secțiunea despre etapele compilării.

Detalii din surse de încredere:
[aici](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-using-directive) și
[aici](https://isocpp.org/wiki/faq/coding-standards#using-namespace-std).

**Exemplu**

Echipa A definește o funcție `scrie` și folosește spațiul de nume `EchipaA`. Prin urmare, numele complet al
funcției va fi `EchipaA::scrie`.

Echipa B definește o funcție `scrie` și folosește spațiul de nume `EchipaB`. Prin urmare, numele complet al
funcției va fi `EchipaB::scrie`. Funcția aceasta nu are vreo legătură cu `EchipaA::scrie`, doar se nimerește
să aibă același nume.

Echipa C are nevoie de funcționalități dezvoltate de ambele echipe A și B. Dacă echipa C folosește clauze
`using namespace`, va pierde mult timp să depaneze situația și să elimine conflictele, întrucât mesajele de
eroare din C++ în caz de coliziuni de nume pot fi kilometrice.

#### Variabile

O variabilă este caracterizată de:
- nume
- tip de date: `int`, `double`, definit de noi [etc.](https://en.cppreference.com/w/c/language/type)
- valoarea reținută
- adresa de memorie unde se află variabila
- `sizeof`
- scop: blocul de acolade cel mai aproape de definiția variabilei
- durată: "locală", "globală" (în ghilimele pentru că nu e prea corect, dar lăsăm așa momentan)

Am pus link către tipurile de date predefinite din C deoarece în C++ sunt enorm de multe
tipuri de date predefinite.

Putem afla adresa unei variabile `x` folosind `&x`.

```c++
#include <iostream>

int main() {
    int x = 10, y = -5;
    double z = 1.1;

    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
    x = x - 3;
    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
    ++x; // x = x + 1;
    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";

    std::cout << "Variabila y are valoarea " << y << " și se află la adresa " << &y << "\n";
    y -= 4; // y = y - 4;
    std::cout << "Variabila y are valoarea " << y << " și se află la adresa " << &y << "\n";

    std::cout << "Variabila z are valoarea " << z << " și se află la adresa " << &z << "\n";
    z *= 3.3; // z = z * 3.3;
    std::cout << "Variabila z are valoarea " << z << " și se află la adresa " << &z << "\n";

    {
        int x = 100;
        std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
    }
    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
}
```

Pentru orice tip de date putem folosi operatorul `sizeof` ca să aflăm câți bytes ocupă o variabilă declarată
cu acel tip de date. Putem aplica `sizeof` și pe o variabilă, dar va fi luat în considerare tipul de date.
`sizeof` este determinat la compilare.

```c++
#include <iostream>

int main() {
    std::cout << "Pe acest mediu de lucru, sizeof(int) este " << sizeof(int) << "\n";
    std::cout << "Pe acest mediu de lucru, sizeof(long) este " << sizeof(long) << "\n";
    std::cout << "Pe acest mediu de lucru, sizeof(double) este " << sizeof(double) << "\n";
}
```

Ce se înțelege prin mediu de lucru?

Sistem de operare, compilator, procesor.

**Înainte de a folosi valoarea unei variabile** (pentru calcule, afișări etc.),
**orice variabilă trebuie inițializată!**

Implicit, variabilele au o valoare nedeterminată, inițializate cu ce se găsește prin memorie. Din acest motiv,
putem considera că de fapt nu sunt inițializate. Variabilele de tipuri primitive (`int`, `double` etc.)
nu sunt inițializate implicit cu zero deoarece acest proces este considerat costisitor în lumea C/C++.

Totodată, utilizarea variabilelor neinițializate este o cauză de defecte (bug-uri) foarte frecventă.

Pentru a încerca să prevenim astfel de defecte (și nu numai), va trebui să ținem cont de warnings și să le
eliminăm. Oricum nu avem de ales 😉️

#### Pointeri 👻

Am văzut mai devreme că putem afla adresa unei variabile `x` folosind `&x`. Ce tip de date are expresia `&x`?

Dacă `x` este de tip `int`, atunci `&x` are tipul de date `int*`. Putem să declarăm o variabilă de tip `int*`
pe care o vom folosi să reținem adrese de variabile de tip `int`:

```c++
#include <iostream>

int main() {
    int x = 10, y = -5;
    double z = 1.1;

    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
    std::cout << "Variabila y are valoarea " << y << " și se află la adresa " << &y << "\n";
    std::cout << "Variabila z are valoarea " << z << " și se află la adresa " << &z << "\n";

    int* ptr = &x;
    std::cout << "Variabila ptr are valoarea " << ptr << " și se află la adresa " << &ptr << "\n";
    ptr = &y;
    std::cout << "Variabila ptr are valoarea " << ptr << " și se află la adresa " << &ptr << "\n";
    // ptr = &z; // eroare: ptr știe să rețină doar adrese de `int`, nu și adrese de `double`
}
```

Variabila `ptr` este un **pointer** la `int`, având tipul de date `int*`.

La rândul său, și variabila `ptr` este reținută undeva în memorie, deci îi putem afla adresa cu `&ptr`. Am
putea reține această adresă folosind o variabilă de tip `int**`. O astfel de variabilă ar fi pointer la `int*`.

Tipurile de date `int*` și `int**` sunt două tipuri de date distincte.

**Ce mai putem face cu pointerii?**

Putem afla valoarea reținută de variabila a cărei adrese e reținută de pointer.
Procesul se numește dereferențiere.

**Surse majore de bug-uri: dereferențierea unui pointer invalid!**

**Exemple: pointer neinițializat, pointer nul, pointer agățat (dangling pointer).**

Un pointer agățat înseamnă că la un moment dat era pointer valid, însă nu mai este (de exemplu, este
reținută adresa unei variabile care a fost distrusă).

```c++
#include <iostream>

int main() {
    int x = 10, y = -5;

    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
    std::cout << "Variabila y are valoarea " << y << " și se află la adresa " << &y << "\n";

    int* ptr = &x;
    std::cout << "Variabila ptr are valoarea " << ptr << " și se află la adresa " << &ptr << "\n";
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";
    x += 5;
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";

    ptr = &y;
    std::cout << "Variabila ptr are valoarea " << ptr << " și se află la adresa " << &ptr << "\n";
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";
    y = 3;
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";
    
    {
        int h;
        h = 4;
        ptr = &h;
    }
    // ptr este acum dangling pointer!!!
    // eroare!!! // std::cout << "Prin dereferențierea ptr obținem valoarea " << *ptr << "\n";

    ptr = nullptr; // ptr este acum nul!!!
    // eroare!!! // std::cout << "Prin dereferențierea ptr obținem valoarea " << *ptr << "\n";
    int* ptr2; // ptr2 este neinițializat!!!
    // eroare!!! // std::cout << "Prin dereferențierea ptr2 obținem valoarea " << *ptr2 << "\n";
}
```

Putem modifica valoarea unei variabile în mod indirect, prin intermediul unui pointer.

```c++
#include <iostream>

int main() {
    int x = 10, y = -5;

    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
    std::cout << "Variabila y are valoarea " << y << " și se află la adresa " << &y << "\n";

    int* ptr = &x;
    std::cout << "Variabila ptr are valoarea " << ptr << " și se află la adresa " << &ptr << "\n";
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";
    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";
    *ptr += 5;
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";
    std::cout << "Variabila x are valoarea " << x << " și se află la adresa " << &x << "\n";

    ptr = &y;
    std::cout << "Variabila ptr are valoarea " << ptr << " și se află la adresa " << &ptr << "\n";
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";
    std::cout << "Variabila y are valoarea " << y << " și se află la adresa " << &y << "\n";
    *ptr = 3;
    std::cout << "Prin dereferențierea variabilei ptr obținem valoarea " << *ptr << "\n";
    std::cout << "Variabila y are valoarea " << y << " și se află la adresa " << &y << "\n";
}
```

Cât ocupă un pointer?

Depinde de mediul de lucru. De obicei, ocupă 4 sau 8 bytes, indiferent de tipul de pointer.

```c++
#include <iostream>

int main() {
    std::cout << "Pe acest mediu de lucru, sizeof(int*) este " << sizeof(int*) << "\n";
    std::cout << "Pe acest mediu de lucru, sizeof(int**) este " << sizeof(int**) << "\n";
    std::cout << "Pe acest mediu de lucru, sizeof(int***) este " << sizeof(int***) << "\n";
    std::cout << "Pe acest mediu de lucru, sizeof(long*) este " << sizeof(long*) << "\n";
    std::cout << "Pe acest mediu de lucru, sizeof(double*) este " << sizeof(double*) << "\n";
}
```

Mai multe detalii despre sizeof-uri [aici](https://en.cppreference.com/w/cpp/language/types#Data_models).

#### Funcții

Cel mai simplu tip de funcție: o funcție care nu primește parametri și nu întoarce nimic.
```c++
#include <iostream>

void f() {
    std::cout << "f()\n";
}

int main() {
    f();
}
```

În C, parametrii se pot transmite doar prin valoare. În C++, parametrii se pot transmite prin valoare sau prin
referință.

La transmiterea parametrilor prin valoare, se creează câte o copie locală pentru fiecare parametru, iar
acea copie există numai în corpul funcției respective. Modificările făcute în interiorul funcției asupra
parametrilor transmiși prin valoare nu se vor vedea în afara funcției:
```c++
#include <iostream>

void f(int x) {
    std::cout << "f: x: " << x << "\n";
    ++x;
    std::cout << "f: x: " << x << "\n";
}

int main() {
    int x;
    x = 2;
    std::cout << "main: x: " << x << "\n";
    f(x);
    std::cout << "main: x: " << x << "\n";
}
```

Desigur, nu era nevoie ca ambele variabile să se numească `x`.

Următorul exemplu folosește tot transmitere prin valoare:
```c++
#include <iostream>

void f(int* ptr) {
    std::cout << "f: *ptr: " << *ptr << "\n";
    ++(*ptr);
    std::cout << "f: *ptr: " << *ptr << "\n";
}

int main() {
    int x;
    x = 2;
    std::cout << "main: x: " << x << "\n";
    f(&x);
    std::cout << "main: x: " << x << "\n";
}
```

De ce este transmitere prin valoare? Să facem câteva modificări:
```c++
#include <iostream>

void f(int* ptr) {
    std::cout << "f: *ptr: " << *ptr << ", ptr: " << ptr << "\n";
    ++(*ptr);
    std::cout << "f: *ptr: " << *ptr << ", ptr: " << ptr << "\n";
    int z = 10;
    ptr = &z;
    std::cout << "f: *ptr: " << *ptr << ", ptr: " << ptr << "\n";
}

int main() {
    int x;
    int* ptr;
    x = 2;
    ptr = &x;
    std::cout << "main: x: " << x << ", *ptr: " << *ptr << ", ptr: " << ptr << "\n";
    f(ptr);
    std::cout << "main: x: " << x << ", *ptr: " << *ptr << ", ptr: " << ptr << "\n";
}
```

De ce există referințe și transmitere prin referință în C++?

Deoarece C++ vrea să fie un limbaj mai sigur, iar pointerii ar trebui întotdeauna inițializați ca să nu avem
bug-uri. Totuși, C++ nu a vrut să modifice semantica pointerilor pentru că altfel ar fi pierdut compatibilitatea
cu limbajul C.

Prin urmare, a fost introdus un nou tip de date care să fie ca pointerii, nepermițând lipsa inițializării. De
asemenea, referințele nu pot fi nule prin definiție. Mai mult, odată ce au fost inițializate, referințele nu
pot arăta către altă variabilă (pentru a nu arăta către ceva invalid - dangling pointer).

Astfel, se poate spune și că referințele sunt un alias sau un alt nume pentru o variabilă. Adresa unei
referințe este de fapt adresa variabilei spre care arată referința.

Putem observa că modificările asupra variabilei transmise prin referință sunt vizibile după apelul funcției:
```c++
#include <iostream>

void f(int& ref) {
    std::cout << "f: ref: " << ref << ", &ref: " << &ref << "\n";
    ++ref;
    std::cout << "f: ref: " << ref << ", &ref: " << &ref << "\n";
    int z = 10;
    ref = z; // nu se modifică variabila către care arată ref
             // se atribuie 10 (valoarea lui z) variabilei referite
    std::cout << "f: ref: " << ref << ", &ref: " << &ref << "\n";
}

int main() {
    int x;
    // int& ref; // eroare - nu este inițializată la declarare!
    int& ref = x;
    x = 2;
    std::cout << "main: x: " << x << ", ref: " << ref << ", &ref: " << &ref << "\n";
    f(x);
    std::cout << "main: x: " << x << ", ref: " << ref << ", &ref: " << &ref << "\n";
}
```

La întoarcerea din funcții prin valoare se efectuează o copie a variabilei din clauza `return`.

La întoarcerea din funcții prin referință **nu se efectuează copieri. Prin urmare, NU întoarcem referințe
la variabile locale, deoarece acele variabile nu vor mai exista!**

Vom avea aceeași eroare și dacă întoarcem prin valoare un pointer care reține adresa unei variabile locale.

#### Definire vs declarare

Prin definirea unei variabile, a unei funcții sau al unui tip de date, descriem complet
variabila/funcția/tipul de date. O definiție implică automat declararea variabilei/funcției/tipului de date.
Reciproca **nu este adevărată!**

O declarare (fără definiție) doar anunță faptul că acea variabilă sau acea funcție există undeva în program.
De multe ori nu avem nevoie de definiția completă a unei funcții ca să o putem apela, deci este suficientă
declararea.

Declararea variabilelor (fără definiție) este folosită de obicei doar pentru variabile "globale". Nu intru
în detalii pentru că **nu folosim variabile globale la acest curs!**

În ceea ce privește tipurile de date, nu avem nevoie decât de declarația tipului de date dacă vom crea doar
o variabilă de tip pointer la acel tip de date (sau referință - dar referințele sunt implementate intern
prin pointeri), întrucât un pointer este simplu de construit: acesta doar reține o adresă de memorie.

De obicei toți pointerii au același `sizeof`: de obicei, acesta este 4 sau 8 bytes.

Avem nevoie de definiția completă a tipului de date numai atunci când vrem să construim o variabilă
de acel tip de date, deoarece avem nevoie de `sizeof`-ul acelui tip de date.

Momentan vom vedea exemple doar cu definiții și declarații de funcții:
```c++
#include <iostream>

void f(); // declarație fără definiție

int main() {
    // void f(); // declarație fără definiție
    f();
}
```
Putem pune declarații atât "globale", cât și locale. Declarația promite că undeva în fișierele noastre sursă
(sau în biblioteci) există definită funcția `void f()`. Prin urmare, după ce am declarat funcția, avem voie să o
apelăm.

Totuși, am mințit că există funcția `void f()` Programul a compilat, dar a crăpat la etapa de linking (legarea
tuturor surselor compilate (fișiere obiect) și bibliotecilor):
```
/usr/bin/ld: /tmp/ccYSCOlt.o: in function `main':
main.cpp:(.text+0x9): undefined reference to `f()'
collect2: error: ld returned 1 exit status
```

Odată ce am declarat o funcție, o putem apela din acel punct în jos. De definit o putem defini mai jos în
același fișier sau în alt fișier. Totuși, definiția nu trebuie să se repete.
```c++
#include <iostream>

void g() { // declarație și definiție
    // f(); // eroare: declarația lui f este valabilă doar în main!
    std::cout << "g()\n";
}

int main() {
    // f(); // eroare: f nu a fost încă declarat
    void f(); // declarație fără definiție
    f();
    g();
}

void f() {
    std::cout << "f()\n";
}
```

Nu este necesar să dăm nume parametrilor atunci când declarăm o funcție, însă este util să facem asta pentru
a documenta codul:
```c++
void f(int& numar);
// echivalent cu
void f(int&);
```

#### Citire și afișare

Pentru a putea modifica variabilele, funcțiile de citire primesc variabilele prin referință. Și funcțiile de
afișare primesc variabilele tot prin referință, dar vom vedea ulterior prin ce diferă.
```c++
#include <iostream>

int main() {
    int x;
    std::cout << "x: ";
    std::cin >> x;
    std::cout << "Am citit " << x << "\n";
}
```

Nu sunt fan citiri de la tastatură pentru că nu putem automatiza rularea/testarea codului. Consider citirile de
la tastatură o pierdere de timp. Dacă alegeți această variantă, salvați ce introduceți de la tastatură într-un
fișier, apoi puteți face copy-paste din fișier în terminal ca să nu pierdeți timpul de fiecare dată.

Din nefericire, sunt mai dificil de automatizat apăsările de taste speciale: săgeți, escape etc.

#### Fișiere
🚧

#### Instrucțiuni condiționale și repetitive

Dacă avem o singură instrucțiune, nu este nevoie de acolade. Totuși, dacă avem `if`-uri imbricate, este
bine să punem acolade ca să fie executate cum ne așteptăm ramurile `else if`/`else`.
```c++
#include <iostream>

int main() {
    int x = 3;

    if(x%3 == 0) {
        std::cout << "rest 0\n";
    }
    else if(x%3 == 1) {
        std::cout << "rest 1\n";
    }
    else {
        std::cout << "altceva\n";
    }
}
```

Instrucțiunea `switch` este similară cu `if`, doar că face numai comparații de egalitate. Poate face codul
mai ușor de citit în anumite situații, mai ales în cazul enumerărilor.

Trebuie să punem câte o instrucțiune `break` după fiecare ramură; altfel, execuția continuă pe următorul
`case`, chiar dacă nu este respectată condiția.

Putem folosi instrucțiunea specială `[[fallthrough]];` pentru a ilustra că suntem conștienți că lipsește
`break` și dorim efectul de "cascadă" (util dacă tratăm mai multe cazuri aproximativ la fel).
Altfel, vom primi warning.
```c++
#include <iostream>

int main() {
    int x = 11;

    switch(x%7) {
    case 0:
        std::cout << "rest 0\n";
        break;
    case 1:
        std::cout << "rest 1\n";
        break;
    case 2:
        std::cout << "rest 2\n";
        [[fallthrough]]; // C++17
    case 3:
        std::cout << "rest 2 sau 3\n";
        break;
    default:
        std::cout << "altceva\n";
        break;
    }
}
```

Avem 3 instrucțiuni repetitive: `for`, `while` și `do`/`while`.
```c++
#include <iostream>

int main() {
    int x = 5;
    while(x > 0) {
        std::cout << "while: x: " << x << "\n";
        --x;
    }

    do {
        std::cout << "do while 1: x: " << x << "\n";
        --x;
    } while(x > 0);

    do {
        std::cout << "do while 2: x: " << x << "\n";
        ++x;
    } while(x < 3);
    
    for(int i = 0; i < x; ++i)
        std::cout << "for 1: i: " << i << "\n";

    for(int i = x; i >= 0; --i)
        std::cout << "for 2: i: " << i << "\n";
}
```

**Atenție!** Dacă la ultimul `for` am fi folosit un tip de date fără semn (`unsigned i = x;`), codul ar fi
rulat la infinit! Dacă am vrea să folosim `unsigned`, am putea avea următorul cod:
```c++
#include <iostream>

int main() {
    for(unsigned i = 5; ; --i) {
        std::cout << "for: i: " << i << "\n";
        if(i == 0)
            break;
    }
```

Analog lui `break` avem `continue`:
```c++
#include <iostream>

int main() {
    for(unsigned i = 0; i < 4; ++i) {
        if(i < 2)
            continue;
        std::cout << "for: i: " << i << "\n";
    }
```

#### Tablouri, vectori

În C, este imposibil de făcut distincția între un pointer și un vector, deoarece vectorii sunt convertiți
la pointeri la primul element atunci când vectorii sunt transmiși unei funcții. Asta înseamnă și că nu putem
ști numărul de elemente.

În C++ avem [`std::array`](https://en.cppreference.com/w/cpp/container/array) pentru vectori de dimensiune
fixă, cunoscută la momentul compilării. De asemenea, avem
[`std::vector`](https://en.cppreference.com/w/cpp/container/vector) dacă nu știm numărul (maxim) de elemente.

Din C++17 avem funcția [`std::size`](https://en.cppreference.com/w/cpp/iterator/size) prin care putem afla
numărul de elemente și dintr-un vector clasic stil C.
Părerile sunt împărțite dacă `std::array` mai prezintă avantaje în acest context,
însă tot avem anumite limitări la vectorii stil C:
nu putem transmite unei funcții vectorul fără să specificăm numărul de elemente și nu îi putem compara cu `==`.

`std::vector` se ocupă automat de gestiunea memoriei la runtime.

```c++
#include <array>
#include <vector>
#include <iostream>

int main() {
    std::array<int, 4> arr1 = {1, -1, 42, 8};
    // std::array<int, 4> arr1{1, -1, 42, 8}; // (aproape) echivalent
    std::cout << arr1[0] << "\n";
    std::array<int, 3> arr2;
    arr2[0] = 3;
    arr2[1] = 2;
    //arr2[2] = 1;
    // arr[3] = 0; // nu se fac verificări, crapă urât la runtime, segmentation fault
    // std::get<3>(arr2) = 0; // verificare la compilare, dă eroare la compilare
    // arr2.at(3) = 0; // verificare la runtime - se aruncă excepție; detalii la tema 2
    // arr2.push_back(3); // eroare la compilare, std::array nu are funcția push_back
                          // deoarece este vector de dimensiune fixă
    std::cout << "arr1.size(): " << arr1.size() << "\n";
    std::cout << "arr2.size(): " << arr2.size() << "\n";

    std::vector<double> vec1{2.3, 1};       // [2.3, 1]  // inițializare cu acolade
    vec1.push_back(3.1);  // [2.3, 1, 3.1]  // se alocă spațiu pt elementul nou adăugat
    vec1[1] = 2;          // [2.3, 2, 3.1]  // nu se fac verificări dacă indexul 1 este valid
                          // nu se extinde spațiul, se modifică valoarea existentă
    // vec1[3] = 5;       // eroare la runtime, vectorul are spațiu alocat doar pt 3 elem
                          // nu se verifică faptul că indexul 3 nu este valid
    // vec1.at(1) = 2;    // verificare la runtime; indexul este valid, nu se aruncă excepție
    // vec1.at(3) = 5;    // verificare la runtime; indexul este invalid, se aruncă excepție
    // pt std::vector nu putem face verificări la compilare, nu avem `std::get` aici
    int x = vec1.back();  // x == 3.1
    std::cout << "x: " << x << "\n";
    vec1.pop_back();      // [2.3, 2]
    std::vector<int> vec2(3, 1); // [1, 1, 1]  // atenție, trebuie cu paranteze aici
    vec2.push_back(2);
    std::cout << "vec1.size(): " << vec1.size() << "\n";
    std::cout << "vec2.size(): " << vec2.size() << "\n";
}
```

Pentru a parcurge elementele unui `std::array`/`std::vector`, avem următoarele variante:
```c++
#include <array>
#include <vector>
#include <iostream>

int main() {
    std::array<int, 4> arr = {1, -1, 42, 8};
    for(unsigned i = 0; i < arr.size(); ++i)
        std::cout << arr[i] << " ";
    // sau
    for(auto i = 0u; i < arr.size(); ++i)
        std::cout << arr[i] << " ";
    // sau
    for(auto i = 0ull; i < arr.size(); ++i)
        std::cout << arr[i] << " ";
    std::cout << "\n";
    for(auto& elem : arr)
        std::cout << elem << " ";
    std::cout << "\n";

    std::vector<int> vec(3, 1); // [1, 1, 1]
    vec.push_back(2);
    for(unsigned i = 0; i < vec.size(); ++i)
        std::cout << vec[i] << " ";
    std::cout << "\n";
    for(const auto& elem : vec)
        std::cout << elem << " ";
    std::cout << "\n";
    
}
```

Mai este o variantă cu iteratori, însă de multe ori varianta echivalentă cu range-for este mult mai ușor
de înțeles.

Este de preferat varianta cu `for(auto& elem : arr)`, deoarece scriem mai puțin și nu apelăm funcția
`size()`/`end()` la fiecare iterație. Folosim `const` dacă nu dorim să modificăm elementele.

Este mai bine să folosim `std::array` decât vectori de dimensiune fixă din C (`int v[20]`) întrucât
nu avem nevoie de o constantă în plus pentru a reține dimensiunea (avem `.size()`) și este mai ușor
de modificat codul dacă ulterior avem nevoie să trecem la `std::vector`. De asemenea, în cazul
`std::array`, se pot face verificări la compilare dacă accesăm un index invalid.

Pentru bucle repetitive mai simple, compilatorul poate memoiza unele apeluri de funcții dacă poate
demonstra că rezultatul apelului ar fi același la fiecare iterație. Ca să fim siguri că se fac aceste
optimizări, ar trebui să ne uităm în codul de asamblare generat.

#### Tablouri asociative

Tablourile asociative se mai numesc maps, dicționare sau hashes (tabele de dispersie).
Sunt la fel ca vectorii, doar că pot fi indexați după orice tip de date, nu doar după întregi.

Pentru a putea indexa după un alt tip de date, variabilele de acel tip trebuie să poată fi
comparate prin egalitate `(operator==`) și/sau prin relații de ordine (`operator<`).

Pentru un tip de date definit de noi, începând cu C++20, putem folosi definire implicită (cu `=default`)
și compilatorul va defini operațiile în mod natural. Pentru a defini ambele operații, avem `operator<=>`.
Detalii la tema 1.

Dacă tipul de date nu are o relație de ordine, atunci folosim
[`std::unordered_map`](https://en.cppreference.com/w/cpp/container/unordered_map). Dacă avem relație de
ordine, putem folosi si [`std::map`](https://en.cppreference.com/w/cpp/container/map).

Exemplu:
```c++
#include <map>
#include <unordered_map>
#include <iostream>

int main() {
    std::map<std::string, int> note;
    note["POO"] = 10;
    note["A&G"] = 9;
    note["LFA"] = 9;
    note["BD"] = 10;
    note["TW"] = 8;
    for(const auto& [materie, nota] : note) {
        std::cout << materie << ": " << nota << "\n";
    }

    std::cout << "---------------\n";

    std::unordered_map<std::string, int> alte_note;
    alte_note["POO"] = 10;
    alte_note["A&G"] = 9;
    alte_note["LFA"] = 9;
    alte_note["BD"] = 10;
    alte_note["TW"] = 8;
    for(const auto& [materie, nota] : alte_note) {
        std::cout << materie << ": " << nota << "\n";
    }    
}

```

#### Șiruri de caractere

Șirurile de caractere sunt un dezastru și în C, și în C++. Dacă vrem să facem prelucrări corecte pe șiruri
de caractere, trebuie să folosim biblioteci specializate. C și C++ nu oferă funcții de prelucrare pentru
șiruri de caractere codificate ca UTF-8 (cel mai folosit standard din prezent (2022)).

Dacă găsiți o bibliotecă de C/C++ care știe să facă normalizări (pentru comparații de egalitate), să
aibă o interfață decentă/ușor de folosit (adică nu [ICU](https://icu.unicode.org/)) și să nu fie un chin
pasul de compilare (adică nu ICU), vă rog să îmi spuneți. Pentru prelucrări mai simple, am găsit
[utf8_string](https://github.com/Gumichan01/utf8_string) și [tiny-utf8](https://github.com/DuffsDevice/tiny-utf8).

C++ ne va provoca destule bătăi de cap, așa că nu are rost să ne punem singuri și mai multe bețe în roate.
Prin urmare, nu are rost să folosim șirurile de caractere din C și să gestionăm manual alocările de memorie.

De aceea, vom folosi [`std::string`](https://en.cppreference.com/w/cpp/string/basic_string/basic_string):
```c++
#include <string>
#include <iostream>

int main() {
    std::string str = "asd";
    str += "efg";
    std::cout << str << "\n";
    if(str == "asd")
        std::cout << "match!\n";
}
```

#### Structuri, uniuni, enumerări

La acest curs nu vom folosi structuri și uniuni. Le putem ignora.

Enumerările sunt folosite pentru a documenta codul și eventual pentru a evita constante magice:
```c++
enum Semafor { Rosu, Galben, Verde };

int main() {
    Semafor sem;
    sem = Semafor::Rosu;
    sem = Galben;
}
```

Intern, enumerările sunt întregi. Dacă nu specificăm altfel, numerotarea începe de la 0 și se
incrementează cu 1.

Dacă nu ne interesează foarte tare conversia cu numerele întregi, este mai bine să folosim `enum class`,
deoarece numele constantelor nu mai sunt globale, ci sunt localizate:
```c++
enum class Semafor { Rosu, Galben, Verde };

int main() {
    Semafor sem;
    sem = Semafor::Rosu;
    // sem = Galben; // eroare
}
```

Altă variantă ar fi să punem un `enum` simplu într-un spațiu de nume (namespace).

De obicei folosim instrucțiuni `switch` când vrem să tratăm cazurile unei enumerări, iar editoarele ne pot
avertiza dacă am uitat un caz (de exemplu dacă am adăugat ulterior un câmp în enumerare și nu avem o ramură
implicită):
```c++
#include <iostream>

enum class Semafor { Rosu, Galben, Verde };

int main() {
    Semafor sem;
    sem = Semafor::Rosu;
    switch(sem) {
        case Semafor::Rosu:
            std::cout << "ROȘU!\n";
            break;
        case Semafor::Galben:
            std::cout << "Galben!\n";
            break;
        case Semafor::Verde:
            std::cout << "Verde!\n";
            break;
        default:
            std::cout << "Defect\n";
            break;
    }
}
```

#### Alocare dinamică

În C, funcțiile standard pentru alocare/dezalocare dinamică de memorie sunt `malloc`, `realloc` și `free`.
Funcțiile `malloc`/`realloc` întorc un pointer la începutul zonei de memorie alocată, iar `free` primește
acest pointer ca să elibereze zona de memorie respectivă.

În C++ modern **nu avem nevoie de alocări dinamice explicite** dacă nu facem ceva low-level. Ne complicăm
existența inutil și putem avea tot felul de bug-uri subtile sau greu de depanat.

Biblioteca standard de C++ ne pune la dispoziție suficient de multe tipuri de date pentru a nu avea nevoie
să ne ocupăm noi explicit de gestionarea memoriei pentru situațiile uzuale. Nu are rost să reinventăm roata.

Dacă totuși dorim asta, avem `new`/`new[]` și `delete`/`delete[]`: `new`-urile întâi apelează `malloc` și apoi
constructorul/constructorii, iar `delete`-urile întâi apelează destructorul/destructorii și apoi `free`. Nu
există echivalent `realloc` în C++.

Tot ce alocăm explicit cu funcțiile/operatorii de alocare trebuie să eliberăm cu funcțiile/operatorii pereche.
În caz contrar, avem memory leaks sau alte erori de memorie.

Pentru a detecta erorile de memorie, folosim programe specializate (valgrind, GCC/Clang sanitizers).

Pe macOS ARM încă nu merge valgrind, încercați cu sanitizers.

Pe Windows există [DrMemory](https://drmemory.org) și cel puțin pe cazuri simple pare să funcționeze.
Există și sanitizers, însă doar pe [MSVC](https://docs.microsoft.com/en-us/cpp/sanitizers/asan)
și pare să detecteze mai puține erori decât pe Linux. Nu mi-a mers
[Application Verifier](https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/application-verifier),
tot cu MSVC. Nu recomand MSVC pentru că ocupă
_mult prea mult_ spațiu pe disc. Probabil se poate instala și o versiune care ocupă mai
[puțin](https://community.chocolatey.org/packages/visualstudio2022buildtools), dar nu am nervi
să testez că nu e mai puțin bloatware sau că nu cere licență de activare.

#### Directive de preprocesare

Directiva `#include` face un simplu copy-paste dintr-un fișier în altul.
Putem avea conflicte urâte dacă nu avem grijă.

Modulele au apărut în C++ de-abia din C++20, însă nu sunt implementate de toate compilatoarele și cu atât
mai puțin de majoritatea bibliotecilor externe.

Directiva `#define` face un simplu find-and-replace. O folosim doar pentru include guards (vedem la headers).

Directivele `#ifdef`/`#else`/`#endif` le folosim la include guards și pentru compilare condiționată. Noi nu
vom folosi direct compilarea condiționată, ci vom folosi biblioteci care să facă asta. De obicei, condiționăm
compilarea pentru anumite sisteme de operare sau arhitecturi de procesor.

Directivele `#pragma` sunt directive nonstandard, neportabile și depind de compilator. Totuși, pentru ce facem
noi aici, putem considera în regulă `#pragma once` ca alternativă la include guards.

#### Bibliotecile standard

Găsim documentația pentru bibliotecile standard de C și C++ pe cppreference.

Biblioteca standard de C este de obicei furnizată de sistemul de operare. Exemple: glibc sau musl pe Linux,
MSVCRT sau UCRT pe Windows. Din acest motiv, biblioteca de C nu este de obicei inclusă în executabile.
Întrucât limbajul C este relativ simplu, există numeroase implementări alternative.

De menționat că pe Windows biblioteca C poate conține telemetrie
([cel puțin prin 2015](https://levicki.net/articles/2015/12/03/RANT_Microsoft_Visual_Studio_2015.php)).

Headerele standard pentru biblioteca C sunt denumite în C sub forma `<header.h>`: `<stdio.h>`, `<stdlib.h>` etc.

În C++, headerele din biblioteca C de forma `<header.h>` sunt accesibile ca `<cheader>` deoarece sunt
incluse în spațiul de nume `std`: `<cstdio>`, `<cstdlib>` etc.


Pentru limbajul C++ nu există multe implementări "la zi" pentru C++ și biblioteca standard asociată.
Compilatoarele de C++ vin de obicei la pachet cu biblioteca standard de C++. Exemple: libstdc++ sau
libc++ pe Linux/macOS, libstdc++-6.dll pe MinGW și acele "Visual C++ Redistributable Runtime" pe MSVC.

### Despre compilarea în C și C++

După cum am spus și mai devreme, limbajele C și C++ au apărut foarte demult și au fost nevoite să păstreze
compatibilitatea cu versiuni mai vechi din motive istorice. La vremea respectivă abia erau puse la punct
fundamentele teoriei compilatoarelor.

Prin urmare, este exagerat să avem pretenția din partea C/C++ la un sistem sofisticat de separare a
codului în module sau pachete.

Un prim efort în acest sens este sistemul de module introdus în C++20. În prezent (2022), modulele nu sunt
implementate complet de toate compilatoarele principale (GCC, Clang, MSVC). Până avem module, va trebui să
ne mulțumim cu instrucțiuni de tip `#include`.

#### Fișiere header, `#include`

[//]: # (sau o referință/pointer la un tip de date)
Pentru a putea folosi o funcție
(sau [altele](https://en.cppreference.com/w/cpp/language/declarations))
definită în altă parte, este necesar să folosim o declarație. O declarație oferă minimul necesar de
informații pentru a putea apela funcția respectivă: numărul și tipurile de date ale parametrilor și
tipul de date întors de funcție.

Teoretic am putea scrie toate declarațiile de funcții de care avem nevoie fără să folosim fișiere header
și instrucțiuni `#include`, însă ar fi foarte repetitiv. Fișierele de tip header au rolul de a grupa
logic diverse declarații.

Instrucțiunea `#include` (sub formele `#include "header"` și `#include <header>`) nu face altceva decât
să copieze conținutul fișierului `header` în locul respectivului `#include`. Nu se întâmplă nimic special,
deștept sau spectaculos, este doar copy-paste de text.

Macroinstrucțiunile (`#include` și nu numai) se aplică succesiv până când nu mai este nimic de înlocuit.

Fișierul rezultat după înlocuirea succesivă a tuturor instrucțiunilor de tip `#include` poartă numele de
**translation unit** (TU). De obicei ne referim la fișiere sursă (cpp-uri) când vorbim despre TU.

Fișierele header din bibliotecile standard conțin multe declarații și poate fi mai greu de urmărit ce se
întâmplă, așa că vom folosi exemple mai simple.

Avem fișierul "header.h":
```c++
void f();
int g(char x);
int g(double x);
int g(double x, int y);
void h(int& z);
```

În fișierul "sursa.cpp" vom pune un `#include` (presupunem că funcțiile sunt definite în alt fișier sursă):
```c++
#include "header.h"

int main() {
    f();
    int a = g('x');
    a = g(3.0);
    a = g(2.0, 5);
    h(a);
}
```

Dacă folosim compilatorul GCC (sau Clang), avem opțiunea `-E` pentru a vedea modificările asupra fișierului
după etapa de preprocesare (`g++ -E sursa.cpp`):
```c++
# 1 "sursa.cpp"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "sursa.cpp"
# 1 "header.h" 1
void f();
int g(char x);
int g(double x);
int g(double x, int y);
void h(int& z);
# 2 "sursa.cpp" 2

int main() {
    f();
    int a = g('x');
    a = g(3.0);
    a = g(2.0, 5);
    h(a);
}
```

Dacă punem de două ori include, se va copia de două ori conținutul fișierului header:
```c++
// sursa.cpp
#include "header.h"
#include "header.h"

int main() {
    f();
    int a = g('x');
    a = g(3.0);
    a = g(2.0, 5);
    h(a);
}
```

Iar apoi `g++ -E sursa.cpp`:
```c++
# 1 "sursa.cpp"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "sursa.cpp"
# 1 "header.h" 1
void f();
int g(char x);
int g(double x);
int g(double x, int y);
void h(int& z);
# 2 "sursa.cpp" 2
# 1 "header.h" 1
void f();
int g(char x);
int g(double x);
int g(double x, int y);
void h(int& z);
# 3 "sursa.cpp" 2

int main() {
    f();
    int a = g('x');
    a = g(3.0);
    a = g(2.0, 5);
    h(a);
}
```

Așadar, implicit nu există vreun mecanism de verificare că am inclus deja un header. Desigur, este foarte
puțin probabil să includem explicit un header de mai multe ori, însă un header poate fi inclus de mai multe
ori în mod indirect:
```c++
// un_header.h
#include "header.h"

// alt_header.h
#include "header.h"

// sursa.cpp
#include "un_header.h"
#include "alt_header.h"
```

În cazul funcțiilor, repetarea declarațiilor nu ne deranjează. Totuși, există situații când vrem să avem
definiția unei funcții într-un fișier header:
```c++
// header.h
int f(int x) {
    return x%2 == 0 ? 42 : x;
}
```

Dacă nu mai punem nimic în header și îl includem de două ori (sau folosim fișierele header definite mai sus),
atunci vom primi eroare la compilare. Fișierul "sursa.cpp" este:
```c++
// sursa.cpp
#include "header.h"
#include "header.h"

int main() {
    int a = f(2);
    a = f(a);
}
```

Vom primi eroarea:
```
$ g++ sursa.cpp -o sursa
In file included from sursa.cpp:2:
header.h:1:5: error: redefinition of ‘int f(int)’
    1 | int f(int x) { return x%2 == 0 ? 42 : x; }
      |     ^
In file included from sursa.cpp:1:
header.h:1:5: note: ‘int f(int)’ previously defined here
    1 | int f(int x) { return x%2 == 0 ? 42 : x; }
      |     ^
```

De ce se întâmplă asta? Să vedem cu `g++ -E sursa.cpp`:
```c++
# 1 "sursa.cpp"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "sursa.cpp"
# 1 "header.h" 1
int f(int x) {
    return x%2 == 0 ? 42 : x;
}
# 2 "sursa.cpp" 2
# 1 "header.h" 1
int f(int x) {
    return x%2 == 0 ? 42 : x;
}
# 3 "sursa.cpp" 2

int main() {
    int a = f(2);
    a = f(a);
}
```

Ce putem face ca să prevenim astfel de probleme dacă un header este inclus de mai multe ori? Folosim un include
guard (soluția standard) sau `#pragma once` (nu este la fel de portabilă, însă în unele situații poate fi mai
rapidă). Un include guard arată în felul următor:
```c++
#ifndef HEADER_H
#define HEADER_H

// conținutul fișierului header

#endif // HEADER_H
```

De exemplu, fișierul nostru "header.h" de mai sus va deveni:
```c++
#ifndef HEADER_H
#define HEADER_H

int f(int x) {
    return x%2 == 0 ? 42 : x;
}

#endif // HEADER_H
```

Iar apoi "sursa.cpp" va arăta astfel după preprocesare (`g++ -E sursa.cpp`)`:
```c++
# 1 "sursa.cpp"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "sursa.cpp"
# 1 "header.h" 1



int f(int x) {
    return x%2 == 0 ? 42 : x;
}
# 2 "sursa.cpp" 2


int main() {
    int a = f(2);
    a = f(a);
}
```

Dezavantajul este că trebuie să avem grijă să nu avem coliziuni de nume cu macro-urile definite. O convenție
uzuală folosită și de IDE-uri este ca define-ul să aibă numele căii fișierului relativ la rădăcina proiectului.

Deși nu ar fi întotdeauna necesar, o convenție este să avem perechi de fișier header - fișier sursă și să
includem fișierul header în fișierul sursă:
```c++
// func.h
#ifndef FUNC_H
#define FUNC_H

int f(int x);

#endif // FUNC_H


// func.cpp
#include "func.h"

int f(int x) {
    return x%2 == 0 ? 42 : x;
}
```

#### Fișiere de tip header și clase

Definiția unei clase trebuie să fie completă ca să putem construi obiecte din acea clasă. Pe scurt și un pic
simplificat, o clasă este definită complet dacă putem determina `sizeof`-ul unui obiect.

Pentru a putea determina `sizeof`-ul unui obiect, trebuie să avem tipurile complete pentru toate atributele
care nu sunt referințe sau pointeri. De asemenea, trebuie să avem toate declarațiile funcțiilor membru.

Asta înseamnă că trebuie să avem `#include`-uri pentru toate tipurile de date care nu sunt referințe sau
pointeri, inclusiv dacă folosim acele tipuri de date ca parametri sau ca tip de retur.

Pentru tipurile de date de tip referințe sau pointeri, avem nevoie de o pre-declarare (forward declaration)
dacă nu putem oferi definiția completă. Această pre-declarare anunță existența tipului respectiv de date,
însă oferă numai o definiție incompletă.

Exemplu:
```c++
// facultate.h
#ifndef FACULTATE_H
#define FACULTATE_H

// avem nevoie de acest #include deoarece avem un obiect complet
// de tip std::string, nu pointer sau referință
#include <string>

class Facultate {
    std::string nume;
};

#endif // FACULTATE_H
```

Dacă în clasa `Student` avem nevoie doar de o referință sau de un pointer la `Facultate`, atunci este suficient
să pre-declarăm clasa sau să precizăm explicit că este vorba de o clasă:
```c++
// student.h
#ifndef STUDENT_H
#define STUDENT_H

class Facultate; // anunțăm că Facultate este o clasă

class Student {
    Facultate& facultate;
};

#endif // STUDENT_H
```

Sau:
```c++
// student.h
#ifndef STUDENT_H
#define STUDENT_H

class Student {
    class Facultate& facultate;
};

#endif // STUDENT_H
```

Ca fapt divers, este antipattern să avem (de obicei) atribute de tip referință.
Detalii [aici](https://lesleylai.info/en/const-and-reference-member-variables/).
Eventual de citit și de [aici](https://quuxplusone.github.io/blog/2022/01/23/dont-const-all-the-things/) despre `const`.

În schimb, dacă dorim să construim un obiect complet, atunci trebuie să includem header-ul:
```c++
// student.h
#ifndef STUDENT_H
#define STUDENT_H

#include "facultate.h"

class Student {
    Facultate facultate;
};

#endif // STUDENT_H
```

Alt exemplu de pre-declarații:
```c++
// student.h
#ifndef STUDENT_H
#define STUDENT_H

#include <iosfwd>

class Student {
public:
    friend std::ostream& operator<<(std::ostream& os, const Student& st);
};

#endif // STUDENT_H
```

Am putea include `<ostream>` sau `<iostream>`, însă minimal avem pre-declarațiile de care avem nevoie în
fișierul header `<iosfwd>`.

#### Include tot ce folosești - IWYU (Include what you use)

Chiar dacă pe unele compilatoare se include indirect `<iosfwd>` când includem `<string>`
(sau se include indirect `<string>`când includem `<iostream>`), este recomandat să punem include-uri
explicite pentru toate definițiile/declarațiile necesare și să nu ne bazăm pe detaliile de implementare
ale unor compilatoare (sau pe include-uri indirecte pentru dependențe directe în fișierul curent).

C++ nu are extrem de multe [fișiere header predefinite](https://en.cppreference.com/w/cpp/header), iar
editorul ne ajută de obicei cu ce trebuie sau ne putem uita pe cppreference când avem nevoie.

Pe de altă parte, nu este în regulă să folosim fișiere header monolitice (de exemplu un header care include
toate fișierele header din biblioteca standard), deoarece creștem aiurea timpul de compilare și includem
în multe locuri și ce nu avem nevoie.

Într-un viitor mai mult sau mai puțin îndepărtat vom putea folosi
[IWYU](https://github.com/include-what-you-use/include-what-you-use). Momentan (2022) are prea multe bug-uri.

Într-un viitor probabil la fel de îndepărtat, vom putea folosi module de C++20.

#### Regula unei singure definiții (ODR - One definition rule)

[ODR](https://en.cppreference.com/w/cpp/language/definition#One_Definition_Rule)
ne spune că o definiție trebuie să apară **o singură dată** într-un translation unit. Dacă o definiție apare
de mai multe ori în fișiere sursă diferite, atunci definiția trebuie să fie **identică** peste tot unde apare.

Într-un fișier sursă (sau mai exact, într-un translation unit), o definiție trebuie să apară **o singură dată**.

Dacă avem definiții în fișiere header, acel header poate fi inclus în mai multe translation units fără probleme,
deoarece definiția va fi identică.

Exemplu:
```c++
// header.h
#ifndef HEADER_H
#define HEADER_H

int f(int x) {
    return x%2 == 0 ? 42 : x;
}

#endif // HEADER_H


// sursa1.cpp
#include "header.h"

// sursa2.cpp
#include "header.h"
```

Chiar dacă ne apare de două ori definiția funcției `f` în program, ODR nu este încălcată, întrucât definiția este
identică. Avem nevoie de include guards (sau `#pragma once`) pentru a nu ne apărea o definiție de mai multe ori
în cadrul aceluiași translation unit.

#### Compilare și linking

Dacă vă interesează, etapele compilării sunt cele de
[aici](https://en.cppreference.com/w/cpp/language/translation_phases).

Pe scurt, se întâmplă următoarele:
- se procesează succesiv toate directivele de preprocesare (de exemplu `#define` și `#include`)
- fiecare fișier sursă este compilat într-un fișier obiect
- toate fișierele obiect sunt legate (linking) pentru a forma un fișier executabil

De obicei nu apelăm compilatorul explicit, ci folosim un instrument de build din următoarele motive:
- portabilitate
- recompilarea fișierelor modificate, nu tot codul
- (re)compilare în paralel
- compilarea dependențelor externe

Câteva observații de interes:
- în CMakeLists.txt, fișierele sursă sunt adăugate de obicei în comanda `add_executable`
- etapa de compilare până la linking se poate executa în paralel pentru fiecare fișier sursă în parte
- dacă nu s-au modificat fișierele header incluse de un fișier sursă și nici fișierul sursă, atunci acel
fișier sursă nu mai trebuie recompilat (de obicei)
- există un abuz de limbaj frecvent folosit:
  - când spunem compilare, de obicei ne referim la compilare _și_ linking deși sunt două programe diferite
  - atunci când vrem să facem distincția între cele două, menționăm și linker-ul
- în limba română, corect este "dependență", nu "dependință"; "dependință" înseamnă încăpere

În mod obișnuit, etapa de linking nu poate fi executată în paralel. Dacă vrem să putem face asta, avem
nevoie de [instrumente specializate](https://github.com/rui314/mold).

#### Diverse

[//]: # (fapt divers inutil: literalul pentru zero este în baza 8.)

[//]: # (https://stackoverflow.com/questions/53315710/trigraphs-in-a-comment-converted-in-c11-ignored-in-c17)