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
    insert(5);
    insert(4);
    insert(1);
    insert(2);
    insert(3);
    cout << pop() << '\n'
         << pop() << '\n'
         << pop() << '\n'
         << pop() << '\n';

}

