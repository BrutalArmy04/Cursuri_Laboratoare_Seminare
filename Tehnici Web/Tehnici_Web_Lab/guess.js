window.onload = guess; // la incarcarea paginii se va apela functia guess
function guess() {
    let mesaj = document.querySelector(".message");
    let nume = prompt("Numele jucatorului ");
    mesaj.innerHTML += ` ${nume}`;
    let nrSecret = Math.floor(Math.random() * 20) + 1; // nr random intre 1 si 20
    console.log(nrSecret);
    let input = document.getElementById('guess');
    let buton = document.getElementById('check');
    buton.onclick = verifica;
    let s = 20;
    let i = 0;
    function verifica() {
        i++;
        if (i < 20) {
            if (nrSecret == parseInt(input.value)) {
                document.body.style.backgroundColor = "red";
                mesaj.innerHTML = `Ai castigat jocul!`;
                document.querySelector(".number").innerHTML = nrSecret;
                buton.disbled = true;
                let p = document.createElement("p");
                p.innerHTML = `Jucatorul ${nume} a castigat jocul cu scorul ${s}`;
                document.getElementById("jucatori").appendChild(p);
            }
            else {
                s--;
                if (nrSecret < parseInt(input.value)) {
                    mesaj.innerHTML = `Numarul e prea mare`;
                }
                else {
                    mesaj.innerHTML = `Numarul e prea mic`;
                }
            }
        }
        else {
            mesaj.innerHTML = `Ai pierdut jocul`;
            buton.disbled = true;
        }
        document.querySelector(".score").innerHTML = s;
        document.querySelector(".hightscore").innerHTML = i;
    }
}