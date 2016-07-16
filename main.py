import sys
import time
import logging
from dataCollector import collector

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

collector.init('114565432')

while True:
    try:
        collector.run()
        time.sleep(10)
    except:
        e = sys.exc_info()[0]
        logging.ERROR(e)
