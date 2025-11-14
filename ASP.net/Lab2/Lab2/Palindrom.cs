using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab2
{
    public class Palindrom
    {
        public void vPalindrom(int n) // less elegant
        {
            int cn = n;
            int a = 0;
            while (cn != 0)
            {
                a = cn % 10 + a*10;
                cn /= 10;
            }
            if (a == n)
                Console.WriteLine("da");
            else
                Console.WriteLine("nu");
        }
    }
}
