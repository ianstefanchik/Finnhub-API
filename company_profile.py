import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

symbol = 'AAPL'
profile = finnhub_client.company_profile2(symbol=symbol)

print(profile)
