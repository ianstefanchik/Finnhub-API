import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

forex = finnhub_client.forex_rates(base='USD')
print(forex)
