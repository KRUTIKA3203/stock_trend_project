async function fetchTrends() {
    const tickers = document.getElementById('tickers').value.split(',').map(t => t.trim());
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ tickers })
    });
    const data = await response.json();
    displayResults(data);
    plotCharts(data);
}

function displayResults(data) {
    let html = "<table border='1' style='margin:auto'><tr><th>Ticker</th><th>Trend</th></tr>";
    data.forEach(stock => {
        html += `<tr><td>${stock.ticker}</td><td>${stock.trend}</td></tr>`;
    });
    html += "</table>";
    document.getElementById('result').innerHTML = html;
}

function plotCharts(data) {
    const traces = data.map(stock => ({
        x: stock.dates,
        y: stock.prices,
        mode: 'lines',
        name: stock.ticker
    }));
    Plotly.newPlot('chart', traces, { title: 'Stock Price Trends' });
}

setInterval(fetchTrends, 300000); // auto refresh every 5 mins
