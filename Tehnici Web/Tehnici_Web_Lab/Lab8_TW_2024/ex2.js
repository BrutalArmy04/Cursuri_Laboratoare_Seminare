window.addEventListener("load", function () {
    let t = setInterval(function () {
        let x = Math.floor(Math.random() * window.innerWidth - 50);
        let y = Math.floor(Math.random() * window.innerHeight - 50);
        let b = document.createElement("button");
        b.style.width = "50px";
        b.style.height = "50px";
        b.style.borderRadius = "10px";
        b.style.backgroundColor = `rgb(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)})`;
        document.body.appendChild(b);
        b.indice = i;
        b.style.position = "absolute";
        b.style.left = x + "px";
        b.style.top = y + "px";
        i++;
        if (i == 4) clearInterval(t);   

    }, 2000);
    document.body.addEventListener("keydown", function (event) {
        let butoane = document.getElementsByTagName("button");
        if ((butoane.length == 4) && (event.key = 's')) {
            for (let b of butoane) {
                b.addEventListener("click", function () {
                    if (b.indice == nr) {
                        b.style.backgroundColor = "red";
                        b.innerHTML = b.indice;
                        if (nr == 3) { alert("Ai castigat!"); }
                    }
                    else {
                        alert("Ai pierdut jocul!");
                        for (let b of butoane) {
                            b.remove();
                        }
                        nr++;
                    }
                }
            }
        }
    })
});