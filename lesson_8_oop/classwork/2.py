class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if ExchangeRates._initialized is False:
            return
        self.message = "Hello from test"
        self.exchange_rates = []  # takes 10s

        ExchangeRates._initialized = True


er = ExchangeRates()
er = ExchangeRates()
er = ExchangeRates()
