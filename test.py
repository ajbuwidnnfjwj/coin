import pyupbit

access = "access"          # 본인 값으로 변경
secret = "secret"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

df = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=2)
target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.5

cur_price = pyupbit.get_orderbook(ticker="KRW-BTC")["orderbook_units"][0]["ask_price"]

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print("target price: ", target_price)
print("current price: ", cur_price)
