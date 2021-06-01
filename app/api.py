from datetime import date, timedelta
from pprint import pprint

import requests


def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    url = f"http://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={','.join(currencies)}"
    # url = f"https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}&symbols={','.join(currencies)}"

    print(url)
    r = requests.get(url)

    if not r and not r.json():
        return False, False
    api_rate = r.json().get("rates")
    pprint(api_rate)
    all_days = sorted(api_rate.keys())
    all_rates = {currency: [] for currency in currencies}

    # print(all_rates)
    # print(all_rates)
    # pprint(api_rate.keys())
    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rate[each_day].items()]

    return all_days, all_rates


if __name__ == '__main__':
    pprint(get_rates(currencies=["USD", "CAD"]))
