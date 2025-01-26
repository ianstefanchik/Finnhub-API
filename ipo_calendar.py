import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

ipos = finnhub_client.ipo_calendar(from_='2024-01-01', to_='2024-12-31')
print(ipos)
