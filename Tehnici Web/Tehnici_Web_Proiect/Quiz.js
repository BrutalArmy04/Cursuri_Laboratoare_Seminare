// Elemente globale
let currentQuestion = 0;
let score = 0;
let questions = []; // Va fi populat din JSON

// Salvarea progresului în localStorage
function saveProgress() {
    localStorage.setItem("quizProgress", JSON.stringify({ currentQuestion, score }));
}

// Încărcarea progresului din localStorage
function loadProgress() {
    let progress = JSON.parse(localStorage.getItem("quizProgress"));
    if (progress) {
        currentQuestion = progress.currentQuestion;
        score = progress.score;
    }
}

// Creare și ștergere de mesaje temporare
function createMessage(message) {
    let msg = document.createElement("div");
    msg.textContent = message;
    msg.classList.add("message");
    document.body.appendChild(msg);
    setTimeout(() => msg.remove(), 3000);
}

// Încărcarea întrebării curente
function loadQuestion() {
    if (!questions || questions.length === 0) {
        console.error("Nu există întrebări încărcate.");
        createMessage("Eroare: Întrebările nu sunt disponibile.");
        return;
    }
    let questionElem = document.getElementById("question");
    let optionsElem = document.getElementById("options");
    let progressElem = document.getElementById("progress");

    let question = questions[currentQuestion];
    if (!question) {
        console.error(`Întrebarea curentă (${currentQuestion}) nu există.`);
        createMessage("Eroare: Întrebarea curentă nu este disponibilă.");
        return;
    }
    questionElem.textContent = question.question;

    optionsElem.innerHTML = ""; // Golim opțiunile
    question.options.forEach((option, index) => {
        let btn = document.createElement("button");
        btn.textContent = option;
        btn.classList.add("option");
        btn.addEventListener("click", (e) => handleAnswer(index, e));
        optionsElem.appendChild(btn);
    });

    progressElem.textContent = `Întrebarea ${currentQuestion + 1} din ${questions.length}`;
}

// Verificarea răspunsului
function handleAnswer(selectedIndex, event) {
    if (selectedIndex === questions[currentQuestion].answer) score++;

    event.target.style.backgroundColor = "green";
    setTimeout(() => {
        currentQuestion++;
        if (currentQuestion < questions.length) {
            console.log("Questions array:", questions);
            loadQuestion();
            saveProgress();
        } else {
            showResults();
        }
    }, 500);
}

// Afișarea rezultatelor
function showResults() {
    let quizElem = document.getElementById("quiz");
    let resultsElem = document.getElementById("results");

    quizElem.style.display = "none";
    resultsElem.style.display = "block";
    resultsElem.innerHTML = `<h2>Rezultatul tău: ${score} din ${questions.length}</h2>`;
    localStorage.removeItem("quizProgress");
}

// Funcție pentru restart
function restartQuiz() {
    currentQuestion = 0;
    score = 0;
    saveProgress();
    loadQuestion();
    document.getElementById("quiz").style.display = "block";
    document.getElementById("results").style.display = "none";
}

// Event Listeners pentru Login și Logout
function handleLogin() {
    let username = document.getElementById("username").value;
    if (/^[a-zA-Z0-9_]{3,}$/.test(username)) { // Validare simplă
        localStorage.setItem("username", username);
        document.getElementById("login").style.display = "none";
        document.getElementById("quiz").style.display = "block";

        // Încarcă întrebările și inițializează quiz-ul
        loadQuestionsFromJSON()
            .then(() => {
                console.log("Întrebările sunt gata. Inițializare quiz.");
                loadProgress(); // Încarcă progresul anterior (dacă există)
                loadQuestion(); // Afișează prima întrebare
            })
            .catch(err => console.error("Eroare la inițializare:", err));
    } else {
        alert("Nume de utilizator invalid. Trebuie să conțină doar litere, cifre și să fie de cel puțin 3 caractere.");
    }
}



function handleLogout() {
    localStorage.removeItem("username");
    localStorage.removeItem("quizProgress");
    document.getElementById("login").style.display = "block";
    document.getElementById("quiz").style.display = "none";
}

// Cereri Ajax pentru preluare JSON
function loadQuestionsFromJSON() {
    return fetch("questions.json") // Asigură-te că returnezi acest Promise
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Întrebările încărcate:", data);
            questions.push(...data); // Adaugă datele încărcate în array-ul `questions`
        })
        .catch(err => {
            console.error("Eroare la încărcarea întrebărilor:", err);
            createMessage("Eroare la încărcarea întrebărilor.");
        });
}


// Funcții suplimentare: canvas, fundal aleator, timp curent
function drawCanvas() {
    let canvas = document.getElementById("quizCanvas");
    let ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FFCC00";
    ctx.fillRect(10, 10, 150, 100);
    ctx.fillStyle = "#000";
    ctx.font = "20px Arial";
    ctx.fillText("Succes!", 20, 50);
}

function randomizeBackgroundColor() {
    document.body.style.backgroundColor = `rgb(${Math.random() * 256}, ${Math.random() * 256}, ${Math.random() * 256})`;
}

function showCurrentTime() {
    let now = new Date();
    createMessage(`Ora curentă: ${now.getHours()}:${now.getMinutes()}:${now.getSeconds()}`);
}

// Inițializare
window.onload = () => {
    let username = localStorage.getItem("username");
    if (username) {
        document.getElementById("login").style.display = "none";
        document.getElementById("quiz").style.display = "block";
        loadProgress();
        console.log(questions);

    } else {
        document.getElementById("login").style.display = "block";
        document.getElementById("quiz").style.display = "none";
    }
    setInterval(randomizeBackgroundColor, 5000);
    drawCanvas();
    showCurrentTime();
};
