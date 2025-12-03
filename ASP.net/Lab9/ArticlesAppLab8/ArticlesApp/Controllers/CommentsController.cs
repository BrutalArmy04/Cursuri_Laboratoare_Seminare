using ArticlesApp.Data;
using ArticlesApp.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace ArticlesApp.Controllers
{
    public class CommentsController(ApplicationDbContext context, UserManager<ApplicationUser> userManager,
    RoleManager<IdentityRole> roleManager): Controller
    {
        private readonly ApplicationDbContext db = context;
        private readonly UserManager<ApplicationUser> _userManager = userManager;
        private readonly RoleManager<IdentityRole> _roleManger = roleManager;


        /*

        // Adaugarea unui comentariu asociat unui articol in baza de date
        [HttpPost]
        public IActionResult New(Comment comm)
        {
            comm.Date = DateTime.Now;

            if(ModelState.IsValid)
            {
                db.Comments.Add(comm);
                db.SaveChanges();
                return Redirect("/Articles/Show/" + comm.ArticleId);
            }

            else
            {
                return Redirect("/Articles/Show/" + comm.ArticleId);
            }
         }

        */


        // Stergerea unui comentariu asociat unui articol din baza de date
        // Se poate serge comentariul doar de catre userul cu rolul Admin sau de userul care a pus comentariul
        [HttpPost]
        [Authorize(Roles = "Admin,User,Editor")]
        public IActionResult Delete(int id)
        {
            Comment comm = db.Comments.Find(id);

            if(comm is null)
            {
                return NotFound();  
            }
            else
            {
                if (comm.UserId == _userManager.GetUserId(User) || User.IsInRole("Admin"))
                {
                    db.Comments.Remove(comm);
                    db.SaveChanges();
                    return Redirect("/Articles/Show/" + comm.ArticleId);
            
                }
                else
                {
                    TempData["message"] = "Nu aveti dreptul sa stergeti comentariul";
                    TempData["messageType"] = "alert-danger";
                    return RedirectToAction("Index", "Articles"); // ii dam unde sa mearga
                }
            }

                
        }

        // In acest moment vom implementa editarea intr-o pagina View separata
        // Se editeaza un comentariu existent
        // Se poate edita comentariul doar de catre utilizatorul care a post postat comentariul respectiv
        // Adminii pot edita orice comentariu, chiar daca nu a fost postat de ei
        // HttpGet default
        [Authorize(Roles = "User,Editor,Admin")]
        public IActionResult Edit(int id)
        {

            Comment comm = db.Comments.Find(id);
            if (comm is null)
            {
                return NotFound();
            }
            else
            {
                if (comm.UserId == _userManager.GetUserId(User) || User.IsInRole("Admin"))
                    return View(comm);
                else
                {
                    TempData["message"] = "Nu aveti dreptul sa editati comentariul";
                    TempData["messageType"] = "alert-danger";
                    return RedirectToAction("Index", "Articles"); // ii dam unde sa mearga
                }
            }   
               
                return View(comm);
        }

        [HttpPost]
        [Authorize(Roles = "User,Editor,Admin")]
        public IActionResult Edit(int id, Comment requestComment)
        {
            Comment? comm = db.Comments.Find(id);


            if (comm is null)
            {
                return NotFound();
            }
            else
            {
                if (comm.UserId == _userManager.GetUserId(User) || User.IsInRole("Admin"))
                {
                    if (ModelState.IsValid)
                    {

                        comm.Content = requestComment.Content;

                        db.SaveChanges();

                        return Redirect("/Articles/Show/" + comm.ArticleId);
                    }
                    else
                    {
                        return View(requestComment);

                    }
                }
                else
                {
                    TempData["message"] = "Nu aveti dreptul sa editati comentariul";
                    TempData["messageType"] = "alert-danger";
                    return RedirectToAction("Index", "Articles"); // ii dam unde sa mearga
                }
            }
            
        }
    }
}