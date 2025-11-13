/// punem virtual la functii din clasa mostenita ca sa nu avem surprize
/// dynamic cast nu merge daca clasa nu este polimorfica
/// virtual void blah() = 0; -> fct virtuala pura, clasa abstracta, sunt facute doar sa fie derivate


//Error handling



#include <iostream>
#include <vector>
using namespace std;

class FisaMedicala{

  protected:
    int colesterol, tensiune_arteriala, varsta;
    string nume, prenume, adresa, data_analiza;
  public:


  };

  class FisaMedicala_40 : public FisaMedicala{
    private:
        string fumat, sedentarism;
    public:
  };


  class FisaMedicala_copii : public FisaMedicala{
    private:
        int proteina_C;
        string data_analiza_C, antecedente_familie;
    public:
  };

  int main()
      {
    /// o sa doresc sa salvez totul intr-un vector ca trb sa afisez toate fisele medicale pe care le am
    /// problema este ca nush daca trb la toate ob odata sau nu, prob o sa fie de tip FisaMedicala

    vector <FisaMedicala> fise;

    return 0;
      }