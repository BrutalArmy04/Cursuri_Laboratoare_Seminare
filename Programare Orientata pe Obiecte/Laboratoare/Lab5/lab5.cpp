#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//    cerc > triunghi > paralelogram > dreptunghi > patrat

struct Coord
    {int x, y;
    friend double distanta_2_pct(Coord c1, Coord c2)
  {
    return sqrt((c2.y-c1.y) * (c2.y-c1.y) + (c2.x-c1.x) * (c2.x-c1.x));
  }


};
class Figuri
   {
    protected:
      vector <Coord> Coordonate;
    public:
      Figuri(const vector <Coord> &C)
      {Coordonate = C;};
      ~Figuri()
           {
        Coordonate.clear();
           }
      istream& operator>>(istream &in){

        for(int i = 0; i < Coordonate.size(); i++){
          in >> Coordonate[i].x >> Coordonate[i].y;
        }
        return in;
      }

        ostream& operator<<(ostream &out){
        for(int i = 0; i < Coordonate.size(); i++){
          out << Coordonate[i].x << " " << Coordonate[i].y << " ";
        }
        return out;
      }

  };

  class Cerc : public Figuri

  {
    public:
      double aria_cerc(const vector <Coord> &Coordonate)
          {return 3.14 * distanta_2_pct(Coordonate[0], Coordonate[1]);}
      double perim_cerc(const vector <Coord> &Coordonate)
      {
        return 2 * distanta_2_pct(Coordonate[0], Coordonate[1]) * 3.14;
      }

    };

    class Poligon : public Figuri
    {
      public:
        /*double perim_poligon(const vector <Coord> &Coordonate)
        {
          dobule perimetru;
          return  Coordonate[0].x;
        }*/
      };

int main()

{
  vector <Coord> v;
  int n;
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> v[i].x >> v[i].y;
  }
  return 0;
}

// folosesti virtual la clasa de baza cand faci mostenire
// static - memorat o singura data in memorie