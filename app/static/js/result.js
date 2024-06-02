function applyResultStyling() {
    var resultElement = document.getElementById('result');
    var resultText = resultElement.innerText.trim().toUpperCase();
    if (resultText === 'NÃO HÁ CHANCES DE SUBSCRIÇÃO') {
        resultElement.classList.add('no-chance');
    } else if (resultText === 'HÁ CHANCES DE SUBSCRIÇÃO') {
        resultElement.classList.add('chance');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    applyResultStyling();
});


function goBack() {
    window.history.back(); // Função para voltar à página anterior
}
