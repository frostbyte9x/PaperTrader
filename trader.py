from stock_market import get_stock_price_v1, get_stock_price_v2, get_actual_stock_price
from utils import multiply, add, sub, print_divider
import time
from data import TradeDB

if __name__ == "__main__": 
    db = TradeDB('trade_values.db')
    while True:
        print_divider()
        print('PaperTrader v0.1')
        print_divider()
        choice = input('Enter input: ')

        if choice == '1':
            sym = input('Enter stock name: ')
            current_price = get_actual_stock_price(sym)
            if current_price:
                vol = int(input('Enter quantity: '))
                price = multiply(current_price, vol)
                print(f'{vol} shares bought for {sym}, Total value: {price}')
            else: 
                print(f'No stock data exists for {sym}.')
        
        if choice == 'exit': 
            break