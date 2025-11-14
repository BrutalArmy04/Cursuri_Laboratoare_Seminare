using Lab3.Controllers;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseRouting();   //activeaza rutarea

app.UseAuthorization();

app.MapStaticAssets();

// Exercitiul 1

// /concatenare -> asta vreau sa scriu pe browser si sa se execute

// /concatenare/a=valoare/b=valoare

app.MapControllerRoute(
    name: "Concatenare", 
    pattern: "concatenare/{a?}/{b?}" /*nu punem din nou / pt ca este deja (la inceput)*/,
    defaults: new {controller = "Examples" /*tot ce este din nume pana la controller al controllerului*/, action = "Concatenare"}
    );

app.MapControllerRoute(
    name: "Produs",
    pattern: "produs/{x}/{y?}",
    defaults: new {controller = "Examples", action = "Produs"}
    );

app.MapControllerRoute(
    name: "Operatie",
    pattern: "operatie/{op1?}/{op2?}/{oper?}",
    defaults: new { controller = "Examples", action = "Operatie" }
    );

//Ex 2

// /Students/Index (var 1)

app.MapControllerRoute(
    name: "StudentsIndex",
    pattern: "{controller=Students}/{action=Index}"
    );

// students/all (var 2)

app.MapControllerRoute(
    name:"StudentsAll",
    pattern: "StudentsController/all",
    defaults: new {controller = "Students", action = "Index"}
    );

//show
// students/{id}

app.MapControllerRoute(
    name: "StudentsShow",
    pattern: "students/show/{id?}",
    defaults: new {controller = "Students", action = "Show"}
    );

//editare
// students/{id}

app.MapControllerRoute(
    name: "StudentsEdit",
    pattern: "students/edit/{id?}",
    defaults: new { controller = "Students", action = "Edit" }
    );

//delete
// students/{id}

app.MapControllerRoute(
    name: "StudentsDelete",
    pattern: "students/delete/{id?}",
    defaults: new { controller = "Students", action = "Delete" }
    );

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}")  // ruta generala, by default
    .WithStaticAssets();    // nu se mai incarca din nou toate asseturile, incarca din cacheul intern


app.Run();
