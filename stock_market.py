import yahooquery as yq
import yfinance as yf
import requests as req
from bs4 import BeautifulSoup as crawler 

def get_stock_price_v1(stock_name=None):
    try:
        ticker = yq.Ticker(stock_name + ".NS")
        summary_detail = ticker.summary_detail[(stock_name + ".NS")]
        print(ticker.summary_detail)
        return summary_detail['currentPrice']
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_stock_price_v2(stock_name = None): 
    try: 
        ticker = yf.Ticker(stock_name + ".NS")
        return ticker.info['currentPrice']
    except Exception: 
        pass 

def get_actual_stock_price(ticker = None):
    try:
        url = f"https://www.google.com/finance/quote/{ticker}:NSE"
        res = req.get(url)
        soup = crawler(res.text, 'html.parser')
        return float(soup.find(class_ = "YMlKec fxKbKc").text.strip()[1:].replace(',', ''))
    except Exception: 
        return None

