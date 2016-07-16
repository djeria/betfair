import requests
import json
import datetime
import dbWriter


class DataCollector:

    def __init__(self, market_id):
        self.db = dbWriter.handle
        self.url = 'http://uk-api.betfair.com/www/sports/exchange/readonly/v1.0/bymarket'
        self.market_id = market_id

    def get_market(self):
        params = {
            'alt': 'json',
            'currencyCode': 'USD',
            'types': 'MARKET_STATE,RUNNER_STATE,RUNNER_EXCHANGE_PRICES_BEST,RUNNER_DESCRIPTION',
            'marketIds': self.market_id
        }

        resp = requests.get(self.url, params=params)

        if resp.ok:
            market = resp.text.replace('while(1) {};\n', '')
            market = json.loads(market)
            market = market['eventTypes'][0]['eventNodes'][0]['marketNodes'][0]

            return market

        else:
            raise Exception('Received invalid response status code %s' % resp.status_code)

    @staticmethod
    def get_quote(runner):
        quote = {
            'runnerId': runner['description']['runnerName'],
            'bestBacks': runner['exchange']['availableToBack'],
            'bestLays': runner['exchange']['availableToLay'],
        }

        return quote

    def save_market(self, market):
        for runner in market['runners']:
            quote = self.get_quote(runner)

            self.db.insert_quote(
                self.market_id,
                quote['runnerId'],
                quote['bestBacks'][0]['price'],
                quote['bestBacks'][0]['size'],
                quote['bestLays'][0]['price'],
                quote['bestLays'][0]['size'],
                datetime.datetime.now()
            )