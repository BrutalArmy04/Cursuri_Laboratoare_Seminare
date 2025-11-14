#include <iostream>
#include <vector>
using namespace std;


class Polinom{

    private:
    vector <int> coef;

    public:
    Polinom(const vector <int> &c){
        coef = c;
    }

    istream& operator>>(istream &in){
        for(int i = 0; i < coef.size(); i++){
            in >> coef[i];
        }
        return in;
    }

    ostream& operator<<(ostream &out){
        for(int i = 0; i < coef.size(); i++){
            out << coef[i] << "X^" << coef.size() - i - 1 << " ";
        }
        return out;
    }
    Polinom operator+(const Polinom &p){
        vector <int> c;
        int i;
        if (coef.size() > p.coef.size()){
            for (i=0; i<coef.size() - p.coef.size(); i++)
            {
                c.push_back(coef[i]);
            }
            for (int j=0; j<p.coef.size(); j++)
            {
                c.push_back(coef[i+j] + p.coef[j]);
            }}
        else
            {
              for (i = 0; i < p.coef.size() - coef.size(); i++)
              {
                  c.push_back(p.coef[i]);
              }
              for (int j = 0; j < coef.size(); j++)
              {
                  c.push_back(coef[j] + p.coef[i + j]);
              }
            }

        return Polinom(c);
    }

    Polinom operator-(const Polinom &p){
        vector <int> c;
        int i;
        if (coef.size() > p.coef.size()){
            for (i=0; i<coef.size() - p.coef.size(); i++)
            {
                c.push_back(coef[i]);
            }
            for (int j=0; j<p.coef.size(); j++)
            {
                c.push_back(coef[i+j] - p.coef[j]);
            }}
        else
            {
              for (i = 0; i < p.coef.size() - coef.size(); i++)
              {
                  c.push_back(p.coef[i]);
              }
              for (int j = 0; j < coef.size(); j++)
              {
                  c.push_back(coef[j] - p.coef[i + j]);
              }
            }

        return Polinom(c);
    }

    Polinom operator*(const Polinom &p)
    {
        vector <int> c;
        for (int i = 0; i < coef.size() + p.coef.size() - 1; i++)
        {
            c.push_back(0);
        }
        for (int i = 0; i<coef.size(); i++)
        {
            for (int j = 0; j<p.coef.size(); j++)
            {
                c[i+j] += coef[i] * p.coef[j];
            }
        }
        return Polinom(c);
    }

    ~Polinom(){
        coef.clear();
    }

};


int main()
{
    vector <int> c;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        c.push_back(x);
    }
    vector <int> d;
    int m;
    cin >> m;
    for(int i = 0; i < m; i++){
        int x;
        cin >> x;
        d.push_back(x);
    }
    Polinom p(c);
    Polinom q(d);
    Polinom r = p * q;
    r << cout;


    return 0;
}


//Mostenire apel const destructor
// baza -> derivata
// derivata -> baza