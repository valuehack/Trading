import krakenex

k = krakenex.API()

def getOHLC(pair, interval=60, since=None):
    #prepare request
    req_data = {
        'pair': pair,
        'interval': str(interval),
    #    'since': since
    }
    if since:
        req_data['since'] = since
    #get Data
    prices = k.query_public('OHLC', req_data)
    result = prices['result']
    
    return result

# hours = Anzahl der Stunden
def getHourAverage(pair, hours):
    
    time = k.query_public('Time')

    interval = time['result']['unixtime'] - hours * 3600

    #prepare request
    req_data = {
        'pair': pair,
        'interval': '60',
        'since': interval
    }

    #get Data
    prices = k.query_public('OHLC', req_data)
    result = prices['result']

    #get n hours average
    av = 0;
    n = 0;
    for price in next(iter(result.values())):
        av += float(price[1])
        n += 1
    av = av/n
    print('Average for ' + pair + ' in last ' + str(n) + ' hours: ' + str(av) + '.')
    return av
    

# pair = Kommagetrennte Liste der Paare (z.B. 'XBTEUR, ETHBTC')
def getTicker(pair):
    #prepare request
    req_data = {
        'pair': pair,
    }

    #get Data
    prices = k.query_public('Ticker', req_data)

    newprices = []

    for pair in prices['result']:
        # get price of last trade
        price = prices['result'][pair]['c'][0]
        newprices.append(price)
        print('Last trade price for ' + pair + ': ' + price)
    
    return newprices
