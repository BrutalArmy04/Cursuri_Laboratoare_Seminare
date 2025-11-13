window.onload = function () {
    let input = document.getElementById('mesaj');
    let buton = documet.getElementById('salveaza');
    let paragraf = document.querySelector('.afiseaza');
    let sterge = document.getElementById('alege');
    sterge.onclick = function () {
        localStorage.removeItem('mesaj');
        paragraf.innerHTML = 'Nici un string'
    }
    buton.onclick = function () {
        localStorage.setItem('mesaj', input.value);
        alert('Mesajul a fost salvat');
        paragraf.textContent = input.value;
    }
}