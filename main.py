from requests import Session
from pprint import pprint as pp
import os

API_KEY = os.getenv("API_KEY")




class CMC:
    #https://coinmarketcap.com/api/documentation/v1/

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def getPrice(self, symbol):
        parameters = {'symbol': symbol}
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data
        
        


cmc = CMC(API_KEY)
pp(cmc.getPrice('BTC'))
