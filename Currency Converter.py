from forex_python.converter import CurrencyRates
import time

cr = CurrencyRates()
amount = int(input("Enter the amount you want to convert: "))
time.sleep(1)
from_currency = input("Enter the currency code to be converted: ").upper()
time.sleep(1)
to_currency = input("Enter the currency code to convert to: ").upper()
time.sleep(1)
print("Summary: You are converting", amount, from_currency, "to", to_currency)
time.sleep(2)
output = cr.convert(from_currency, to_currency, amount)
print("The converted rate is:", output)
