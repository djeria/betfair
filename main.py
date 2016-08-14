import sys
import time
import logging
from dataCollector import DataCollector

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

collector = DataCollector('1.125246976')

while True:
    try:
        collector.run()
        time.sleep(5)
    except RuntimeError, e:
        print "Runtime error: " + str(e)
        sys.exit()
    except Exception, e:
        print "Unexpected error: " + str(e)
