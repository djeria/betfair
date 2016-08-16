import sqlite3
from ConfigParser import SafeConfigParser


class SqlServer:

    def __init__(self, db):
        self.db_conn = sqlite3.connect(db)
        self.cursor = self.db_conn.cursor()

    def commit(self):
        self.db_conn.commit()

    def close(self):
        self.db_conn.close()

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


config = SafeConfigParser()
config.read('config.ini')

local_db = config.get('main', 'db')

handle = SqlServer(local_db)
