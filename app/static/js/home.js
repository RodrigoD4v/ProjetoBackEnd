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

// Obtendo o contexto do gráfico de barras
const ctxBar = document.getElementById('barChart').getContext('2d');

// Fazendo uma solicitação GET para obter os dados dos clientes
fetch('/ecclientes')
    .then(response => response.json())
    .then(data => {
        // Configurando o gráfico de barras com os dados recebidos
        setupBarChart(ctxBar, {
            labels: data.labels,
            datasets: [{
                label: 'Número de Clientes',
                data: data.values,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        });
    })
    .catch(error => console.error('Error fetching data:', error));

//////////////////////////////////////////////////////////////////////////////////////////////////

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






////////////////////////////////////////////////////////////////////////////////////////////////////

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

// Dados 
// Obtendo os contextos dos gráficos
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