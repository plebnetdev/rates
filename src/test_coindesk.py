from app import coindesk_btc_fiat

if __name__ == "__main__":

    asian_list = ['HKD', 'CNY', 'SGD', 'AUD', 'TWD', 'THB', 'KRW', 'JPY']
    g7currencies = ['HKD', 'CNY', 'SGD', 'GBP', 'EUR', 'AUD', 'JPY']

    for coin in asian_list:
       symbol = f'BTC-{coin}'
       time, rate = coindesk_btc_fiat(symbol)
       arate = "%.2f" % rate
       print(arate)
       print(f'BTC-{coin}: {"%.2f" % rate}')


'''
{"time":{"updated":"Mar 10, 2021 00:54:00 UTC","updatedISO":"2021-03-10T00:54:00+00:00","updateduk":"Mar 10, 2021 at 00:54 GMT"},
 "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
 "chartName":"Bitcoin",
 "bpi":{"USD":{"code":"USD",
               "symbol":"&#36;",
               "rate":"55,618.4738",
               "description":"United States Dollar",
               "rate_float":55618.4738},
        "GBP":{"code":"GBP","symbol":"&pound;",
               "rate":"40,049.6950",
               "description":"British Pound Sterling",
               "rate_float":40049.695},
        "EUR":{"code":"EUR","symbol":"&euro;",
               "rate":"46,749.9413",
               "description":"Euro",
               "rate_float":46749.9413}}}
               
'''
