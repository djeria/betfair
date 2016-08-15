import sys
import time
import logging
from dataCollector import DataCollector

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

collector = DataCollector('1.126180340')

while True:
    try:
        collector.run()
        time.sleep(5)
    except RuntimeError, e:
        logging.exception("Runtime error")
        sys.exit()
    except Exception, e:
        logging.exception("Unexpected error")
