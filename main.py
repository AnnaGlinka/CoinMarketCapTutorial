import requests
from requests import Session

import os

API_KEY = os.getenv("API_KEY")

#https://coinmarketcap.com/api/documentation/v1/

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

#r = requests.get(url, headers=headers)


class CMC:

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY,
        }
        self.session = Session()
        self.session.headers.update(headers=headers)


cmc = CMC(API_KEY)
