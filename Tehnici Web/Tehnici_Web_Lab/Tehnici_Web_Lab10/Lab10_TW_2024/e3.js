window.onload = function () {
    let select = document.getElementById('categorie');
    let sectiune = document.getElementById('carti');

    select.onchange = function () {
        let url = `localhost:8000/${select.value}.json`;
        fetch(url).then(function (response) {
            if (response.status == '200')
                return response.json();
            else { alert('eroare'); throw ('eroare') }
        }
    }
}