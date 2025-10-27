import numpy as np

def classify_trend(data, model, scaler):
    data['Change'] = data['Close'].pct_change()
    data = data.dropna()
    features = data[['Change']].values
    scaled = scaler.transform(features)
    preds = model.predict(scaled)
    last_trend = preds[-1]
    trend = "Buy" if last_trend == 1 else "Sell"
    return trend, list(data.index.strftime('%Y-%m-%d %H:%M')), list(data['Close'])
