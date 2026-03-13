package lab3.exercise3.service;

import lab3.exercise3.model.Angajat;
import java.util.ArrayList;
import java.util.List;

/**
 * TODO: Completează cele 3 metode.
 * Folosește ArrayList — nu mai e nevoie de redimensionare manuală.
 */
public class AngajatService {
    private List<Angajat> angajati;

    public AngajatService() {
        this.angajati = new ArrayList<>();
    }

    /** TODO: angajati.add(a); println("Angajat adăugat: " + a.getName()); */
    public void addAngajat(Angajat a) {
        angajati.add(a); 
        System.out.println("Angajat adăugat: " + a.getName()); 
    }

    /** TODO: dacă goală → mesaj; altfel parcurge cu index și afișează (i+1) + ". " + angajat */
    public void listAll() {
        if (angajati.size() == 0)
            System.out.println("Nu exista angajati");
        else 
            for (var i = 0; i < angajati.size(); i++)
            {
                System.out.println("Angajat" + i + angajati.get(i));
            }
    }

    /** TODO: parcurge lista, sumează a.salariuTotal(), returnează totalul. */
    public double totalSalarii() {
        int s = 0;
        for (Angajat i : angajati)
        {
            s+= i.salariuTotal();

        }
        return s;
    }
}
