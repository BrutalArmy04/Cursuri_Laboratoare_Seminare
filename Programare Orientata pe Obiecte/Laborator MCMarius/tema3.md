# Tema 3

Scopul ultimei teme este utilizarea unor noțiuni mai avansate de OOP (principii SOLID, design patterns) și a programării
generice.

[//]: # (nitpick: ar fi mai corect să spunem șabloane de funcții și șabloane de clase; este abuz de limbaj)

### Cerințe
- minim o funcție șablon și o clasă șablon (template)
    - modificați o clasă existentă care este ceva mai izolată de celelalte
      (să nu aveți foarte mult de modificat) și transformați-o în clasă template
    - adăugați (minim) un atribut de tip `T` sau care depinde de `T`
    - adăugați (minim) o funcție membru care să depindă de `T` (sau de alt parametru template);
    - adăugați (minim) o funcție normală/liberă template; poate să fie `friend`
- minim 2 design patterns (3 dacă aveți singleton sau ceva la fel de simplu și proiectul e simplu);
  **utilizarea acestor design patterns ar trebui să aibă sens**

Observații:
- desigur, pt nota 10 trebuie să nu fie warnings sau erori de memorie
- nu ar trebui să vă ia mai mult de câteva ore (cel mult 8-9 aș zice)
- puteți folosi și alte design patterns pe lângă cele prezentate aici
- aceste patterns se pot combina între ele și au numeroase variațiuni

Pentru lista completă a cerințelor, vezi [template-ul de proiect](../tema-1/README#template-proiect).

#### Termen limită
- săptămâna 11 (18 decembrie/14 mai): progres parțial
- **săptămâna 12 (22 decembrie/21 mai): tema 3 gata**
- săptămâna 13 (15 ianuarie/28 mai): (eventuale) modificări în urma feedback-ului

Orice funcționalitate în plus e luată în considerare pentru puncte bonus, inclusiv la temele din urmă.
Nota maximă este 12.

-----

## Principiile SOLID

Principiile SOLID sintetizează câteva recomandări pentru a scrie cod OOP ușor de întreținut și de extins.

- **S**: Single responsibility principle
- **O**: Open-closed principle
- **L**: Liskov substitution principle
- **I**: Interface segregation principle
- **D**: Dependency inversion principle

Să le luăm pe rând.

**S**-ul din SOLID ne spune că nu trebuie să avem o clasă care face prea multe lucruri. Este de preferat să
avem mai multe clase mici decât o singură clasă mare cu multe funcții și atribute. Prin izolarea diverselor
funcționalități în clase separate, codul este mai ușor de depanat, de refactorizat și de testat.

Dacă o clasă are mai mult de 5-10 funcții publice (în aplicații mai mari 1-3 funcții publice), cel mai
probabil clasa face prea multe și ar trebui restructurat codul în mai multe clase/module ajutătoare. Dacă o
funcție are mai mult de ~60-100 de rânduri (să încapă pe un ecran fără să facem prea mult scroll), probabil
trebuie împărțită în funcții mai mici. Trebuie găsit un echilibru ca să nu ajungem în extrema cealaltă cu
multe funcții foarte mici (over-engineering).

**O**-ul din SOLID se referă la faptul că ce implementăm ar trebui să fie "open for extension, closed for
modification". Partea cu "open" înseamnă că este ușor să adăugăm noi funcționalități. Partea cu "closed"
înseamnă că nu ar trebui să schimbăm codul/comportamentul existent dacă o funcție/clasă/modul depinde de
acest cod.

Cu alte cuvinte, să nu stricăm ce merge deja. Atunci când adăugăm o nouă derivată, nu ar trebui să avem
nevoie să schimbăm codul în clasa de bază sau în derivate.

**L**-ul din SOLID zice că orice obiect de tip clasă de bază ar trebui să poată fi substituit (înlocuit) cu
un obiect din orice derivată a acelei clase de bază fără ca funcționalitatea să fie alterată. Un obiect de
clasă derivată _este un fel de_ obiect de clasă de bază.

Derivatele noi nu ar trebui să fie complet diferite de clasa de bază. O încălcare a acestui principiu este
problema cu [cercul și elipsa](https://en.wikipedia.org/wiki/Circle%E2%80%93ellipse_problem).

**I**-ul din SOLID seamănă într-un fel cu **S**-ul. Ideea ar fi să nu avem interfețe prea complicate sau
prea generale ca să avem cât mai puține situații de felul "unde dai și unde crapă". Dacă interfețele sunt
cât de cât specifice, defectele sunt ușor de identificat pentru că afectează o mică parte din cod.

**D**-ul din SOLID ne spune să ne bazăm pe interfețe, nu pe detalii de implementare. Am respectat acest
principiu când am vorbit despre interfețe non-virtuale. Clasele derivate lasă clasa de bază să definească
interfața. Poate să fie dificil la început să ne "inversăm" modul de gândire de până acum, dar ideea de
interfață non-virtuală ar trebui să ne ghideze.

## Design patterns

În continuare, prezint câteva exemple de design patterns care s-ar putea potrivi și care nu sunt foarte complicate.

### Singleton

Context: avem nevoie de un singur obiect dintr-o anumită clasă, deoarece nu are rost să avem mai multe obiecte de acest fel.

Exemplu: un obiect care gestionează o aplicație/un joc
```c++
class application {
private:
    application() = default;
public:
    application(const application&) = delete;
    application& operator=(const application&) = delete;
    static application& get_app() {
        static application app;
        return app;
    }
};

// mod de utilizare
auto& x = application::get_app();
```

**⚠ Atenție!** Inițializarea atributelor statice trebuie pusă într-un **singur** fișier .cpp, deoarece
inițializarea trebuie făcută o singură dată. Fișierele .cpp sunt compilate o singură dată, dar fișierele
`.h` sunt incluse de alte fișiere `.h`/`.cpp` și atunci ar apărea inițializarea de mai multe ori.

### Object pool

Context: avem un număr limitat de obiecte care trebuie refolosite. De obicei este folosit pentru refolosirea
conexiunilor la un server. Poate fi considerat un fel de generalizare a singleton-ului: un connection_pool
cu o singură conexiune poate fi privit ca un singleton.

Exemplu cu conexiuni; `connection_pool` poate la rândul său să utilizeze `singleton`; după ce o conexiune
nu mai e folosită, se apelează `close`:
```c++
class connection {
private:
    bool opened = false;
public:
    void open() { opened = true; }
    bool free() const { return !opened; }
    void close() { opened = false; }
    ~connection() { close(); }
};

class connection_pool {
private:
    static const int max_conns = 5;
    std::vector<connection> conns{max_conns};
public:
    connection& get_conn() {
        for(auto& conn : conns)
            if(conn.free()) {
                conn.open();
                return conn;
            }
        throw std::runtime_error("too many open connections!");
    }
};

// mod de folosire
connection_pool pool;
try {
    connection& c = pool.get_conn();
    auto data = fetch_data(c); // presupunem că am definit funcția aceasta
    std::cout << data;
} catch(std::runtime_error& err) { std::cout << err.what() << "\n"; }
```

**Builder**

Context: limitare a limbajului C++. Funcțiile au doar argumente poziționale, nu și argumente de tip dicționar
(sau cheie-valoare). Dacă nu vrem să inițializăm toate atributele, nu putem folosi argumente implicite dacă
ne interesează doar argumentele "de la sfârșit".

Exemplu:
```c++
class dulap {
    int nr_rafturi;
    int nr_sertare;
    std::string tip_maner;
    std::string tip_balama;
friend class dulap_builder;
public:
    dulap() = default;
};

class dulap_builder {
private:
    dulap d;
public:
    dulap_builder() = default;
    dulap_builder& nr_rafturi(int nr) {
        d.nr_rafturi = nr;
        return *this;
    }
    dulap_builder& nr_sertare(int nr) {
        d.nr_sertare = nr;
        return *this;
    }
    dulap_builder& tip_maner(const std::string& tip) {
        d.tip_maner = tip;
        return *this;
    }
    dulap_builder& tip_balama(const std::string& tip) {
        d.tip_balama = tip;
        return *this;
    }
    dulap build() {
        return d;
    }
};

// mod de folosire
dulap_builder b;
dulap d = b.nr_rafturi(5).tip_balama("clasic").build();
```

Observații:
- în funcția `build` putem arunca o excepție dacă obiectul este invalid (de exemplu, lipsește ușa)
- putem introduce o funcție sau o clasă suplimentară pentru a reseta obiectul intern (sau putem face
  asta în funcția `build`) ca să putem folosi același `builder` pentru a construi mai multe obiecte

Tehnica prin care înlănțuim apeluri și întoarcem un nou obiect (nu neapărat `this`) la modul general
se numește method chaining și este foarte utilă în anumite situații.

Alte utilizări (nu depind de limbaj): evaluare leneșă a unor expresii, tratarea erorilor cu tipuri
de date rezultat.

Exemplu: construirea unor cereri (SQL) în mod dinamic. Adăugăm pe parcurs mai multe clauze
(`where`, `join` etc.), însă nu ar fi eficient să facem câte o cerere la baza de date la fiecare pas.
Astfel, acumulăm condițiile într-o variabilă internă și efectuăm cererea efectivă cu toate condițiile
acumulate de-abia "la sfârșit", în momentul în care avem nevoie de rezultate.

### Factory

Context: obiectul are foarte multe atribute (să zicem 5+, foarte comun în aplicații medii/mari) și
nu ne interesează să le setăm pe fiecare în parte. Se folosește de obicei la testarea automată:
dorim să obținem o instanță a obiectului "repede", fără să ne preocupe foarte tare ce "conține".

Exemplu:
```c++
class scaun {
    int nr_picioare;
    bool spatar;
    std::string material;
public:
    scaun(int nrPicioare, bool spatar, std::string material)
    : nr_picioare(nrPicioare), spatar(spatar), material(std::move(material)) {}};

class scaun_factory {
public:
    static scaun taburet() { return scaun(4, false, "lemn"); }
    static scaun taburet_simplu() { return scaun(3, false, "lemn"); }
    static scaun scaun_de_lemn() { return scaun(4, true, "lemn"); }
    static scaun scaun_de_metal() { return scaun(4, true, "metal"); }
    static scaun scaun_modern() { return scaun(2, true, "metal"); }
};

// mod de folosire
scaun s = scaun_factory::taburet();
```

Observații:
- putem modifica să întoarcem smart pointers
- putem combina pattern-ul cu un builder
- putem folosi factories abstracte pentru a crea familii de obiecte legate între ele:
  - avem
    - `class A {}; class A1 : public A {}; class A2 : public A {};`
    - `class B {}; class B1 : public B {}; class B2 : public B {};`
  - `Factory` este o interfață care întoarce pointeri la `A` și `B` (factory abstract)
  - `Factory1 : public Factory` construiește `A1`, `B1`
  - `Factory2 : public Factory` construiește `A2`, `B2`
  - în `main` inițializăm un factory concret, apoi putem lucra cu referință/pointer la `Factory` și astfel ascundem tipurile concrete (`A1` și `B1` de exemplu)
  - exemplu cu baze de date:
    - `A` și `B` ar putea fi adaptor (pt conexiuni), statement_generator
    - `A1` și `B1` (`A2` cu `B2` etc.) sunt clase concrete pentru o bază de date anume (exemple: MySQL, Oracle, PostgreSQL, SQLite, SQL Server)
    - restul codului va interacționa doar cu pointeri la `A` și `B` pe care îi putem obține cu ajutorul unui factory abstract

### Proxy

Context: avem nevoie de o interfață pentru alte obiecte. Exemple: abstractizarea codului din alte limbaje/module, restricționarea accesului, testarea automată.

Exemplu:
```c++
class postare {
public:
    void citeste() {}
    void scrie() {}
    void modifica() {}
    void ascunde() {}
    void sterge() {}
};

class user {};
class auth {
    user u;
public:
    auth(const user& u) : u(u) {}
};

class postare_proxy {
private:
    postare p;
    auth a;
public:
    postare_proxy(const postare& p, const auth& a) : p(p), a(a) {}
    void citeste() {
        if(a.are_voie())
            p.citeste();
    }
    // restul funcțiilor publice din postare (cele de interes) sunt adăugate și în proxy
};
```

Observații:
- de ce nu am făcut verificarea direct în clasa `postare`? deoarece fiecare clasă ar trebui să facă un singur lucru (iar pe acela să îl facă bine)

### Alte design patterns de adăugat/completat

#### Decorator

Scop simplificat: reprezentăm un obiect într-un mod diferit.

Din ce am văzut în (prea) multe locuri, pare destul de standard să păstrezi interfața obiectului pe care
îl decorezi. Cu toate acestea, eu nu am avut de folosit în practică decoratorii în acest fel 🙃

Pe scurt:
```c++
class abc {
    // atribute
};

class abc_decorator {  // : public abc dacă vrem să păstrăm interfața obiectului inițial
    abc ob;  // sau pointer la abc/pointer la bază
public:
    // adăugăm noi funcționalități
    std::string& to_csv() { /* ... */ }
    std::string& to_json() { /* ... */ }
}
```

Patterns asemănătoare: adapter, facade.

#### Strategy

TL;DR interfață comună pentru diverși algoritmi/variante ale aceluiași algoritm.

#### Null object

Un eventual alt mod de a "trata" erori. În loc să folosim `nullptr` sau coduri de retur, continuăm să
folosim obiectul într-un lanț de apeluri, iar apelurile respective nu vor face nimic în caz de erori.
E un fel de proxy care ignoră apelurile invalide. Dacă vreți, poate să semene un pic și cu înlănțuirea din builder.

```c++
obiect ob;
obiect_wrapper ow(ob);

ow.f();
ow.g();  // <--- acest apel "crapă", dar putem continua execuția normal
ow.h();

// alternativ
ow.f().g().h();  // ob.g() crapă
```

Clase ajutătoare în C++: [`std::optional`](https://en.cppreference.com/w/cpp/utility/optional),
[`std::variant`](https://en.cppreference.com/w/cpp/utility/variant).

## Templates

Pentru motivație etc, citiți cursul. Această secțiune conține câteva exemple care mi s-au părut
relevante/utile și arată modul în care putem folosi fișiere separate pentru templates.

Atunci când instanțiem o clasă template, trebuie să fie generată definiția concretă a funcției/clasei
pentru tipul instanțiat. Din acest motiv, în locul în care instanțiem cu un tip concret o funcție sau
o clasă template este necesar să avem definiția completă, nu doar declarația.

Cu alte cuvinte, avem nevoie de ce aveam până acum în .cpp, nu doar ce aveam în header. De aceea,
mai ales pentru biblioteci este de preferat o variantă header-only.

În varianta 1 (vezi mai jos), putem păstra organizarea în fișiere separate, iar din perspectiva
compilatorului e ca și cum ar fi header-only. Avantajul este că nu trebuie să declarăm în avans
tipurile concrete (ar putea fi o infinitate). Dezavantajul este că fiecare funcție/clasă este
(re)compilată de fiecare dată când instanțiem template-ul și trebuie să recompilăm toate
fișierele care includ header-ul atunci când modificăm ceva la implementarea template-ului.

În varianta 2 (vezi mai jos), împărțirea este la fel ca înainte, însă dezavantajul este acela că trebuie
să declarăm în mod explicit funcțiile/clasele toate tipurile de date pentru care avem nevoie de templates. 
Avantajul de la varianta 2 este acela că dacă modificăm implementarea, nu trebuie să recompilăm
fișierele care includ header-ul.

Așadar, avem de ales între mai multă flexibilitate (varianta 1) și timp mai mic de compilare (varianta 2).

Pentru situațiile întâlnite aici, putem folosi fie `<class T>`, fie `<typename T>`, este același lucru.
La versiuni mai vechi ale limbajului există situații când merge doar cu `typename` sau doar cu `class`,
însă nu ne vom întâlni cu ele (sper).
Important este să le folosim pe cât posibil în mod consistent, peste tot la fel.


### Funcții template

#### Varianta 1

O variantă organizată ca header și cpp, dar dpdv al compilatorului tot header-only:
```c++
// sursa.h
#ifndef SURSA_H
#define SURSA_H

template <typename T>
void f(T x);

#include "sursa.cpp"
#endif

/////////////////////////

// sursa.cpp
// ATENȚIE: FĂRĂ #include "sursa.h"
#include <iostream>

template <typename T>
void f(T x) {
    std::cout << x;
}

/////////////////////////

// main.cpp
#include "sursa.h"

int main() {
    f<int>(5);
}
```

Iar în CMakeLists.txt avem:
```cmake
# ...
add_executable(oop main.cpp)
# ...
```

**ATENȚIE!** În această variantă **nu** trebuie să punem `sursa.cpp` în sistemul de build (Makefile/CMakeLists.txt etc.)!

**ATENȚIE!** Nu includem sursa.h în sursa.cpp dacă alegem această abordare. De ce?

Pentru fiecare loc unde includem `sursa.h`, se va include automat și implementarea, iar în fișierul respectiv există
definiția completă a clasei/funcției template și se face de fiecare dată instanțiere de templates. Acesta este și
motivul pentru care codul de C++ care folosește multe templates durează mult de compilat.

#### Varianta 2

Dacă alegem să împărțim codul ca până acum în header și cpp, este **obligatoriu** să adăugăm la sfârșitul
fișierului cpp declarații cu **toate** tipurile concrete folosite în restul surselor.

Dacă nu adăugăm aceste declarații, vom primi erori de linker de felul următor:
```
/usr/bin/ld: /tmp/ccEk3rHM.o: in function `main':
main.cpp:(.text+0xe): undefined reference to `void f<int>(int)'
collect2: error: ld returned 1 exit status
```

Avem această eroare deoarece compilatorul are nevoie de definiția completă a funcției/clasei template
atunci când are de instanțiat parametrul de template cu un tip concret (există o infinitate de
tipuri concrete).

O abordare echivalentă este să facem un fișier sursă care să conțină doar declarațiile
cu tipuri concrete (`sursa_impl.cpp` în exemplul de mai jos).

```c++
// sursa.h
#ifndef SURSA_H
#define SURSA_H

template <typename T>
void f(T x);

#endif

/////////////////////////

// sursa.cpp
#include "sursa.h"
#include <iostream>

template <typename T>
void f(T x) {
    std::cout << x;
}

/////////////////////////

// sursa_impl.cpp
#include "sursa.cpp"

template
void f<int>(int x);

/////////////////////////

// main.cpp
#include "sursa.h"

int main() {
    f<int>(5);
}
```

Iar în CMakeLists.txt avem:
```cmake
# ...
add_executable(oop main.cpp sursa_impl.cpp)
# add_executable(oop main.cpp sursa.cpp) # sau așa dacă punem declarațiile pentru tipuri concrete tot în sursa.cpp
# ...
```

Observații:
- în `sursa_impl.cpp` trebuie să adăugăm declarații pentru **toate** tipurile pe care le folosim peste tot unde includem `sursa.h`
- este suficient să adăugăm `sursa_impl.cpp` în sistemul de build (Makefile/CMakeLists.txt etc.), nu și `sursa.cpp`


#### Funcție de afișat colecții din STL

Întrucât există mai multe (prea multe?) moduri de a afișa o colecție, afișarea nu este implementată.

**Atenție!** Din cauza ODR (one definition rule), problema cu a ne defini noi `operator<<` ca funcție
de sine stătătoare este aceea că altcineva nu va mai putea rescrie afișarea în alt mod.

De aceea, e de preferat să ne punem datele într-o clasă wrapper și să facem `operator<<` pe această clasă wrapper.

Totuși, clasa wrapper e mai complicat de făcut ca să meargă și pentru colecții de colecții. Așadar,
în exemplul următor ne vom limita la o funcție de sine stătătoare.

```c++
#include <iostream>
#include <vector>

template <typename T>
std::enable_if_t<!std::is_convertible_v<T, std::string>, std::ostream&>
operator<<(std::ostream& os, const T& obj) {
    os << "[";
    for(auto iter = obj.begin(); iter != obj.end(); ++iter) {
        os << *iter;
        if(iter == obj.end())
            break;
        os << ", ";
    }
    os << "]";
    return os;
}


class abc {
public:
    friend std::ostream& operator<<(std::ostream& os, const abc&) { os << "abc"; return os; }
};

int main() {
    auto vec = std::vector<std::vector<int>>{{1, 2, 3, 4, 5, 6, 7}, {3, 4, 5, 6, 7, 8}};
    auto v2 = std::vector<abc>{{}, {}};
    std::cout << vec << "\n" << v2 << "\n";
}
```

Observații:
- dacă nu adăugăm rândul cu `std::enable_if`, atunci avem ambiguitate cu `operator<<` definit pentru `std::string`, deoarece `std::string` este iterabil (are `begin` și `end`)
- [`std::is_convertible<From, To>`](https://en.cppreference.com/w/cpp/types/is_convertible) este un template pentru verificare la momentul compilării dacă From poate fi convertit la To
- `std::is_convertible<From, To>::value` va întoarce `true` dacă această conversie este posibilă
- `std::is_convertible_v<From, To>` este o scurtătură pentru `std::is_convertible<From, To>::value` (C++17)
- [`std::enable_if<bool, T>`](https://en.cppreference.com/w/cpp/types/enable_if) este un template care elimină generarea unor definiții de funcții/clase dacă valoarea primului parametru este `false`
- în situația în care condiția este adevărată, `std::enable_if<bool, T>::type` va întoarce `T`
- `std::enable_if_t<bool, T>` este o scurtătură pentru `std::enable_if<bool, T>::type` (C++14)
- în cazul nostru, va întoarce tipul de retur pentru `operator<<`, adică `std::ostream&`
- în acest mod, nu mai generăm definiția și pentru `std::string`, deci nu mai apar ambiguități
- am pus o condiție în plus pentru a nu mai afișa ultima virgulă; acesta este motivul pentru care nu am folosit `for(const auto& elem : obj)`
  - am fi putut lua ultimul element și să comparăm cu acela, însă asta ar necesita ca elementele să fie comparabile

Metoda prin care compilatorul continuă substituirea lui T cu tipuri concrete și nu dă erori de compilare, deși a găsit și tipuri care nu se potrivesc, se numește [SFINAE](https://en.cppreference.com/w/cpp/language/sfinae) (substitution failure is not an error).

În cazul în care avem foarte multe elemente, am dori să optimizăm afișarea pentru a limita consumul de resurse:
```c++
#include <iostream>
#include <vector>

template <typename T>
std::enable_if_t<!std::is_convertible_v<T, std::string>, std::ostream&>
operator<<(std::ostream& os, const T& obj) {
    os << "[";
    int nr = 0;
    for(auto iter = obj.begin(); iter != obj.end(); ++iter) {
        os << *iter;
        ++nr;
        if(iter == obj.end())
            break;
        os << ", ";
        if(nr >= 5) {
            os << "...";
            break;
        }
    }
         
    os << "]";
    return os;
}

int main() {
    auto vec = std::vector<std::vector<int>>{{1, 2, 3, 4, 5, 6, 7}, {3, 4, 5, 6, 7, 8}};
    std::cout << vec << "\n";
}
```

În C++20 putem să scriem într-un mod un pic mai elegant constrângerea pentru tipuri. Headerele și funcția main rămân la fel:
```c++
template <typename T> requires (!std::convertible_to<T, std::string>)
std::ostream& operator<<(std::ostream& os, const T& obj) {
    os << "[";
    for(const auto& elem : obj)
        os << elem << " ";
    os << "]\n";
    return os;
}
```

Dacă dorim să marcăm în mod explicit constrângerea pentru colecție, putem proceda în felul următor:
```c++
template <typename T>
concept Container = requires(T v) {
    std::begin(v);
    std::end(v);
};

template <Container T> requires (!std::convertible_to<T, std::string>)
std::ostream& operator<<(std::ostream& os, const T& obj) {
    os << "[";
    for(const auto& elem : obj)
        os << elem << " ";
    os << "]\n";
    return os;
}
```

#### Funcții cu număr variabil de argumente

```c++
#include <string>
#include <iostream>

class elem {};

class abc {
    abc() = default;
    abc(int) { std::cout << "constr int\n"; }
    abc(std::string, int) { std::cout << "constr string int\n"; }
    abc(elem) { std::cout << "constr elem\n"; }
public:
    template <typename... Args>
    static abc create(Args&&... args) {
        return abc(std::forward<Args>(args)...);
    }
};

int main() {
    abc::create(1);
    abc::create(elem{});
}
```

Observații:
- poate fi util când avem mulți constructori, însă vrem să restricționăm crearea de obiecte
  (exemplu: object pool de mai sus)
- smart pointerii funcționează similar pentru a putea apela constructorii
- nu putem folosi fișiere separate deoarece nu este rezonabil să declarăm în avans toate combinațiile de apeluri
- dacă vreți totuși să lucrați cu fișiere separate, fie scrieți funcția cu nr variabil de argumente în header,
  fie includeți cpp-ul în header (vezi la începutul secțiunii cu funcții template)

#### Expresii de tip fold (C++ 17)

[Documentație](https://en.cppreference.com/w/cpp/language/fold).

```c++
#include <iostream>

template <typename T>
void print(std::ostream& os, const T& elem) { os << elem << " "; }

template <typename... Args>
void afis(Args... args) {
    (std::cout << ... << args) << "\n";
    // (std::cout.operator<<(args), ...) << "\n"; // (1)
    // (..., std::cout.operator<<(args)) << "\n"; // (2)
    (print(std::cout, args), ...);
    std::cout << "\n";
    (..., print(std::cout, args));
    std::cout << "\n";
}

int main() {
  afis(1, 2, 3, 4);
  afis("a", 3);
}
```

Observații:
- pentru `std::cout << ... << args` "expansiunea" se face astfel:
  - `(std::cout << ... ) << args`, adică
  - `(std::cout << ... ) << 4`, adică
  - `((std::cout << ... ) << 3) << 4`, adică
  - `(((std::cout << ... ) << 2) << 3) << 4`, adică
  - `((((std::cout <<   1 ) << 2) << 3) << 4`
  - întâi se evaluează `std::cout << 1` care întoarce noul stream, care va deveni argument pentru `std::cout << 2` etc.
- dacă punem pe dos, ce se întâmplă?
  - `std::cout << args << ...`, adică
  - `std::cout << (args << ...), adică
  - `std::cout << (1  << (2 << ...))`, adică
  - `std::cout << (1  << (2 << ( 3 << ...)))`, adică
  - `std::cout << (1  << (2 << ( 3 << 4  )))`, adică... facem shiftare pe biți și o să vedem doar un număr foarte mare
- dacă ne definim o clasă proprie pentru care definim `operator<<` și încercăm afișarea, rândurile cu (1) și (2)
  nu vor mai merge deoarece compilatorul se va uita doar la definițiile din interiorul clasei `std::ostream`,
  nu și la funcțiile friend
- din cauza modului în care se realizează expansiunea argumentelor, nu putem adăuga spații în mod direct
- acesta este motivul pentru care am definit separat funcția `print`, iar apelurile se vor realiza în felul următor:
  - `(print(std::cout, args), ...)`, adică
  - `(print(std::cout, 1), ...)`, adică
  - `(print(std::cout, 1), (print(std::cout, 2), ...))`, adică...
  - și, cu toate acestea, se va afișa `1 2 3 4`
  - de ce? parantezele ar zice pe dos; așa funcționează
    [operatorul virgulă](https://en.cppreference.com/w/cpp/language/operator_other#Built-in_comma_operator):
    întâi se evaluează expresia din stânga, abia apoi expresia din dreapta
- detalii în documentație

**La ce vă puteți folosi de acest lucru la temele voastre?**

Vă puteți defini o funcție de adăugare a mai multor elemente simultan. Găsiți un exemplu și în documentație.

Alternativ, puteți folosi
[liste explicite de inițializare](https://en.cppreference.com/w/cpp/utility/initializer_list)
dacă argumentele au același tip (de exemplu pointeri la bază); cf
[recomandărilor](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rt-variadic-not),
variadic templates ar fi overkill.

Bonus: dacă vrem să restricționăm funcția de afișare doar pentru derivate ale anumitei clase, putem folosi din nou concepte (C++20):
```c++
#include <iostream>

class Base {
public:
    friend std::ostream& operator<<(std::ostream& os, const Base&);// { return os; }
};

std::ostream& operator<<(std::ostream& os, const Base&) { os << "."; return os; }

//template <typename T>
//concept Derived = std::is_base_of_v<Base, T>;
template <typename T>
concept Derived = std::derived_from<T, Base>;

template <Derived... Args>
//template <typename... Args> requires(Derived<Args>, ...)
void afis2(const Args... args) {
    (std::cout << ... << args) << "\n";
    //(std::cout.operator<<(args), ...) << "\n";  // err
    //(..., std::cout.operator<<(args)) << "\n";  // err
    (print(std::cout, args), ...);
    std::cout << "\n";
    (..., print(std::cout, args));
    std::cout << "\n";
}

class Der1 : public Base {};
class Der2 : public Base {};

int main() {
  afis2(Base{});
  // afis2(1); // err
  afis2(Base{}, Der1{}, Der2{}, Base{});
}
```

Observații:
- nu am reușit să exprim cu `std::enable_if` această constrângere (probabil se poate, dar e mai urât); cu concepte e destul de natural
- `template <Derived... Args>` este scurtătură pentru `template <typename... Args> requires(Derived<Args>, ...)`
- diferența esențială dintre `std::derived_from` și `std::is_base_of` este aceea că prima permite doar moșteniri publice

### Clase template

#### Varianta 1

```c++
// sursa.h
#ifndef SURSA_H
#define SURSA_H

template <typename T>
class cls {
public:
    void f(T x);
};

#include "sursa.cpp"
#endif

/////////////////////////

// sursa.cpp
// ATENȚIE: FĂRĂ #include "sursa.h"
#include <iostream>

template <typename T>
void cls<T>::f(T x) {
    std::cout << x;
}

/////////////////////////

// main.cpp
#include "sursa.h"

int main() {
    cls<int> c;
    c.f(5);
}
```

Iar în CMakeLists.txt avem:
```cmake
# ...
add_executable(oop main.cpp)
# ...
```

#### Varianta 2

```c++
// sursa.h
#ifndef SURSA_H
#define SURSA_H


template <typename T>
class cls {
public:
    void f(T x);
};

#endif

/////////////////////////

// sursa.cpp
#include "sursa.h"
#include <iostream>

template <typename T>
void cls<T>::f(T x) {
    std::cout << x;
}

/////////////////////////

// sursa_impl.cpp
#include "sursa.cpp"

template
class cls<int>;

/////////////////////////

// main.cpp
#include "sursa.h"

int main() {
    cls<int> c;
    c.f(5);
}
```

Iar în CMakeLists.txt avem:
```cmake
# ...
add_executable(oop main.cpp sursa_impl.cpp)
# add_executable(oop main.cpp sursa.cpp) # sau așa dacă punem declarațiile pentru tipuri concrete tot în sursa.cpp
# ...
```

Observații:
- toate funcțiile unei clase template sunt la rândul lor funcții template
- clasele template sunt de obicei utile dacă vrem să ne definim diverse structuri de date (de exemplu arbori)

#### Curiously recurring template pattern (CRTP), mixin

CRTP este o tehnică de polimorfism folosind șabloane de clase. Tehnica este aplicabilă cu unele variații în
alte limbaje de programare.

La modul general, tehnica arată în felul următor:
```c++
template <typename Derivata>
class Baza {
    // ...
};

class Derivata : public Baza<Derivata> {
    // ...
};
```

Dacă vă dă cu virgulă rândul cu moștenirea, să vedem un exemplu concret:
```c++
#include <string>

template <typename Derived, typename T>
class Identifiable {
    const T id;
protected:
// public:
    Identifiable(const T& id_) : id(id_) {}
public:
    const T& get_id() const { return id; }
};

class User : public Identifiable<User, std::string> {
public:
    User() : Identifiable("unique_id") {}
};

class Post : public Identifiable<Post, int> {
public:
    // using Identifiable<Post, int>::Identifiable;
    Post(int id) : Identifiable(id) {}
};

int main() {
    User u;
    Post p{1};
}
```

Cu ajutorul CRTP, am eliminat duplicarea logicii gestionării unor identificatori. Exemplul este minimal,
dar cred că se înțelege că putem scăpa de mult cod repetitiv cu CRTP.


##### Exemplu de singleton cu CRTP:
```c++
#include <iostream>

template <typename Derived>
class Singleton {
protected:
    Singleton() = default;
public:
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    static Derived& getInstance() {
        static DerivedInstance instance;
        return instance;
    }
private:
    class DerivedInstance : public Derived{
        // avem nevoie de clasa DerivedInstance pentru
        // a putea construi un obiect de tip Derived aici
        // constr implicit generat de compilator este:
        // public:
        // DerivedInstance() : Derived() {}
    };
};


class Test : public Singleton<Test> {
protected:
    Test() = default;
};
class Test2 : public Singleton<Test2> {
protected:
    Test2() = default;
};

int main() {
    //Test t1; // eroare
    Test &t1 = Test::getInstance();
}
```

##### Exemplu mai complicat de singleton cu CRTP

Dacă dintr-un motiv sau altul avem nevoie și de constructor de inițializare cu parametru
lucrurile se complică. Va trebui să facem inițializare explicită pentru clasele care au
nevoie de transmitere prin parametri și să distrugem explicit obiectele pentru toate
clasele singleton.

Alternativele ar fi:

- renunțăm la singleton pentru acele clase cu inițializare cu parametri
- duplicăm logica de singleton în acele clase
- CRTP separate
- inițializare pentru toate clasele singleton (interfață uniformă)

Fiecare variantă are avantaje și dezavantaje, nu există o soluție perfectă.

Varianta propusă este următoarea:

```c++
#include <iostream>

template <typename Derived, bool has_default_constructor=true>
class Singleton {
protected:
    Singleton() = default;
public:
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    
    static Derived& getInstance() { return getInstance_(std::bool_constant<has_default_constructor>{}); }
    ~Singleton() {}
    template <typename... Args>
    static void init(Args&&... args) {
        if(!instance)
            instance = new DerivedInstance(std::forward<Args>(args)...);
    }
    static void destroyInstance() {
        if (instance) {
            delete instance;
            instance = nullptr;
        }
    }
private:
    class DerivedInstance : public Derived{
        // avem nevoie de clasa DerivedInstance pentru
        // a putea construi un obiect de tip Derived aici
        // constr implicit generat de compilator este:
        // public: DerivedInstance : Derived() {}
        // noi vrem și argumente, deci vom face astfel:
        public:
        template <typename... Args>
        explicit DerivedInstance(Args&&... args) : Derived(std::forward<Args>(args)...) {}
    };
    // cazul cu constructor fără parametri
    static Derived& getInstance_(std::true_type) {
        if(!instance) {
            instance = new DerivedInstance;
        }
        return *instance;
    }
    // cazul cu constructor cu parametri
    static Derived& getInstance_(std::false_type) {
        return *instance;
    }
    static Derived* instance;
};

template<typename Derived, bool has_default_constructor>
Derived* Singleton<Derived, has_default_constructor>::instance = nullptr;


class Test : public Singleton<Test> {
protected:
    Test() = default;
};
class Test2 : public Singleton<Test2> {
protected:
    Test2() = default;
};
class NoCopy {
public:
    NoCopy() = default;
    NoCopy(const NoCopy&) = delete;
    NoCopy& operator=(const NoCopy&) = delete;
};

class Test3 : public Singleton<Test3, false> {
    int x;
    float y;
    NoCopy& nc;
protected:
    Test3(int param1, float param2, NoCopy& n) : x(param1), y(param2), nc(n) {}
};

int main() {
    //Test t1; // eroare
    Test &t1 = Test::getInstance();
    Test2 &t2 = Test2::getInstance();
    NoCopy nc1;
    auto& nc2 = nc1;
    Test3::init(2, 3.4, nc2);
    auto& inst = Test3::getInstance();
    Test::destroyInstance();
    Test2::destroyInstance();
    Test3::destroyInstance();
}
```

În varianta de mai sus, trebuie să specificăm explicit pentru o clasă pe care vrem să o facem singleton
dacă are constructor de inițializare cu parametri. Nu avem un mecanism din limbaj (folosind funcții
de metaprogramare - `type_traits`) care să ne ofere această informație. În exemplul de mai sus,
clasa `Test3` are nevoie de această precizare.

Pentru a alege implementarea potrivită de `getInstance_`, folosim tag dispatch.

##### Exemplu de Counter cu CRTP:
```c++
#include <iostream>

template <typename Derived>
class Countable {
    static int nrObiecte;
protected:  // nu dorim să creăm direct obiecte de tip Counter
    Countable() {
        nrObiecte++;
    }
    ~Countable() {
        nrObiecte--;
    }
public:
    static int getNr() { return nrObiecte; }
};

class User : public Countable<User> {};

class Admin : public Countable<Admin> {};

template<typename Derived>
int Countable<Derived>::nrObiecte;

int main() {
    User u1, u2;
    std::cout << User::getNr() << "\n";
    Admin a1;
    std::cout << Admin::getNr() << "\n";
}
```

##### Alte exemple de CRTP

Alt exemplu este să înlănțuim apeluri de funcții în mod polimorfic, adică atât din bază, cât și din derivată.

Fără CRTP nu ar funcționa:
```c++
class Baza {
public:
    Baza& f1() {
        // ...
        return *this;
    }
    Baza& f2() {
        // ...
        return *this;
    }
};

class Derivata : public Baza {
public:
    Derivata& g1() {
        // ...
        return *this;
    }
    Derivata& g2() {
        // ...
        return *this;
    }
};

int main() {
    Derivata d;
    d.g1().f1().g2().f2();
    //         ^----- eroare aici!!!
}
```

Primim eroare în locul semnalat, deoarece `f1` întoarce referință către bază, deci nu mai avem acces la
funcțiile din derivată.

Soluția cu CRTP este următoarea:
```c++
template <typename T>
class Baza {
public:
    T& f1() {
        // ...
        return static_cast<T&>(*this);
    }
    T& f2() {
        // ...
        return static_cast<T&>(*this);
    }
};

class Derivata : public Baza<Derivata> {
public:
    Derivata& g1() {
        // ...
        return *this;
    }
    Derivata& g2() {
        // ...
        return *this;
    }
};

int main() {
    Derivata d;
    d.g1().f1().g2().f2(); // merge!
}
```

Cast-urile din bază sunt necesare fiindcă `*this` este altfel văzut ca `Baza&` și nu se poate face conversie
implicită de la `Baza&` la `Derivata&`. Având în vedere că nu putem crea obiecte de tip `Baza` fără să avem
un parametru la template, cast-ul este sigur. Puteam denumi parametrul de la șablon tot `Derivata` în loc de
`T`, dar nu știu dacă era la fel de clar.

CRTP are numeroase alte utilizări, însă nu voi intra în foarte multe detalii. Alte exemple: polimorfism
la compilare prin definirea unei interfețe în bază (tot cu cast-uri în bază),
[copiere polimorfică](https://devblogs.microsoft.com/oldnewthing/20220721-00/?p=106879),
evaluarea leneșă a expresiilor (expression templates).

Exemplu de CRTP din biblioteca standard: [`std::enable_shared_from_this`](https://en.cppreference.com/w/cpp/memory/enable_shared_from_this).


Un idiom complementar este cel de clasă **mixin** (sau mix-in). Dacă la CRTP aveam clasa de bază template,
aici avem derivata template. În cazul CRTP, baza stabilea interfața. La mixin, derivata este un șablon
și poate fi extins cu diverse interfețe.

Reluând exemplul de la tema 2 de la moșteniri multiple ale interfețelor, am putea folosi șabloane pentru
a crea mai ușor clase pornind de la numeroase interfețe:
```c++
template<class... Mixins>
class Post : public Mixins...
{
public:
    Post(const Mixins&... mixins) : Mixins(mixins)... {}
    // funcționalități suplimentare comune
};

int main() {
    Post<Identifiable, Loggable, Deletable> post1;
    Post<Identifiable, Loggable> post2;
    Post<Identifiable> post3;
    Post<Loggable> post4;
}
```

Dacă încercam să folosim abordarea de la tema 2, am fi avut de definit explicit câte o nouă clasă pentru
fiecare combinație de interfețe și am fi duplicat implementarea funcționalităților suplimentare comune.

Aici am profitat de faptul că se creează o nouă clasă prin instanțierea șablonului cu noi tipuri de date,
pe măsură ce avem nevoie de ele.

#### Tipuri de date dependente

```c++
#include <string>
#include <memory>
#include <array>

class ob {};
template <int nr>
class scaun {
    std::array<ob, nr> picioare;
public:
};

int main() {
  scaun<4> c;
  scaun<3> d;
  // c = d; // eroare
}
```

Tipurile de date de mai sus sunt utile de exemplu la înmulțiri de matrice: vrem să impunem ca nr de linii
al primei matrice să fie egal cu nr de coloane al celei de-a doua matrice. Astfel, codificăm o valoare în
tipul de date. `scaun<3>` și `scaun<4>` sunt două tipuri de date distincte!

### Supraîncărcare operatori friend în clase template

```c++
// sursa.h
#ifndef SURSA_H
#define SURSA_H

#include <iostream>

template <typename T>
class cls;

template <typename T>
std::ostream& operator<<(std::ostream& o, const cls<T>& c);

template <typename T>
class cls {
    T info;
public:
    cls(const T& x);
    friend std::ostream& operator<< <>(std::ostream&, const cls<T>&);
};

#endif

/////////////////////////

// sursa.cpp
#include "sursa.h"

template <typename T>
cls<T>::cls(const T& x) : info(x) {}

template <typename T>
std::ostream& operator<<(std::ostream& o, const cls<T>& c) {
    o << c.info;
    return o;
}

/////////////////////////

// sursa_impl.cpp
#include "sursa.cpp"

template class
cls<int>;

template
std::ostream& operator<< <>(std::ostream& o, const cls<int>& x);

/////////////////////////

// main.cpp
#include "sursa.h"

int main() {
    cls<int> c(5);
    std::cout << c;
}
```