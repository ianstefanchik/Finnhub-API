import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

symbol = 'AAPL'
news_sentiment = finnhub_client.news_sentiment(symbol)
print(news_sentiment)
