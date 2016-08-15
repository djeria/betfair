import sqlite3


class SqlServer:

    def __init__(self):
        self.db = sqlite3.connect('D:/data/market.db')
        self.cursor = self.db.cursor()

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()

    def drop_table(self, table):
        self.cursor.execute('''DROP TABLE %s''' % table)
        self.commit()

    def create_quotes_table(self):
        self.cursor.execute('''
            CREATE TABLE quotes(
                marketId STRING,
                marketState STRING,
                runnerName STRING,
                bestBackPrice REAL,
                bestBackSize REAL,
                bestLayPrice REAL,
                bestLaySize REAL,
                time TIMESTAMP)
            ''')
        self.commit()

    def insert_quote(self, market_id, market_state, runner_name, best_back_price,
                      best_back_size, best_lay_price, best_lay_size, time):
        self.cursor.execute('''
            INSERT INTO quotes(
                marketId,
                marketState,
                runnerName,
                bestBackPrice,
                bestBackSize,
                bestLayPrice,
                bestLaySize,
                time)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        ''', (market_id, market_state, runner_name, best_back_price, best_back_size,
              best_lay_price, best_lay_size, time))
        self.commit()

    def clear_quotes_table(self):
        self.cursor.execute('''DELETE from quotes''')
        self.commit()

handle = SqlServer()
