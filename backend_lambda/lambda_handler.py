import json
import yfinance as yf
import boto3
import joblib
import io
from utils import classify_trend

MODEL_BUCKET = "stock-trend-models"
MODEL_KEY = "models/model.joblib"
SCALER_KEY = "models/scaler.joblib"

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    model_obj = s3.get_object(Bucket=MODEL_BUCKET, Key=MODEL_KEY)
    scaler_obj = s3.get_object(Bucket=MODEL_BUCKET, Key=SCALER_KEY)

    model = joblib.load(io.BytesIO(model_obj['Body'].read()))
    scaler = joblib.load(io.BytesIO(scaler_obj['Body'].read()))

    body = json.loads(event['body'])
    tickers = body['tickers']

    results = []
    for t in tickers:
        data = yf.download(t, period="5d", interval="1h")
        trend, dates, prices = classify_trend(data, model, scaler)
        results.append({"ticker": t, "trend": trend, "dates": dates, "prices": prices})

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(results)
    }
