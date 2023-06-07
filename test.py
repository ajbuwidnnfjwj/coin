import pyupbit

access = "amsKD2aTZurXzcG8eVYCcHgBdx8aijgrzB6XGL7B"          # 본인 값으로 변경
secret = "FeuIjVwUs0VkhAWlFkZMN3oqh3mMBFnPPDsPCYjl"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

df = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=2)
target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.5

cur_price = pyupbit.get_orderbook(ticker="KRW-BTC")["orderbook_units"][0]["ask_price"]

print("보유 코인: ",upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print("보유 현금: ", upbit.get_balance("KRW"))         # 보유 현금 조회
print("target price: ", target_price)
print("current price: ", cur_price)