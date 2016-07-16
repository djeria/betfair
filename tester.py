from dataCollector import DataCollector
import dbWriter
import dbReader
import requests
import json

collector = DataCollector('1.125604886')

market = collector.get_market();

for runner in market['runners']:
    quote = collector.get_quote(runner)

    print quote


# dbWriter.handle.drop_table('markets')
# dbWriter.handle.create_markets_table()
#
# dbWriter.handle.drop_table('runners')
# dbWriter.handle.create_runners_table()

# time, back, lay = dbReader.handle.get_quotes(114549309, 67779631)

# print dbReader.handle.get_runners_table(103163147)

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


