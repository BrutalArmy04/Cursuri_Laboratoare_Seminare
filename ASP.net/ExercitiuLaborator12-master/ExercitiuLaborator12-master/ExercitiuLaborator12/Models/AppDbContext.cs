using Microsoft.EntityFrameworkCore;

namespace ExercitiuLaborator12.Models
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options)
        : base(options)
        {
        }

        public DbSet<Gym> Gyms { get; set; }
        public DbSet<Membership> Memberships { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<Membership>()
                .HasOne(m => m.Gym)
                .WithMany(g => g.Memberships)
                .HasForeignKey(m => m.GymId)
                .OnDelete(DeleteBehavior.Cascade);
        }
    }
}
