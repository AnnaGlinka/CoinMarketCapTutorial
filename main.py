from pprint import pprint as pp
import os
from coin_market_cap_data import CoinMarketCapData
from reports_builder import ReportsBuilder

#https://coinmarketcap.com/api/documentation/v1


cmc = CoinMarketCapData(os.getenv("API_KEY"))
print(cmc.get_all_coins_symbols())
#pp(cmc.getPrice('BTC', 'ETH'))
symbols_list = [
    'BTC', 'ETH', 'USDT', 'BNB', 'USDC', 'XRP', 'BUSD', 'ADA', 'DOGE', 'MATIC',
    'SOL', 'DOT'
]
symbols = ""
for symbol in symbols_list:
    symbols += symbol + ","

#pp(cmc.getPrice(symbols))


rb = ReportsBuilder()
print("All cryptocurrency available in the API:")
response_data = cmc.get_coin_price(symbols)
print("-------------------------------------------------------------------------")
coin_data = response_data[0]
response_status_code = response_data[1]

if response_status_code == 200:
    rb.create_report(coin_data)

else:
    match response_status_code:
        case 400:
            print("Bad request")
        case 401:
            print("Unauthorized")
        case 403:
            print("Forbidded")
        case 404:
            print("Not found")
        case 429:
            print("To Many Requests")
        case 500:
            print("Internal Server Error")
    
    




