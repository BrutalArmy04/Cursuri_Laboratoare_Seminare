let cosCumparaturi = {
    faina: 12.5,
    unt: 15,
    out: 10,
    cascaval: 20.3
};
function valoareCos(lista)
{
    let total = 0;
    for (let k in lista)
    {
        console.log(k);
        total += lista[k];
    }
    return total;
}
console.log(`Valoarea totala a cosului este ${valoareCos(cosCumparaturi)} ron`)
function adaugaIngredient(ingredient, pret) {
    cosCumparaturi[ingredient] = pret;
    console.log(cosCumparaturi);
}
adaugaIngredient('sare', 2)
console.log(`Valoarea totala a cosului este ${valoareCos(cosCumparaturi)} ron`)

var retete = [
    { nume: "Pateuri cu cascaval", timpPreparare: 45, ingrediente: ["făină", "unt", "cașcaval", "ouă"] },
    { nume: "Salata de fructe", timpPreparare: 15, ingrediente: ["mere", "banane", "portocale", "struguri"] },
    { nume: "Supa de legume", timpPreparare: 30, ingrediente: ["ceapă", "morcovi", "cartofi", "pătrunjel"] },
    { nume: "Pizza", timpPreparare: 60, ingrediente: ["făină", "roșii", "brânză", "ciuperci"] },
    { nume: "Tort de ciocolata", timpPreparare: 90, ingrediente: ["făină", "ciocolată", "ouă", "zahăr"] }
];
function cautaReteta(reteta) {
    for (let r of retete) {
        if (r.nume.toLowerCase() == reteta.toLowerCase()) {
            return r;
        }
    }
    return null;
}
function afiseazaReteta() {
    let promptReteta = prompt("Introduceti un nume de reteta");
    let r = cautaReteta(promptReteta);
    if (r) {
        alert(`${r.nume} se prepara in ${r.timpPreparare}. Ingrediente: ${r.ingrediente.join("/")}`)
    }
    else { alert("Nu exista reteta") }
}
//afiseazaReteta()

function cautaRetete(timp) {
    let reteteMax = []
    for (let r of retete) {
        if (r.timpPreparare <= timp) {
            reteteMax.push(r.nume);
        }
    }
    return reteteMax
}

function afiseazaRetete()
{
    let promptTimp = parseInt(prompt("introduceti un timp maxim"));
    let reteteMax = cautaRetete(promptTimp);
    if (reteteMax.length > 0) {
        alert(`Retetele care se prepara in maxim ${promptTimp} de minute sunt: ${reteteMax}`);

    }
    else { alert(`Nu exista retete care se prepara in ${promptTimp} minute`); }
}
//afiseazaRetete()
var sfaturiDeGatit = [
    "Întotdeauna citește rețeta complet înainte de a începe.",
    "Măsoară ingredientele cu precizie pentru cele mai bune rezultate.",
    "Gătește la foc mic pentru a evita arderea mâncării.",
    "Folosește ingrediente proaspete pentru un gust mai bun.",
    "Nu te teme să experimentezi cu condimentele!"
];
function schimbaContinut() {
    let indice = Math.floor(Math.random() * sfaturiDeGatit.length)
    let paragraf = document.getElementById("par1");
    console.log(paragraf.innerHTML);
    paragraf.innerHTML = sfaturiDeGatit[indice];
}
//schimbaContinut()

function schimbaTitle() {
    let title = document.querySelector("title");
    title.innerHTML = `Salut, ${prompt("Numele:")}`;
}
//schimbaTitle()

function schimbaImagini() {
    let colectie = document.querySelectorAll("#galerie img")
    for (let c of colectie) {
        c.src = "https://media.tenor.com/7qFULBHgzlYAAAAi/bubu-cooking-dudu-bubu.gif";
        c.alt = "bubu gateste";
    }
}
schimbaImagini()
function schimbaCaption() {
    let texte = document.querySelectorAll("#galerie figcaption");
    for (let i = 0; i < texte.length; i++) {
        texte[i].innerHTML = `Figura ${i+1}`
    }
}
schimbaCaption()

function majuscule() {
    let elemente = document.querySelectorAll("ol > li")
    for (let e in elemente) {
        e.innerHTML = e.innerHTML.toUpperCase();
        e.style.color = "green";
    }
}
// majuscule()