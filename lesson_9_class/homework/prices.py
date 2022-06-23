from random import choice

exchange_rates = [
    {"from": "UAH", "to": "USD", "value": 0.02777778},
    {"from": "USD", "to": "UAH", "value": 36},
]

list_currency = ["UAH", "USD"]


def get_exhange_rate(currency_a: str, currency_b: str):
    pass


class Price:
    def __init__(self, amount: int, currency: str, name: str):
        self.amount: int = amount
        if currency == "":
            currency = self.select_currency()
        self.currency: str = currency
        self.name_price = name
        # print('class currency: '+self.currency)
        self.print_class()

    def __str__(self):
        return f"price ({self.amount}, {self.currency})"

    def __add__(self, other: "Price"):
        instance = Price.add_amount(self, other, name_c="ADD", znak=1)
        return instance

    def __sub__(self, other: "Price"):
        instance = Price.add_amount(self, other, name_c="SUB", znak=-1)
        return instance

    @classmethod
    def select_currency(cls):
        return choice(list_currency)

    def print_class(cls):
        print(cls.name_price + ": " + str(cls))

    def add_amount(self, other: "Price", name_c: str, znak: int):
        currency_A = self.currency
        currency_B = other.currency
        amount_A = self.amount
        amount_B = other.amount

        if currency_A != currency_B:

            # basic_cur = currency_A
            # double conversion only for currency A,
            # because the value of currency B is reduced to currency A
            kurs = self.exchange_rate(currency_A, currency_B)
            amount_A_m1 = amount_A * kurs
            amount_A = amount_A_m1 * self.exchange_rate(currency_B, currency_A)
            amount_B = amount_B * self.exchange_rate(currency_B, currency_A)

        amount_ADD = int(amount_A) + int((znak * amount_B))

        return Price(amount=amount_ADD, currency=currency_A, name=name_c)

    def exchange_rate(self, cer_from, cer_to):
        for exc_cer in exchange_rates:
            if exc_cer.get("from") == cer_from and exc_cer.get("to") == cer_to:
                return exc_cer.get("value")

        return 0


price_a = Price(300, "", "A")
price_b = Price(50, "", "B")
price_add = price_a + price_b
price_sub = price_a - price_b
