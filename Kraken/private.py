import krakenex
import pprint
import os

PATH = os.path.dirname(os.path.realpath(__file__))

k = krakenex.API()
k.load_key(PATH + '/kraken.key')


def getBalance():
    balance = k.query_private('Balance')
    balance = balance['result']

    return balance


def getOpenOrders():
    #prepare request
    req_data = {}

    #ger orders
    orders = k.query_private('OpenOrders', req_data)
    return orders['result']
    
    
def printOpenPositions():
    #prepare request
    req_data = {'docalcs': 'true'}

    #querry servers
    start = k.query_public('Time')
    open_positions = k.query_private('OpenPositions', req_data)
    end = k.query_public('Time')
    latency = end['result']['unixtime']-start['result']['unixtime']

    #parse result
    dict(open_positions)

    b = 0
    c = 0
    for i in open_positions['result']:
        order = open_positions['result'][i]
        if(order['pair']=='XETHZUSD'):
            b += (float(order['vol']))
        if (order['pair'] == 'XXBTZUSD'):
            c += (float(order['vol']))

    print('total open eth: ' + str(b))
    print('total open btc: ' + str(c))
    print('total open positions: ' + str(len(open_positions['result'])))
    
# price in 2nd currency
def market(pair, volume):
    
    amount = float(volume)
    
    if amount <= 0:
        tx = 'sell'
    else:
        tx = 'buy'
    
    #prepare request
    req_data = {
        'pair': pair,
        'type': tx,
        'ordertype': 'market',
        'volume': abs(amount),
        'oflags': 'viqc',
    }

    #submit order
    order = k.query_private('AddOrder', req_data)
    result = order['result']
    
    if order['error']:
        print('Error: ' + order['error'])
    else:
        print('Trade successful!')

    pprint.pprint(result)
