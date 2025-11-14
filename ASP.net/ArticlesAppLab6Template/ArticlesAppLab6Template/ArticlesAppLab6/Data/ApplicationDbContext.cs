using ArticlesApp.Models;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

namespace ArticlesAppLab6.Data
{
    public class ApplicationDbContext : IdentityDbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }
        
    }

    public DBSet<Article> Articles { get; set; }
    public DBSet<Category> Categories { get; set; }
    public DBSet<Comment> Comments { get; set; }
    }
