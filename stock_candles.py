import finnhub
import datetime

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

symbol = 'AAPL'
start = int(datetime.datetime(2023, 1, 1).timestamp())
end = int(datetime.datetime(2023, 12, 31).timestamp())

candles = finnhub_client.stock_candles(symbol, 'D', start, end)
print(candles)
