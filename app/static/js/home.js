// Cor para as estruturas
const colors = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)',
    'rgba(255, 205, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)',
    'rgba(255, 99, 132, 0.2)'
];

// Função para configurar um gráfico de barra com interação de exibição do cargo ao passar o mouse
function setupBarChartWithHover(ctx, data) {
    return new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': ' + context.parsed.y;
                        }
                    }
                }
            },
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
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': ' + context.parsed.y;
                        }
                    }
                }
            },
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

// Fazendo uma solicitação GET para obter os dados dos clientes por emprego e cargo
fetch('/ecclientes')
    .then(response => response.json())
    .then(data => {
        const datasets = [{
            label: 'Numero de Trabalhadores',
            data: data.values,
            backgroundColor: colors,
            borderColor: colors,
            borderWidth: 1
        }];

        // Configurando o gráfico de barras com os dados recebidos
        setupBarChartWithHover(ctxBar, {
            labels: data.labels,
            datasets: datasets
        });
    })
    .catch(error => console.error('Error fetching job clients data:', error));

//////////////////////////////////////////////////////////////////////////////////////////////////

// Obtendo o contexto do gráfico de barras horizontais
const ctxHorizontalBar = document.getElementById('horizontalBarChart').getContext('2d');

// Fazendo uma solicitação GET para obter os dados dos clientes por estado civil
fetch('/maritalstatusclients')
    .then(response => response.json())
    .then(data => {
        const datasets = [{
            label: 'Estado Civil dos Clientes',
            data: data.values,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }];

        // Configurando o gráfico de barras horizontais com os dados recebidos
        new Chart(ctxHorizontalBar, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: datasets
            },
            options: {
                indexAxis: 'y',  // Configurando o eixo horizontal
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.dataset.label + ': ' + context.parsed.x;
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching marital status clients data:', error));

// Obtendo o contexto do gráfico de linha
const ctxLine = document.getElementById('lineChart').getContext('2d');

// Fazendo uma solicitação GET para obter os dados dos clientes por educação
fetch('/educationclients')
    .then(response => response.json())
    .then(data => {
        const datasets = [{
            label: 'Educação dos Clientes',
            data: data.values,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            fill: false
        }];

        // Configurando o gráfico de linha com os dados recebidos
        setupLineChart(ctxLine, {
            labels: data.labels,
            datasets: datasets
        });
    })
    .catch(error => console.error('Error fetching education clients data:', error));