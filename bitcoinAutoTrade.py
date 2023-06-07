import time
import pyupbit

access = "access"
secret = "secret"

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
log = [0]
while True:
    try:
        krw = get_balance("KRW") * 0.6
        btc = get_balance("BTC")
        cur_btc_price = get_current_price("KRW-BTC")

        if krw > 5000 and cur_btc_price > log[0]:
            #upbit.buy_market_order("KRW-BTC", krw*0.9995)
            print("주문: ", krw*0.9995)
            log.append(btc - get_balance("BTC"))

        
        for i in range(len(log)):
            if log[i] < cur_btc_price * log[i]:
                if btc > 0.00008:
                    #upbit.sell_market_order("KRW-BTC", btc*0.9995)     
                    print("판매: ", btc*0.9995)
                    log.pop(i)

        log.sort()

        if len(log) > 10000:
            for i in range(1000):
                log.pop(0)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
