using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;

namespace Lab3.Controllers
{
    public class ExamplesController : Controller
    {
        public string Concatenare(string? a, string? b)
        {
            return a + " " + b;
        }

        public string Produs(int x, int? y)
        {
            if (y == null)
                return "Introduceti ambele valori";
            return Convert.ToString(x * y);
        }
        
        public string Operatie(int? op1, int? op2, string? oper) {

            if (op1 == null || op1 is not int)
                return "Introduceti valoarea 1";
            if (op2 == null || op2 is not int)
                return "Introduceti valoarea 2";
            if (oper == null || oper is not string)
                return "Introduceti valoarea 3";

            switch (oper){ 
                    case "plus":
                        return Convert.ToString(op1 + op2);
                    case "minus":
                        return Convert.ToString(op1 - op2);
                    case "ori":
                        return Convert.ToString(op1 * op2);
                    case "div":
                        return Convert.ToString(op1 / op2);
                    default:
                    return "Operatie invalida";

            }

        }
    }
}
