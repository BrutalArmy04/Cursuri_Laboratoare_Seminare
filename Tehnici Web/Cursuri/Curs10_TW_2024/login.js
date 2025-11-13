window.onload = function(){

  let form = document.getElementById("form");
  let user = document.getElementById("user");
  let parola = document.getElementById("parola");
  let mesaj = document.getElementById("welcome");
  let eroare = document.getElementById("eroare");
  let logout = document.getElementById("logout");

  // Verificăm dacă utilizatorul este logat
  function verificareStatus() {
    let userLogat = localStorage.getItem("username");
    if (userLogat) {
      // Utilizator logat
      mesaj.style.display = "block";
      username.textContent = userLogat;
      form.style.display = "none";
      logout.style.display = "block";
      eroare.style.display = "none";
    } else {
      // Utilizator nelogat
      mesaj.style.display = "none";
      form.style.display = "block";
      logout.style.display = "none";
      eroare.style.display = "block";
    }
  }
  verificareStatus();

  // Validam userul
  function validUser(user)
  {
    let u = /^[a-zA-Z][a-zA-Z0-9_]{2,}$/;
    return u.test(user);
  }

  // Validam parola
  function validParola(parola)
  {
    let p = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[?!$%&#@]).{5,}$/;
    return p.test(parola);
  }

  // Verificam userul si parola intr-un array de useri
  function verificareUser(user,parola){
    let useri = [{nume:"User1",parola:"Parola1!"},{nume:"User2",parola:"Parola2!"},{nume:"User3",parola:"Parola3!"}]
    for(let u of useri){
      if ((u.nume == user) && (u.parola == parola)) return true;
    }
    return false;
  }

  user.onchange = function(){
    let userValue = user.value;
    eroare.textContent ="";
    if(!validUser(userValue)){
      eroare.textContent = "User invalid";
    }
  }
  parola.onchange = function(){
    let parolaValue = parola.value;
    eroare.textContent ="";
    if(!validParola(parolaValue)){
      eroare.textContent = "Parola invalida";
    }
  }
  // Evenimentul de submit (logare)
  form.onsubmit = function(event){
    event.preventDefault();
    eroare.textContent ="";
    let username = user.value;
    let password = parola.value;
    if (verificareUser(username,password))
    {
      localStorage.setItem("username", username); // Salvăm utilizatorul în localStorage
      verificareStatus();
    }
    else{
      eroare.textContent ="Date de logare sunt invalide";
    }
  }

  // Eveniment de delogare
  logout.onclick = function(){
    localStorage.removeItem("username"); // Ștergem utilizatorul din localStorage
    verificareStatus();
  }
}
