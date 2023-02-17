from coin_market_cap_data import CoinMarketCapData
from requests import Session
import os

API_KEY = os.getenv("API_KEY")
incorrect_api_key = "kdks"

def test_api_endpoint():
    apiurl = 'https://pro-api.coinmarketcap.com'
    apiurl_map = apiurl + '/v1/cryptocurrency/map'
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    session = Session()
    session.headers.update(headers)
    r = session.get(apiurl_map)
    assert r.status_code == 200

def test_get_coin_prices_unauthorized():
    cmc = CoinMarketCapData(incorrect_api_key)
    assert cmc.get_coin_price("ETH") == (None, 401)




