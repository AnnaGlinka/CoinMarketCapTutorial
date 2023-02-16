from requests import Session

class CoinMarketCapData:

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_all_coins_symbols(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        coin_list = []
        for coin in data:
            coin_list.append(coin['symbol'])
        return coin_list

    def get_coin_price(self, symbols):
        parameters = {'symbol': symbols}
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        r = self.session.get(url, params=parameters)
        #print(r.status_code)
        if r.status_code == 200:
            data = r.json()['data']
            return (data, r.status_code)
        else:
            return (None, r.status_code)
            

           
        