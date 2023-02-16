from datetime import date
import csv 

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