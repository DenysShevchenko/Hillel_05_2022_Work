from abc import ABC, abstractclassmethod


class User:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age


class PaymentSystem(ABC):
    @abstractclassmethod
    def authorize(self, user: User):
        pass

    @abstractclassmethod
    def checkout(self):
        pass


class PayPal(PaymentSystem):
    BASE_URL = "paypal.com"

    def authorize(self, user: User):
        # token = self.get_access_token()
        # self.send_callback_api(token)
        print("Authorize with PayPal")

    def checkout(self):
        print("Checkout with PayPal")


class Stripe(PaymentSystem):
    BASE_URL = "stripe.com"

    def authorize(self, user: User):
        # self._authorize(self.BASE_URL, user)
        print(f"Authorize with Stripe. {user}")

    def checkout(self):
        print("Checkout with Stripe")


class PaymentProcessor:
    def __init__(self, payment_system: PaymentSystem, user: User) -> None:
        self._payment_system = payment_system
        self._payment_system.authorize(user)

    def checkout(self):
        self._payment_system.checkout()


def quick_order(payment_processor: PaymentProcessor):
    payment_processor.checkout()


def shopping(payment_processor: PaymentProcessor):
    payment_processor.checkout()


def main():
    user = User(name="John", surname="Doe", age="20")
    paypal = PayPal()  # noqa: F841
    stripe = Stripe()

    # if payment_system == "paypal":
    #     paypal.authorize()
    #     paypal.checkout()
    # elif payment_system == "stripe":
    #     stripe.authorize()
    #     stripe.checkout()

    payment_processor = PaymentProcessor(stripe, user)

    shopping(payment_processor)
    quick_order(payment_processor)


if __name__ == "__main__":
    main()


class BaseUnit:
    pass


class Unit(BaseUnit):
    pass


class BaseAttackProcess(ABC):
    pass


class AttackProcess(BaseAttackProcess):
    def __init__(self, unit: Unit) -> None:
        self._unit = unit


class Protection:
    def __init__(self):
        self.config = ""


class Damage:
    def __init__(self):
        self.config = ""


class DamageProcessor:
    def __init__(
        self, attac: Unit, protec: Unit, protection: Protection, damage: Damage
    ):
        self.attac: Unit = attac
        self.protec: Unit = protec
        self.protection = protection
        self.damage = protection

    def calculate(self):
        print("...")


class HealthProcessor:
    def __init__(self, unit, reduce_protocol) -> None:
        self.unit = unit
        self.reduce_protocol = reduce_protocol

    def reduce_health(self):
        self.reduce_protocol.calculate()
