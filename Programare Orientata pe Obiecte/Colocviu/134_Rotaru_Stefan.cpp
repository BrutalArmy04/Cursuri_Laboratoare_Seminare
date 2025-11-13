/* Rotaru Stefan 134
 * CLion 2024 3 5
 * Tutore Laborator: Bahrim Dragos */

#include <iostream>
#include <memory>
#include <ostream>
#include <istream>
#include <vector>
using namespace std;

class Comanda {
protected:
    string nume;
    float gramaj;
    static int id;
    int contor;
    float energie;

    virtual void read(istream &is);
    virtual void print(ostream &os) const;
public:
    Comanda() = default;
    virtual shared_ptr<Comanda> clone()const = 0;
    Comanda(const string &nume, float gramaj, int contor)
        : nume(nume),
          gramaj(gramaj),
          contor(id++) {
    }
    virtual ~Comanda() = default;

    void set_energie(float energie) {
        this->energie = energie;
    }

    //friend ostream &op>>(ostream &os, const Comanda&ob) {};
};
class Bautura : public Comanda {
private:
    bool pet;
public:
    Bautura() = default;
    shared_ptr<Comanda> clone () const override{return make_shared<Bautura>(*this);};
    explicit Bautura(bool pet)
        : pet(pet) {
    }

    Bautura(const string &nume, float gramaj, int contor, bool pet)
        : Comanda(nume, gramaj, contor),
          pet(pet) {
    }

    ~Bautura() override = default;

    Bautura(const Bautura &o): Comanda(o){};
    void val_energie(const float &gramaj, float &energie) {
        if (pet == true)
            set_energie(25);
        else
            set_energie(0.25 * gramaj);
    }
};

class Desert: public Comanda {
private:
    string tip;
public:
    Desert() = default;

    explicit Desert(const string &tip)
        : tip(tip) {
    }
    Desert(const Desert &o): Comanda(o){};
    Desert(const string &nume, float gramaj, int contor, const string &tip)
        : Comanda(nume, gramaj, contor),
          tip(tip) {
    }
    shared_ptr<Comanda> clone () const override{return make_shared<Desert>(*this);};
    ~Desert() override = default;

    void val_energie(const float &gramaj, float &energie) {
        if (tip == "felie")
            set_energie(25);
        else if (tip == "portie")
            set_energie(0.5 * gramaj);
        else set_energie(2 * gramaj);
    }
};

class Burger : public Comanda {
    vector <string> ingrediente;
public:
    Burger() = default;

    explicit Burger(const vector<string> &ingrediente)
        : ingrediente(ingrediente) {
    }
    shared_ptr<Comanda> clone () const override{return make_shared<Burger>(*this);};
    Burger(const string &nume, float gramaj, int contor, const vector<string> &ingrediente)
        : Comanda(nume, gramaj, contor),
          ingrediente(ingrediente) {
    }
    Burger(const Burger &o): Comanda(o){};
    ~Burger() override = default;
    void val_energie(const float &gramaj, const vector<string> ingrediente, float &energie)
    {set_energie(0.25 * gramaj * sizeof(ingrediente));}
};

class Angajat {
private:
    int energie;
    string nume;
    Angajat(int energie = 100)
        : energie(energie) {
    }

    Angajat(const Angajat &other)
        : energie(other.energie) {
    }

    Angajat & operator=(const Angajat &other) {
        if (this == &other)
            return *this;
        energie = other.energie;
        return *this;
    }
    virtual void print(ostream &os)const;
public:
    void set_energie(int energie) {
        this->energie = energie;
    }

    [[nodiscard]] string nume1() const {
        return nume;
    }

    virtual ~Angajat() = default;

    friend std::ostream & operator<<(std::ostream &os, const Angajat &obj) {
        return os
               << "energie: " << obj.energie
               << " nume: " << obj.nume;
    }

    /*friend ostream&op>>(ostream &os, const Angajat &ob)
    {
    ob.print(os);
    return os;}*/

};

/*class Casier : public Angajat {
public:
    Casier() = default;
    explicit Casier(const Angajat &other)
        : Angajat(other) {
    }

    Casier(const Casier &other)
        : Angajat(other) {
    }

    Casier & operator=(const Casier &other) {
        if (this == &other)
            return *this;
        Angajat::operator =(other);
        return *this;
    }

    ~Casier() override = default;
    void consum_energie()  {

    }
};*/

class Loop {
private:
/*
public:
    void preluare(Angajat &A) {
        if (Angajat.nume1() == "Casier") {
            Angajat.set_energie -= 25;
        else Angajat.set_energie -=100;
        }


    void livrare(Angajat &A)
    {
    if (Angajat.nume1() == "Livrator")
    Angajat.set_energie -= 25;
    else Angajat.set_energie -=100;
    }
    void Preparare(Angajat &A, Comanda &C)
    {}
    if (Angajat.nume1() == "Bucatar")



    }*/

};
class app {
    //Loop L;
    app() = default;
public:
    app(const app&) = delete;
    app& operator=(const app&) = delete;
    static app &getapp()
    {static app ap;
        return ap;}


};
int Comanda:: id = 0;



int main() {
    auto &x = app::getapp();
    return 0;
    /*pt numarat de angajati se face un vector de 4 si se numara fiecare aparitie a unui angajat in acel vector de 4 elemente, iar apoi se afiseaza*/
}