import bs4 as bs
import requests


URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='


def get_rate(code: str, date: str = '') -> float:
    date = reversed(date.split('-'))
    date = '/'.join(str(x) for x in date)

    resp = requests.get(URL+date).text

    soup = bs.BeautifulSoup(resp, "xml")

    chars = soup.find_all('CharCode')
    rate_values = soup.find_all('VunitRate')

    chars = list(map(lambda x: x.text, chars))

    rate_values = list(map(lambda x: float(x.text.replace(',', '.')),
                           rate_values))

    for rate_currency in rate_values:
        if chars[rate_values.index(rate_currency)] == code:
            return rate_currency
