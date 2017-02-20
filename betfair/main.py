import logging
import sys
import time
import multiprocessing

from betfair.dataCollector import DataCollector


def collect_betfair_data(market_id):
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    collector = DataCollector(market_id)

    while True:
        try:
            collector.run()
            time.sleep(5)
        except RuntimeError as e:
            logging.exception("Runtime error")
            sys.exit()
        except Exception as e:
            logging.exception("Unexpected error")

if __name__ == "__main__":
    markets = [
        '1.129426476',
        '1.129639772',
    ]

    pool = multiprocessing.Pool(2)
    pool.map(collect_betfair_data, markets)