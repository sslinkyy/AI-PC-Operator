import yfinance as yf
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

class StockAnalyst(NeuralNetworkAgent):
    def __init__(self, name, supervisor):
        super().__init__(name, level=2, supervisor=supervisor)
        supervisor.add_subordinate(self)

    def execute_task(self, user_command):
        if user_command.startswith("analyze_stock"):
            _, stock_symbol = user_command.split()
            return self.analyze_stock(stock_symbol)
        return self.respond(f"Unknown command: {user_command}")

    def analyze_stock(self, stock_symbol):
        stock_data = self.get_stock_data(stock_symbol)
        market_sentiment = self.get_market_sentiment(stock_symbol)
        news_analysis = self.get_news_analysis(stock_symbol)
        
        analysis_result = {
            "stock_data": stock_data,
            "market_sentiment": market_sentiment,
            "news_analysis": news_analysis
        }
        
        self.knowledge[f'analyze_stock {stock_symbol}'] = analysis_result
        self.save_knowledge()
        return self.respond(f"Analysis for {stock_symbol}: {analysis_result}")
    
    def get_stock_data(self, stock_symbol):
        stock = yf.Ticker(stock_symbol)
        hist = stock.history(period="1mo")
        return hist.tail().to_dict()

    def get_market_sentiment(self, stock_symbol):
        news_headlines = self.get_news_analysis(stock_symbol)
        sentiments = [TextBlob(headline).sentiment.polarity for headline in news_headlines]
        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        return "Positive" if avg_sentiment > 0 else "Negative"

    def get_news_analysis(self, stock_symbol):
        url = f"https://news.google.com/search?q={stock_symbol}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [title.get_text() for title in soup.find_all('a', class_='DY5T1d')]
        return headlines[:5]
