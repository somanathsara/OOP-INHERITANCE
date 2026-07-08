"""Currency convertor class - Handle conversion rates privately and perform conversions."""
class CurrencyConvert:
    def __init__(self):
        self.__from_currency = ""
        self.__to_currency = ""
        self.__exchange_rate = 0
    def set_data(self, fro, to, rate):
        self.__from_currency = fro
        self.__to_currency = to
        self.__exchange_rate = rate
    def convert(self, amount):
        total = amount * self.__exchange_rate
        print(f"Converted amount :{total}")
    def diplaydetails(self):
        print(f"From currency : {self.__from_currency}")
        print(f"To currency : {self.__to_currency}")
        print(f"Excahnge rate of currency : {self.__exchange_rate}")
p1 = CurrencyConvert()
p1.set_data("USD","INR",93)
p1.convert(8000)