import krakenex
import pprint
from private import getBalance, getOpenOrders

balance = getBalance()
orders = getOpenOrders()

print(str(len(orders['open'])) + ' open orders.')
pprint.pprint(balance)
