import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

earnings = finnhub_client.earnings_calendar(symbol='AAPL')
print(earnings)
