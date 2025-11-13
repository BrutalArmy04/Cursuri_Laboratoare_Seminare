window.onload = function () {
    let n = document.getElementById('nume');
    let e = document.getElementById('email');
    let v = document.getElementById('varsta');
    let buton = document.getElementById('salveaza');
    let div = document.querySelector('#informatii');
    let dateSalvate = JSON.parse(lcoalStorage.getItem('date'))
    if (localStorage.getItem('date')) {
        let ob = JSON.parse(local`<p>${ob.nume}, ${ob.email}, ${ob.varsta}</p>`);
    }
    buton.onlick = function () {
        let ob = { nume: inputNume.value, email: inputEmail.value, varsta: inputVarsta.value };
        localStorage.setItem('date', JSON.stringify(ob));
        div.innerHTML = `<p>${ob.nume}, ${ob.email}, ${ob.varsta}</p>`;
    }
}

