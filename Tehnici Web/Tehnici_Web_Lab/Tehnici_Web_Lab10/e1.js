window.onload = function () {
    let input = document.getElementById('mesaj');
    let buton = document.getElementById('salveaza');
    let paragraf = document.querySelector('.afiseaza')
    let mesajSalvat = localStorage.getItem('mesaj');
    if (mesajSalvat) {
        localStorage.setItem('mesaj', input.value);
        alert('Mesajul a fost salvat!');
        paragraf.textContent = input.value;
    }
    else {
        alert('Nu ai introdus un mesaj')
    }
    buton.onclick = function (event) {
        event.stopPropagation();
        if (input.value) {
            localStorage.setItem('mesaj', input.value);
            alert('Mesajul a fost salvat');
            paragraf.textContent = input.value;
        }
        else { ('Nu ai introdus un mesaj') }
        localStorage.setItem('mesaj', input.value);
        alert('Mesajul a fost salvat');
        paragraf.textContent = input.value;
    }
    document.body.onclick = function () {

    }
    }
}
