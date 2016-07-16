import sys
import time
import logging
from dataCollector import DataCollector

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

collector = DataCollector('1.125604886')

while True:
    try:
        collector.run()
        time.sleep(10)
    except:
        e = sys.exc_info()[0]
        logging.ERROR(e)
