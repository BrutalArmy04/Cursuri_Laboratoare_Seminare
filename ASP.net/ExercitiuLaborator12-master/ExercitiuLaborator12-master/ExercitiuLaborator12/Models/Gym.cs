using System.ComponentModel.DataAnnotations;

namespace ExercitiuLaborator12.Models
{
    public class Gym
    {
        [Key]
        public int Id { get; set; }
        [Required(ErrorMessage ="Va rugam, introduceti numele salii!")]
        public string Name { get; set; }

        public virtual ICollection<Membership>? Memberships { get; set; }
    }
}
