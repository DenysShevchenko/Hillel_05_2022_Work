exchange_rates = [
    {"from": "UAH", "to": "USD", "value": 0.02777778},
    {"from": "USD", "to": "UAH", "value": 36},
]

list_currency = ["UAH", "USD"]


def get_exhange_rate(currency_a: str, currency_b: str) -> float:
    pass


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency


price_a = Price(20000, "AUD")
price_b = Price(30000, "EUR")

"""
price_a = 20000, UAH
middle_a_price  = price_a * exchange_rate(USD)
middle_b_price  = price_b * exchange_rate(USD)
total = Price(x, "USD")
price_a = 20000, UAH
middle_b_price_1  = price_b * exchange_rate(USD)
middle_b_price_2  = middle_b_price_1 * exchange_rate(UAH)
total = Price(x, "UAH")
***
price_a = 20000, UAH
value = 15000
total = Price(35000, "UAH")
price_a * 1.1
"""

total = price_a + price_b


print(total)
