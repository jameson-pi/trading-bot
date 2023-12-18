#investopedia trading bot
from InvestopediaApi import ita
from password import password
client = ita.Account("piscitello284@gmail.com",password() )

status = client.get_portfolio_status()
print(status.account_val)
print(status.buying_power)
print(status.cash)
print(status.annual_return)