using System.ComponentModel.DataAnnotations;

namespace ExercitiuLaborator12.Models
{
    public class Membership
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public string Title { get; set; }
        [Required]
        [Range(1, int.MaxValue)]
        public int Value { get; set; }
        [Required(ErrorMessage ="Data emiterii este obligatorie!")]
        public DateTime Date { get; set; }
        [Required(ErrorMessage ="Este obligatoriu sa introduceti numele salii de sport!")]
        public int GymId {  get; set; }

        public virtual Gym? Gym { get; set; }
    }
}
