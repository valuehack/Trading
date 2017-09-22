from public import getHourAverage, getTicker
from private import market

# import socket
# socket.setdefaulttimeout(60000)

pair = 'XBTEUR'
hours = 10

av = getHourAverage(pair, hours)
current = float(getTicker(pair)[0])

dev = (av / current - 1)*100

print('Price against ' + str(hours) + ' hour average: ' + str(dev) + '%.')

if abs(dev >= 5):
    market(pair, dev*10)
else:
    print('Not buying under 5%.')
