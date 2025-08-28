// audio.js
const form = document.getElementById("audioForm");
const processBtn = document.getElementById("processBtn");
const btnText = processBtn.querySelector(".btn-text");
const btnLoading = processBtn.querySelector(".btn-loading");
const resultsDiv = document.getElementById("results");
const transcriptionDiv = document.getElementById("transcription");
const translationDiv = document.getElementById("translation");
const errorDiv = document.getElementById("error");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("audio_file");
    if (!fileInput.files.length) {
        alert("Por favor selecciona un archivo de audio");
        return;
    }

    const formData = new FormData();
    formData.append("audio_file", fileInput.files[0]);
    formData.append("source_language", document.getElementById("source_language").value);
    formData.append("target_language", document.getElementById("target_language").value);

    btnText.style.display = "none";
    btnLoading.style.display = "inline";

    try {
        const response = await fetch("/process_audio", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            errorDiv.style.display = "block";
            errorDiv.innerText = data.error;
            resultsDiv.style.display = "none";
        } else {
            resultsDiv.style.display = "block";
            errorDiv.style.display = "none";
            transcriptionDiv.innerText = data.transcription;
            translationDiv.innerText = data.translation;
        }

    } catch (err) {
        console.error(err);
        errorDiv.style.display = "block";
        errorDiv.innerText = "Error al procesar el audio.";
        resultsDiv.style.display = "none";
    } finally {
        btnText.style.display = "inline";
        btnLoading.style.display = "none";
    }
});

// Función para leer la traducción en voz alta
function leerTraduccion() {
    const texto = translationDiv.innerText;
    if (texto.trim() === "") {
        alert("No hay texto traducido para leer.");
        return;
    }
    const targetLang = document.getElementById("target_language").value;
    const utterance = new SpeechSynthesisUtterance(texto);
    utterance.lang = targetLang + "-" + targetLang.toUpperCase();
    speechSynthesis.speak(utterance);
}
