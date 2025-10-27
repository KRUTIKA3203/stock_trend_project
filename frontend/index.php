<?php include 'config.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Stock Trend Classifier</title>
<link rel="stylesheet" href="assets/style.css">
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="assets/chart.js"></script>
</head>
<body>
    <h1>📈 Stock Trend Classifier</h1>
    <div class="input-section">
        <input type="text" id="tickers" placeholder="Enter tickers (AAPL, MSFT, TSLA)">
        <button onclick="fetchTrends()">Analyze</button>
    </div>

    <div id="result"></div>
    <div id="chart"></div>

    <script>
        const API_URL = "<?php echo API_URL; ?>";
    </script>
</body>
</html>
