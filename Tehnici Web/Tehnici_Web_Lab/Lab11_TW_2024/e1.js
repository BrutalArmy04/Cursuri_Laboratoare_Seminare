window.onload = function () {
    let buton = document.getElementById('btn');
    let div = document.getElementById('msg');

    buton.onclick = function () {
        let url = 'http://localhost:9090/mesaje.json';
        fetch(url).then(function (response) {
            if (response.status == 200) {
                return response.json();
            }
            else {
                throw new Error("statusul este" + response.status);
            }
        }).then(function (dateJS) {
            //let dateJS = JSON.parse(date);
            let indiceRandom = Math.floor(Math.random() * dateJS.length);
            div.innerHTML = dateJS[indiceRandom].mesaj;
        }).catch(function (err) {
            console.error('A aparut o eroare:' + err.message);
        }
    }

}
