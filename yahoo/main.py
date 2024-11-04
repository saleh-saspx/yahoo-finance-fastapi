# from EnergyMarket import EnergyMarket
# from ForexMarket import ForexMarket
from CryptocurrencyMarket import CryptocurrencyMarket

# energy_market = EnergyMarket()
# print("energy_market :", energy_market.get_prices())

# forex_market = ForexMarket()
# print("ForexMarket :", forex_market.get_prices())

crypto_market = CryptocurrencyMarket()
print("crypto_market:", crypto_market.get_current_prices())