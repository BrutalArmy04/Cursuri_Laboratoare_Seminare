window.onload = function () {
    let input = document.getElementById('mesaj');
    let buton = document.getElementById('salveaza');
    let paragraf = document.querySelector('.afiseaza')
    buton.onclick = function () {
        localStorage.setItem('mesaj', input.value);
        alert('Mesajul a fost salvat');
        paragraf.textContent = input.value;
    }
}
