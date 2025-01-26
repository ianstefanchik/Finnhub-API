import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

symbol = 'AAPL'
financials = finnhub_client.company_basic_financials(symbol, 'all')
print(financials)
