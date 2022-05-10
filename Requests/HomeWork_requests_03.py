from pprint import pprint
import requests
import datetime
import time

URL = 'https://api.stackexchange.com'


if __name__ == '__main__':
    # Запрос через сформированный на сайте конфигруратор (дата today и from выставлялись в конфигураторе заранее)
    # response = requests.get(
        # f'{URL}/2.3/questions?fromdate=1651968000&todate=1652140800&order=desc&sort=activity&tagged=Python&site=stackoverflow')
    # pprint(response.json())

    # Запрос через автоматическое указание даты сегодняшней и from (за два дня)
    # - тут не могу быть уверен, что правильно перевёл в UNIX формат дату
    datetime_today = time.mktime(datetime.date.today().timetuple())
    datetime_from = time.mktime(datetime.date(2022,5,8).timetuple())
    print(datetime_today)
    print(datetime_from)
    response = requests.get(f'{URL}/2.3/questions?fromdate={datetime_from:.0f}&todate={datetime_today:.0f}&order=desc&sort=activity&tagged=Python&site=stackoverflow')
    pprint(response.json())