import pyupbit

access = "amsKD2aTZurXzcG8eVYCcHgBdx8aijgrzB6XGL7B"          # 본인 값으로 변경
secret = "FeuIjVwUs0VkhAWlFkZMN3oqh3mMBFnPPDsPCYjl"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회