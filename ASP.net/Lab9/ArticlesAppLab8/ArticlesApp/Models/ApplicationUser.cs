using Microsoft.AspNetCore.Identity;

namespace ArticlesApp.Models
{
    public class ApplicationUser : IdentityUser // trb importata bilioteca
    {
        // un user poate posta mai multe articole

        public virtual ICollection<Article> Articles { get; set; } = [];
        // un user poate posta mai multe comentarii
        public virtual ICollection<Comment> Comments { get; set; }
    }
}
