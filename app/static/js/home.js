 // Função para configurar um gráfico de barra
 function setupBarChart(ctx, data) {
    return new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Função para configurar um gráfico de barras horizontais
function setupHorizontalBarChart(ctx, data) {
    return new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            indexAxis: 'y',
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Função para configurar um gráfico de linha
function setupLineChart(ctx, data) {
    return new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Dados para os gráficos
const chartData = {
    labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
    datasets: [{
        label: 'Idade',
        data: [25, 30, 35, 40, 45, 50],
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
    }, {
        label: 'Saldo',
        data: [500, 700, 600, 800, 1000, 900],
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
    }, {
        label: 'Duração',
        data: [10, 15, 20, 25, 30, 35],
        backgroundColor: 'rgba(255, 206, 86, 0.2)',
        borderColor: 'rgba(255, 206, 86, 1)',
        borderWidth: 1
    }, {
        label: 'Dias anteriores',
        data: [3, 4, 2, 5, 6, 7],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }, {
        label: 'Anteriores',
        data: [2, 3, 1, 4, 5, 6],
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
        borderColor: 'rgba(153, 102, 255, 1)',
        borderWidth: 1
    }, {
        label: 'Campanha',
        data: [1, 0, 2, 1, 3, 2],
        backgroundColor: 'rgba(255, 159, 64, 0.2)',
        borderColor: 'rgba(255, 159, 64, 1)',
        borderWidth: 1
    }]
};

// Obtendo os contextos dos gráficos
const ctxBar = document.getElementById('barChart').getContext('2d');
const ctxHorizontalBar = document.getElementById('horizontalBarChart').getContext('2d');
const ctxLine = document.getElementById('lineChart').getContext('2d');

// Configurando os gráficos
const barChart = setupBarChart(ctxBar, chartData);
const horizontalBarChart = setupHorizontalBarChart(ctxHorizontalBar, chartData);
const lineChart = setupLineChart(ctxLine, chartData);

// Eventos de abertura e fechamento do modal (preservados conforme o código original)
document.getElementById('btn-predict').addEventListener('click', function() {
    console.log('OHHH caraiii');
    $('.modal').modal('show');
});

document.querySelector('.btn-close').addEventListener('click', function() {
    $('#exampleModalCenter').modal('hide');
});

document.querySelector('.btn-secondary').addEventListener('click', function() {
    $('#exampleModalCenter').modal('hide');
});