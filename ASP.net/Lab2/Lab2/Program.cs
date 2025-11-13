// namespace -> am acces la tot din aplicatie
namespace Lab2
{
    class Program
    {


        static void Main(string[] args)
        {

            //int n = int.Parse(Console.ReadLine());
            //Palindrom p = new Palindrom();
            //p.vPalindrom(n);
            int[] a = new int[100];
            int n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++) 
                a[i] = int.Parse(Console.ReadLine());


            for (int j = 0; j < n; j++) 
                Console.WriteLine(a[j]);


                    // Console.WriteLine("Hello World");


                    /*int nr = 100;
                    string str = "Acesta este un text";
                    double d = 12.35;
                    char c = 'a';
                    bool b = true;
                    object obj = 100;
                    Console.WriteLine("Numarul este " + nr);
                    Console.WriteLine("Stringul este: " + str);
                    Console.WriteLine("Numarul in virgula mobila este: " + d);
                    Console.WriteLine("Caracterul este: " + c);
                    Console.WriteLine("Valoarea de adevar este: " + b);
                    Console.WriteLine("Obiectul este: " + obj);*/


                    /*// CONVERSII IMPLICITE
                    int nrInt = 10;
                    // Metoda GetType() preia tipul de date
                    Type tipNrInt = nrInt.GetType();
                    // Conversie implicita
                    double nrDouble = nrInt;
                    // Se preia tipul
                    Type tipNrDouble = nrDouble.GetType();
                    // Afisare valori inainte de conversie
                    Console.WriteLine("nrInt value: " + nrInt);
                    Console.WriteLine("nrInt Type: " + tipNrInt);
                    // Afisare valori dupa conversia implicita
                    Console.WriteLine("nrDouble value: " + nrDouble);
                    Console.WriteLine("nrDouble Type: " + tipNrDouble);*/


                    /*// CONVERSII EXPLICITE
                    double nDouble = 25.123;
                    // Conversie explicita
                    int nInt = (int)nDouble;
                    // Afisarea valorii inainte de conversie
                    Console.WriteLine("Valoarea inainte de conversie a fost: "
                    + nDouble);
                    // Afisarea valorii dupa conversie
                    Console.WriteLine("Valoarea dupa conversie este: " +
                    nInt);*/


                    /*string st = "1000000000000000";
                    Type tip1 = st.GetType();
                    // Se converteste tipul string in int
                    long x = long.Parse(st);
                    Type tip2 = x.GetType();
                    Console.WriteLine("Valoarea initiala a fost: " + st);
                    Console.WriteLine("A avut tipul: " + tip1);
                    Console.WriteLine("Noua valoare dupa conversie este: " + x);
                    Console.WriteLine("Valoarea dupa conversie are tipul: " + tip2);


                    /*
                    // NULLABLE
                    int? num1 = null;
                    int? num2 = 45;
                    Console.WriteLine("Valorile sunt: {0}, {1}", num1, num2);*/
                } } }
