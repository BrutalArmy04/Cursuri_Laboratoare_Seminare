using ExercitiuLaborator12.Models;

namespace ExercitiuLaborator12.Data
{
    public static class SeedData
    {
        public static void Initialize(AppDbContext context)
        {
            if (!context.Gyms.Any())
            {
                context.Gyms.AddRange(
                    new Gym { Name = "Stay Fit Gym" },
                    new Gym { Name = "World Class" },
                    new Gym { Name = "700 Fit Club" }
                );

                context.SaveChanges();
            }
        }
    }
}
