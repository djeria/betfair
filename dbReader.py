import sqlite3
from datetime import datetime


class SqlServer:

    def __init__(self):
        self.db = sqlite3.connect('D:/data/market.db')
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    def get_quotes_table(self, market_id, runner_name):
        self.cursor.execute('''
            SELECT * from quotes
            where marketId='%s'
            and runnerName='%s'
        ''' % (market_id, runner_name))
        return self.cursor.fetchall()

    def get_quotes(self, market_id, runner_id):
        time = []
        back_price = []
        back_size = []
        lay_price = []
        lay_size = []

        for quote in self.get_quotes_table(market_id, runner_id):
            time.append(datetime.strptime(quote[6], '%Y-%m-%d %H:%M:%S.%f'))
            back_price.append(quote[2])
            back_size.append(quote[3])
            lay_price.append(quote[4])
            lay_size.append(quote[5])

        return (time, back_price, back_size, lay_price, lay_size)

handle = SqlServer()