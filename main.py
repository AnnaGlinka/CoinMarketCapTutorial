from requests import Session
from pprint import pprint as pp
import os
from datetime import date
import csv 

#https://coinmarketcap.com/api/documentation/v1


class CoinMarketCapData:

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoinsSymbols(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        coin_list = []
        for coin in data:
            coin_list.append(coin['symbol'])
        return coin_list

    def getPrice(self, symbolss):
        parameters = {'symbol': symbols}
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data


class ReportsBuilder():
    date = ""  
    def __init__(self):
        self.date = date.today()

        
    def create_report(self, data):
        #pp(data)
        with open(f'cryptocurrency {date.today()}.csv', 'w', encoding='UTF8') as f:
            self.writer = csv.writer(f)
            header = ['Symbol', 'Name', 'Currency', 'Price']
            print(header)
            self.writer.writerow(header)
            for symbol, value in data.items():
                data_record = []
                data_record.append(symbol)
                data_record.append(value['name'])
                for currency, value in value['quote'].items():
                    data_record.append(currency)
                    data_record.append(value['price'])
                print(data_record)
                self.writer.writerow(data_record)
    

cmc = CoinMarketCapData(os.getenv("API_KEY"))
#print(cmc.getAllCoinsSymbols())
#pp(cmc.getPrice('BTC', 'ETH'))
symbols_list = [
    'BTC', 'ETH', 'USDT', 'BNB', 'USDC', 'XRP', 'BUSD', 'ADA', 'DOGE', 'MATIC',
    'SOL', 'DOT'
]
symbols = ""
for symbol in symbols_list:
    symbols += symbol + ","

#pp(cmc.getPrice(symbols))

#print(cmc.getPrice(symbols))

rb = ReportsBuilder()
rb.create_report(cmc.getPrice(symbols))

