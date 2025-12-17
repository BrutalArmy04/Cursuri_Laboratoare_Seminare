using ExercitiuLaborator12.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;

namespace ExercitiuLaborator12.Controllers
{
    public class MembershipsController : Controller
    {

        private readonly AppDbContext context;

        public MembershipsController(AppDbContext contextt)
        {
            context = contextt;
        }


        public IActionResult Index()
        {
            var memberships = context.Memberships
                                    .Include(m => m.Gym)
                                    .ToList();

            return View(memberships);
        }
        public IActionResult New()
        {
            ViewBag.Gyms = new SelectList(context.Gyms, "Id", "Name");
            return View();
        }

        [HttpPost]
        public IActionResult New(Membership membership)
        {
            if (ModelState.IsValid)
            {
                membership.Date = DateTime.Now;

                context.Memberships.Add(membership);
                context.SaveChanges();

                return RedirectToAction("Index");
            }

            
            ViewBag.Gyms = new SelectList(context.Gyms, "Id", "Name");
            return View(membership);
        }
        public IActionResult Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var membership = context.Memberships.Find(id);

            if (membership == null)
            {
                return NotFound();
            }

            ViewBag.Gyms = new SelectList(context.Gyms, "Id", "Name", membership.GymId);

            return View(membership);
        }

        [HttpPost]
        public IActionResult Edit(int id, Membership membership)
        {
            if (id != membership.Id)
            {
                return NotFound();
            }

           
            if (ModelState.IsValid)
            {
                try
                {
                    var originalMembership = context.Memberships.AsNoTracking().FirstOrDefault(m => m.Id == id);
                    if (originalMembership != null)
                    {
                        membership.Date = originalMembership.Date; 
                    }

                    context.Update(membership);
                    context.SaveChanges();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!MembershipExists(membership.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }

            ViewBag.Gyms = new SelectList(context.Gyms, "Id", "Name", membership.GymId);
            return View(membership);
        }
        private bool MembershipExists(int id)
        {
            return context.Memberships.Any(e => e.Id == id);
        }
        public IActionResult Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var membership = context.Memberships
                .Include(m => m.Gym)
                .FirstOrDefault(m => m.Id == id);

            if (membership == null)
            {
                return NotFound();
            }

            return View(membership);
        }

        [HttpPost, ActionName("Delete")] 
        public IActionResult DeleteConfirmed(int id)
        {
            var membership = context.Memberships.Find(id);

            if (membership != null)
            {
                context.Memberships.Remove(membership);
                context.SaveChanges();
            }

            TempData["Message"] = "Abonamentul a fost șters cu succes!";

            return RedirectToAction(nameof(Index));
        }
    }
}

