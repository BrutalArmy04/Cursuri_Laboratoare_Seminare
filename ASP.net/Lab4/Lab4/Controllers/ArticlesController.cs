using Lab4.Models;
using Microsoft.AspNetCore.Mvc;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Lab4.Controllers
{
    public class ArticlesController : Controller
    {
        [NonAction] //  nu pot apela metoda din url cu asta
        public Article[] GetArticles()
        {
            // Se instantiaza un array de articole 
            Article[] articles = new Article[3];
            // Se creeaza articolele 
            for (int i = 0; i < 3; i++)
            {
                Article article = new Article();
                article.Id = i;
                article.Title = "Articol " + (i + 1).ToString();
                article.Content = "Continut articol " + (i + 1).ToString();
                article.Date = DateTime.Now;
                // Se adauga articolul in array 
                articles[i] = article;
            }
            return articles;
        }
        // Afisarea tuturor articolelor
        // [HttpGet] -> se executa implicit



        public IActionResult Index()
        {
            Article[] article = GetArticles();
            //se adauga array-ul de articole intr-un ViewBag pentru a fi trimis pentru afisare
            //punga pentru uitat

            ViewBag.Articole = article;
            // returneaza view-ul din folderul Views, folderul articles care are ac mnume ca metoda - Index
            return View();

        }

        // Afisarea unui singur articol in functie de ID-ul sau

        [HttpGet]
        public IActionResult Show(int? id)
        {
            Article[] article = GetArticles();

            try
            {
                ViewBag.Articol = article[(int)id];
                return View();
            }
            catch (Exception ex)
            {
                //return View("Error");
                return StatusCode(StatusCodes.Status404NotFound);
            }
        }

        //Afisarea formularului de creare a unui nou articol unui nou articol
        [HttpGet]
        public IActionResult New()
        {

            return View();

        }
        [HttpPost]
        public IActionResult New(Article article)
        {

            // ... cod adaugare articol in baza de date
            return Content("Articolul a fost adaugat");

        }

        // GET: Afisarea datelor unui articol pentru editare 
        [HttpGet]
        public IActionResult Edit(int? id)
        {
            ViewBag.Id = id;
            return View();
        }

        // POST: Trimiterea modificarilor facute catre server 


        [HttpPost]
        public IActionResult Edit(Article article)
        {
            return View("EditMethod");
        }

        // POST Stergere articol din baza de date
        [HttpPost]
        public IActionResult Delete(int? id)
        {
            // ... cod stergere articol din baza de date
            return Content("Articolul a fost sters din baza de date!");
        }

    }
}


