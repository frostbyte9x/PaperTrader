import sqlite3
from datetime import date

class TradeDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS trades
            (id INTEGER PRIMARY KEY, trade_date DATE, symbol TEXT, quantity INTEGER, buy_price REAL, sell_price REAL)
        ''')
        self.conn.commit()

    def add_trade(self, trade_date, symbol, quantity, buy_price, sell_price):
        self.cursor.execute('''
            INSERT INTO trades (trade_date, symbol, quantity, buy_price, sell_price)
            VALUES (?, ?, ?, ?)
        ''', (trade_date, symbol, quantity, buy_price, sell_price))
        self.conn.commit()

    def get_trades(self):
        self.cursor.execute('SELECT * FROM trades')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()


# Example usage
# db = TradeDB('trade_values.db')

# # Add trades
# db.add_trade(date.today().isoformat(), 'AAPL', 'B', 100, 145.50)
# db.add_trade(date.today().isoformat(), 'GOOG', 'S', 50, 2750.25)

# # Retrieve trades
# trades = db.get_trades()
# for trade in trades:
#     print(trade)

# # Close the database connection
# db.close_connection()