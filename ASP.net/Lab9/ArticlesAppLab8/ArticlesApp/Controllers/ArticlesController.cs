    using ArticlesApp.Data;
using ArticlesApp.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;

namespace ArticlesApp.Controllers
{
    public class ArticlesController(ApplicationDbContext context, UserManager<ApplicationUser> userManager
        , RoleManager<IdentityRole> roleManager) : Controller


    {
        private readonly ApplicationDbContext db = context; 
        private readonly UserManager<ApplicationUser> _userManager = userManager;
        private readonly RoleManager<IdentityRole> _roleManager = roleManager;

        // Se afiseaza lista tuturor articolelor impreuna cu categoria 
        // din care fac parte
        // Pentru fiecare articol se afiseaza si userul pentru care s-a postat articolul
        // HttpGet implicit
        [Authorize(Roles = "User,Editor,Admin")] // fara spatiu, ca altfel cauta rol cu spatiu in nume
        public IActionResult Index()
        {
            var articles = db.Articles
                             .Include(a => a.Category)
                                .Include(a => a.User)
                             .OrderByDescending(a => a.Date);

            // ViewBag.OriceDenumireSugestiva
            ViewBag.Articles = articles;

            if (TempData.ContainsKey("message"))
            {
                ViewBag.Message = TempData["message"];
                ViewBag.Alert = TempData["messageType"];
            }

            return View();
        }

        // Se afiseaza un singur articol in functie de id-ul sau 
        // impreuna cu categoria din care face parte
        // In plus sunt preluate si toate comentariile asociate unui articol
        // se afieseaza si userul care a postat articolul
        // HttpGet implicit
        [Authorize(Roles = "User,Editor,Admin")]
        public IActionResult Show(int id)
        {
            Article? article = db.Articles
                                 .Include(a => a.Category)
                                 .Include(a => a.Comments)
                                    //tabbed ca sa arat ca e subordonata (nu e obligatoriu)
                                    .ThenInclude(c => c.User) // userii care au postat comentariile
                                 .Include (a => a.User) // userul care a postat articolul
                                 .Where(a => a.Id == id)
                                 .FirstOrDefault();

            if (article is null)
            {
                return NotFound();

                // sau se foloseste TempData
                // TempData["message"] = "Articolul nu exista!";
                // return RedirectToAction("Index");
            }
            SetAccessRights();
            return View(article);
        }


        // Se afiseaza formularul in care se vor completa datele unui articol
        // impreuna cu selectarea categoriei din care face parte
        // Doar utilizatorii cu rolul Editor sau Admin pot adauga articole
        // HttpGet implicit
        [Authorize(Roles = "Editor,Admin")]
        public IActionResult New()
        {
            Article article = new Article();

            article.Categ = GetAllCategories();

            return View(article);
        }

        // Se adauga articolul in baza de date
        // Doar utilizatorii cu rolul Editor sau Admin pot adauga articole
        [Authorize(Roles = "Editor,Admin")]
        [HttpPost]
        public IActionResult New(Article article)
        {
            article.Date = DateTime.Now;
            // preluam id-ul userului care posteaza articolul
            article.UserId = _userManager.GetUserId(User);   

            if (ModelState.IsValid)
            {
                db.Articles.Add(article);
                db.SaveChanges();
                TempData["message"] = "Articolul a fost adaugat";
                TempData["messageType"] = "alert-success";
                return RedirectToAction("Index");
            }

            else
            {
                article.Categ = GetAllCategories();
                return View(article);
            }
        }


        // Se editeaza un articol existent in baza de date impreuna cu categoria din care face parte
        // Categoria se selecteaza dintr-un dropdown
        // Se afiseaza formularul impreuna cu datele aferente articolului din baza de date
        // Doar utilizatorii cu rolul Editor sau Admin pot edita articole
        // Adminii pot edita toate articolele
        // Editorii pot edita doar articolele pe care le-au postat
        // HttpGet implicit
        [Authorize(Roles = "Editor,Admin")]
        public IActionResult Edit(int id)
        {

            Article? article = db.Articles
                                .Include(a => a.Category)
                                .Where(art => art.Id == id)
                                .FirstOrDefault();

            if (article is null)
            {
                return NotFound();

               // sau se foloseste TempData
               // TempData["message"] = "Articolul nu exista!";
               // return RedirectToAction("Index");
            }

            article.Categ = GetAllCategories();

            if (article.UserId == _userManager.GetUserId(User) || User.IsInRole("Admin"))
            {
                // utilizatorul este cel care a postat articolul sau este admin
                return View(article);
            }
            else
            {
                // utilizatorul nu are dreptul sa editeze articolul
                TempData["message"] = "Nu aveți dreptul să faceți modificări asupra unui articol care nu vă \r\naparține"; 
                TempData["messageType"] = "alert-danger";
                return RedirectToAction("Index");
            }

        }

        // Se adauga articolul modificat in baza de date
        // Se verifica rolul utilizatorilor care au dreptul sa editeze articolul
        [HttpPost]
        [Authorize(Roles = "Editor,Admin")]
        public IActionResult Edit(int id, Article requestArticle)
        {
            Article? article = db.Articles.Find(id);

            if(article is null)
            {
                return NotFound();
            }

            else
            {
                if (ModelState.IsValid)
                {
                    if(article.UserId == _userManager.GetUserId(User) || User.IsInRole("Admin"))
                    {
                        // utilizatorul este cel care a postat articolul sau este admin
                        article.Title = requestArticle.Title;
                        article.Content = requestArticle.Content;
                        article.Date = DateTime.Now;
                        article.CategoryId = requestArticle.CategoryId;
                        TempData["message"] = "Articolul a fost modificat";
                        TempData["messageType"] = "alert-success";
                        db.SaveChanges();
                        return RedirectToAction("Index");
                    }
                    else
                    {
                        // utilizatorul nu are dreptul sa editeze articolul
                        TempData["message"] = "Nu aveți dreptul să faceți modificări asupra unui articol care nu vă \r\naparține";
                        TempData["messageType"] = "alert-danger";
                        return RedirectToAction("Index");
                    }
                }
                else
                {
                    requestArticle.Categ = GetAllCategories();
                    return View(requestArticle);
                }
            }   
        }


        // Se sterge un articol din baza de date 
        // Utilizatorii cu rolul Admin pot sterge orice articol
        // Editorii pot sterge doar articolele pe care le-au postat
        [HttpPost]
        [Authorize(Roles = "Editor,Admin")]
        public ActionResult Delete(int id)
        {
            Article? article = db.Articles.Find(id);
           /* Article article = db.Articles
                                .Include(a => a.Comments)
                                .Where(art => art.Id == id)
                                .FirstOrDefault();*/

            if (article is null)
            {
                return NotFound();
            }

            else
            {
                if (article.UserId == _userManager.GetUserId(User) || User.IsInRole("Admin"))
                {
                    // utilizatorul este cel care a postat articolul sau este admin
                    db.Articles.Remove(article);
                    db.SaveChanges();
                    TempData["message"] = "Articolul a fost sters";
                    TempData["messageType"] = "alert-success";
                }
                else
                {
                    // utilizatorul nu are dreptul sa stearga articolul
                    TempData["message"] = "Nu aveți dreptul să ștergeți un articol care nu vă aparține";
                    TempData["messageType"] = "alert-danger";
                    return RedirectToAction("Index");
                }
            }

                

            try
            {
                db.SaveChanges();
                TempData["message"] = "Articolul a fost sters";
            }
            catch(DbUpdateException)
            {
                TempData["message"] = "Nu se poate sterge articolul";
            }

            return RedirectToAction("Index");
        }

        // Adaugarea unui comentariu asociat unui articol in baza de date
        [HttpPost]
        public IActionResult Show([FromForm] Comment comment)
        {
            comment.Date = DateTime.Now;

            // preluam id-ul useruluicare posteaza comentariul
            comment.UserId = _userManager.GetUserId(User);

            if (ModelState.IsValid)
            {
                db.Comments.Add(comment);
                db.SaveChanges();
                return Redirect("/Articles/Show/" + comment.ArticleId);
            }
            else
            {
                Article? art = db.Articles
                                .Include(a => a.Category)
                                .Include(a => a.Comments)
                                    .ThenInclude(a => a.User)   // userul care a postat comentariul
                                .Include(a => a.User) // userul care a postat articolul
                                    
                                .Where(art => art.Id == comment.ArticleId)
                                .FirstOrDefault();

                if (art is null)
                {
                    return NotFound();
                }

                //return Redirect("/Articles/Show/" + comm.ArticleId);
                SetAccessRights();
                return View(art);
            }

        }

        // Conditiile de afisare a butoanelor de Edit si Delete
        // Butoanele se afla in View-ul Show.cshtml
        private void SetAccessRights()
        {
            ViewBag.AfisareButoane = false;
            if (User.IsInRole("Editor"))
            {
                ViewBag.AfisareButoane = true;

            }
            ViewBag.UserCurent = _userManager.GetUserId(User);

            ViewBag.EsteAdmin = User.IsInRole("Admin");
        }


            [NonAction]
        public IEnumerable<SelectListItem> GetAllCategories()
        {
            // generam o lista de tipul SelectListItem fara elemente
            var selectList = new List<SelectListItem>();

            // extragem toate categoriile din baza de date
            var categories = from cat in db.Categories
                             select cat;

            // iteram prin categorii
            foreach (var category in categories)
            {
                // adaugam in lista elementele necesare pentru dropdown
                // id-ul categoriei si denumirea acesteia
                selectList.Add(new SelectListItem
                {
                    Value = category.Id.ToString(),
                    Text = category.CategoryName
                });
            }
            /* Sau se poate implementa astfel: 
             * 
            foreach (var category in categories)
            {
                var listItem = new SelectListItem();
                listItem.Value = category.Id.ToString();
                listItem.Text = category.CategoryName;

                selectList.Add(listItem);
             }*/


            // returnam lista de categorii
            return selectList;
        }

        // Metoda utilizata pentru exemplificarea Layout-ului
        // Am adaugat un nou Layout in Views -> Shared -> numit _LayoutNou.cshtml
        // Aceasta metoda are un View asociat care utilizeaza noul layout creat
        // in locul celui default generat de framework numit _Layout.cshtml
        public IActionResult IndexNou()
        {
            return View();
        }
    }
}
