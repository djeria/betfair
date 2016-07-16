from dataCollector import DataCollector
import dbWriter
import dbReader
import requests
import json

# collector = DataCollector('1.125604886')
# collector.run();

#
# market = collector.get_market();
#
# for runner in market['runners']:
#     quote = collector.get_quote(runner)
#
#     print quote['runnerId'] + ': ' + str(quote['bestBacks'][0]['price'])

# dbWriter.handle.drop_table('quotes')
# dbWriter.handle.create_quotes_table()
# dbWriter.handle.clear_quotes_table()

# print dbReader.handle.get_quotes_table('1.125604886', 'The Draw')

# url = 'http://uk-api.betfair.com/www/sports/exchange/readonly/v1.0/bymarket'
# params = {
#     'alt': 'json',
#     'currencyCode': 'USD',
#     'types': 'MARKET_STATE,RUNNER_STATE,RUNNER_EXCHANGE_PRICES_BEST,RUNNER_DESCRIPTION',
#     'marketIds': '1.125488354'
# }
#
# resp = requests.get(url, params=params)
#
# if resp.ok:
#             market = resp.text.replace('while(1) {};\n', '')
#             market = json.loads(market)
#             market = market['eventTypes'][0]['eventNodes'][0]['marketNodes'][0]
#
#             for runner in market['runners']:
#                 print runner


