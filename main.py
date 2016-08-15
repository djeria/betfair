import sys
import time
import logging
from multiprocessing import Pool
from dataCollector import DataCollector

def collect_betfair_data(market_id):
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    collector = DataCollector(market_id)

    while True:
        try:
            collector.run()
            time.sleep(5)
        except RuntimeError, e:
            logging.exception("Runtime error")
            sys.exit()
        except Exception, e:
            logging.exception("Unexpected error")

if __name__ == "__main__":
    markets = [
        '1.125246985',
        '1.125800676',
    ]

    pool = Pool(4)
    pool.map(collect_betfair_data, markets)