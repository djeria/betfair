import sqlite3
from datetime import datetime
from tabulate import tabulate

class SqlServer:

    def __init__(self):
        self.db = sqlite3.connect('D:/data/market.db')
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    def get_stored_markets(self):
        self.cursor.execute('''
            SELECT distinct
                DATE(time),
                marketId,
                runnerName
            from quotes''')
        return self.cursor.fetchall()

    def show_stored_markets(self):
        markets = self.get_stored_markets()
        print tabulate(markets, headers=["Date", "Market Id", "Runner"], floatfmt=".9f")

    def get_quotes_table(self, market_id, runner_name):
        self.cursor.execute('''
            SELECT
                marketId,
                runnerName,
                bestBackPrice,
                bestBackSize,
                bestLayPrice,
                bestLaySize,
                strftime('%%Y-%%m-%%d %%H:%%M:%%S', time)
            from quotes
            where marketId='%s'
            and runnerName='%s'
            and bestBackPrice > 0
            and bestBackPrice < 500
            and bestLayPrice > 0
            and bestLayPrice < 500
        ''' % (market_id, runner_name))
        return self.cursor.fetchall()

    def get_quotes(self, market_id, runner_name):
        time = []
        back_price = []
        back_size = []
        lay_price = []
        lay_size = []

        for quote in self.get_quotes_table(market_id, runner_name):
            time.append(datetime.strptime(quote[6], '%Y-%m-%d %H:%M:%S'))
            back_price.append(quote[2])
            back_size.append(quote[3])
            lay_price.append(quote[4])
            lay_size.append(quote[5])

        quotes = {
            'time': time,
            'back_price': back_price,
            'back_size': back_size,
            'lay_price': lay_price,
            'lay_size': lay_size,
        }

        return quotes

handle = SqlServer()