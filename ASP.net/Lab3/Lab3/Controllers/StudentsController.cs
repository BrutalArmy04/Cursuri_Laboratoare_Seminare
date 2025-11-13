using Microsoft.AspNetCore.Mvc;

namespace Lab3.Controllers
{
    public class StudentsController : Controller
    {
        public string Index()
        {
            return "Afisarea tuturor studentilor";
        }

        public string Create()
        {
            return "Crearea unui nou student";
        }

        public string Show(int? id)
        {
            if (id == null)
            {
                return "Studentul nu exista";

            }
            return "Afisare student cu Id-ul: " + id;
        }
        public string Edit(int? id)
        {
            if (id == null)
            {
                return "Studentul nu exista";

            }
            return "Editare student cu Id-ul: " + id;
        }
        public string Delete(int? id)
        {
            if (id == null)
            {
                return "Studentul nu exista";

            }
            return "Stergere student cu Id-ul: " + id;
        }
    }
}
