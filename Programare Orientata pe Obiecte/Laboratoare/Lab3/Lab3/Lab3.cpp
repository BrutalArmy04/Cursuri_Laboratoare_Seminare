#include <iostream>
#include <vector>
using namespace std;

class Matrice {
public:
    Matrice(int nrLinii, int nrColoane, int element = 0) {
        for (auto x = 0; x < nrLinii; x++) {
            vector<int> aux;
            for (int i = 0; i < nrColoane; i++) {
                aux.push_back(element);
            }
            matrice.push_back(aux);
        }
    }

    Matrice(const Matrice& aux) : matrice(aux.matrice) {

    }

    friend ostream& operator<<(ostream& out, const Matrice& aux) {
        for (auto i = 0; i < aux.matrice.size(); i++) {
            for (auto j = 0; j < aux.matrice[i].size(); j++) {
                out << aux.matrice[i][j] << " ";
            }
            out << std::endl;
        }
        return out;
    }

    friend istream& operator>>(istream& in, Matrice& aux) {
        int nrLinii, nrColoane;
        std::cout << "Introduceti nrLinii =";
        in >> nrLinii;
        std::cout << "Introduceti nrColoane =";
        in >> nrColoane;
        vector<vector<int>> matrice;
        int n;
        for (auto i = 0; i < nrLinii; i++) {
            vector<int> auxVector;
            for (auto j = 0; j < nrColoane; j++) {
                in >> n;
                auxVector.push_back(n);
            }
            matrice.push_back(auxVector);
        }
        aux.matrice = matrice;
        return in;
    }

    size_t nrLinii() const {
        return matrice.size();
    }

    size_t nrColoane() const {
        if (nrLinii() == 0) {
            return 0;
        }
        return matrice[0].size();
    }

    Matrice operator+(const Matrice& aux) const {
        if (this->nrLinii() != aux.nrLinii() ||
            this->nrColoane() != aux.nrColoane()) {
            return Matrice(0, 0);
        }
        auto sd = this->nrColoane();
        Matrice auxx(this->nrLinii(), this->nrColoane());
        for (auto i = 0; i < this->nrLinii(); i++) {
            for (auto j = 0; j < this->nrColoane(); j++) {
                auxx.matrice[i][j] = this->matrice[i][j] + aux.matrice[i][j];
            }
        }
        return auxx;
    }

    Matrice operator*(int scalar) const {
        Matrice aux(this->nrLinii(), this->nrColoane());
        for (auto i = 0; i < this->nrLinii(); i++) {
            for (auto j = 0; j < this->nrColoane(); j++) {
                aux.matrice[i][j] = this->matrice[i][j] * scalar;
            }
        }
        return aux;

    }
    Matrice transpusa(const Matrice& matrice)
    {
        Matrice transp_mat(this->nrLinii, this->nrColoane, 1);
        vector <int> copy_line;
        for (auto i = 0; i < this->nrColoane(); i++)
        {
            copy_line = matrice[i];
            transp_mat.push_back(copy_line);
        }
        return transp_mat;

    }

    Matrice operator-(const Matrice& aux) const {
        return *this + (aux * -1);
    }

private:
    vector<vector<int>> matrice;
};

Matrice operator*(int scalar, const Matrice& aux) {
    return aux * scalar;
}

int main() {
    Matrice x(2, 2, 1);
    Matrice y = Matrice::transpusa(x);
    std::cout << y;
}
