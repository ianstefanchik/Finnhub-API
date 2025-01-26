import finnhub

api_key = 'YOUR_API_KEY'
finnhub_client = finnhub.Client(api_key=api_key)

news = finnhub_client.general_news('general')

for article in news[:5]:
    print(article['headline'])
    print(article['url'])
    print()
