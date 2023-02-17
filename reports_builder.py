from datetime import date
import csv 

class ReportsBuilder():
    def __init__(self):
        self._date = date.today()

        
    def create_report(self, data):
        #pp(data)
        with open(f'cryptocurrency {date.today()}.csv', 'w', encoding='UTF8') as f:
            self._writer = csv.writer(f)
            _header = ['Symbol', 'Name', 'Currency', 'Price']
            print(_header)
            self._writer.writerow(_header)
            for _symbol, _value in data.items():
                _data_record = []
                _data_record.append(_symbol)
                _data_record.append(_value['name'])
                for currency, value in _value['quote'].items():
                    _data_record.append(currency)
                    _data_record.append(value['price'])
                print(_data_record)
                self._writer.writerow(_data_record)