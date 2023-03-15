import ccxt
import config
import time
import sys
from config import API_KEY, SECRET_KEY

SYMBOL = "BTC/USDT"
POSITION_SIZE = 0.01

# gridbot settings
NUM_BUY_GRID_LINES = 5
NUM_SELL_GRID_LINES = 5
GRID_SIZE = 2
CHECK_ORDERS_FREQUENCY = 1
CLOSED_ORDER_STATUS = "closed"

exchange = ccxt.bybit({
    'apiKey': config.API_KEY,
    'secret': config.SECRET_KEY
})

# activate Bybit testnet mode
exchange.set_sandbox_mode(True)

exchange.options['createMarketBuyOrderRequiresPrice'] = False

# check connection to Bybit in order to get ticker's data
ticker = exchange.fetch_ticker(SYMBOL)

buy_orders = []
sell_orders = []


for i in range(NUM_BUY_GRID_LINES):
    price = ticker['bid'] - (GRID_SIZE * (i + 1))
    print("submitting market limit buy order at {}".format(price))
    order = exchange.create_limit_buy_order(SYMBOL, POSITION_SIZE, price)
    buy_orders.append(order['info'])

for i in range(NUM_SELL_GRID_LINES):
    price = ticker['bid'] + (GRID_SIZE * (i + 1))
    print("submitting market limit sell order at {}".format(price))
    order = exchange.create_limit_sell_order(SYMBOL, POSITION_SIZE, price)
    sell_orders.append(order['info'])

while True:
    closed_order_ids = []

    for buy_order in buy_orders:
        print("checking for open buy orders {}".format(buy_order['orderId']))
        try:
            order = exchange.fetch_order(buy_order['orderId'])
        except Exception as e:
            print("request failed, retrying")
            continue

        order_info = order['info']

        if order_info['status'] == CLOSED_ORDER_STATUS:
            closed_order_ids.append(order_info['id'])
            print("buy order executed at {}".format(order_info['price']))
            new_sell_price = float(order_info['price'] + GRID_SIZE)
            print("creating new limit sell order at {}".format(new_sell_price))
            new_sell_order = exchange.create_limit_sell_order(
                SYMBOL, POSITION_SIZE, new_sell_price)
            sell_orders.append(new_sell_order)

        time.sleep(CHECK_ORDERS_FREQUENCY)

    for sell_order in sell_orders:
        print("checking sell order {}".format(sell_order['orderId']))
        try:
            order = exchange.fetch_order(sell_order['orderId'])
        except Exception as e:
            print("request failed, retrying")
            continue

        order_info = order['info']

        if order_info['status'] == CLOSED_ORDER_STATUS:
            closed_order_ids.append(order_info['id'])
            print("sell order executed at {}".format(order_info['price']))
            new_buy_price = float(order_info['price']) - GRID_SIZE
            print("creating new limit buy order at {}".format(new_buy_price))
            new_buy_order = exchange.create_limit_buy_order(
                SYMBOL, POSITION_SIZE, new_buy_price)
            buy_orders.append(new_buy_order)

        time.sleep(CHECK_ORDERS_FREQUENCY)

    for order_id in closed_order_ids:
        buy_orders = [
            buy_order for buy_order in buy_orders if buy_order['orderId'] != order_id]
        sell_orders = [
            sell_order for sell_order in sell_orders if sell_order['orderId'] != order_id]

    if len(sell_orders) == 0:
        sys.exit("stopping bot, nothing left to sell")
