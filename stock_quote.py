import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

symbol = 'AAPL'
quote = finnhub_client.quote(symbol)

print(quote)
