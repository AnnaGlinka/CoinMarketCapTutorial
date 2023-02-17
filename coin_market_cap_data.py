from requests import Session

class CoinMarketCapData:

    def __init__(self, token):
        self._apiurl = 'https://pro-api.coinmarketcap.com'
        self._headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }
        self._session = Session()
        self._session.headers.update(self._headers)

    def get_all_coins_symbols(self):
        _url = self._apiurl + '/v1/cryptocurrency/map'
        _r = self._session.get(_url)
        _data = _r.json()['data']
        _coin_list = []
        for _coin in _data:
            _coin_list.append(_coin['symbol'])
        return _coin_list

    def get_coin_price(self, symbols):
        _parameters = {'symbol': symbols}
        _url = self._apiurl + '/v1/cryptocurrency/quotes/latest'
        _r = self._session.get(_url, params=_parameters)
        #print(r.status_code)
        if _r.status_code == 200:
            _data = _r.json()['data']
            return (_data, _r.status_code)
        else:
            return (None, _r.status_code)
            

           
        