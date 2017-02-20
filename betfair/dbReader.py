import sqlite3
from datetime import datetime
from configparser import ConfigParser
from tabulate import tabulate


class SqlServer:

    def __init__(self, db):
        self.db_conn = sqlite3.connect(db)
        self.db_conn.row_factory = sqlite3.Row
        self.cursor = self.db_conn.cursor()

    def close(self):
        self.db_conn.close()

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
                marketState,
                runnerName,
                bestBackPrice,
                bestBackSize,
                bestLayPrice,
                bestLaySize,
                strftime('%%Y-%%m-%%d %%H:%%M:%%S', time) as time
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
            if quote['marketState'] == 'OPEN':
                time.append(datetime.strptime(quote['time'], '%Y-%m-%d %H:%M:%S'))
                back_price.append(quote['bestBackPrice'])
                back_size.append(quote['bestBackSize'])
                lay_price.append(quote['bestLayPrice'])
                lay_size.append(quote['bestLaySize'])

        quotes = {
            'time': time,
            'back_price': back_price,
            'back_size': back_size,
            'lay_price': lay_price,
            'lay_size': lay_size,
        }

        return quotes

config = ConfigParser()
config.read('config.ini')

local_db = config.get('main', 'db')

handle = SqlServer(local_db)