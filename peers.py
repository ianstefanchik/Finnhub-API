import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

symbol = 'AAPL'
peers = finnhub_client.company_peers(symbol)
print(peers)
