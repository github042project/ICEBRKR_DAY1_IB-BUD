# money.py — Currency-aware Decimal money type
# Module: IB Wallet (Pots) | Task: IBBUD-11

from decimal import Decimal, ROUND_HALF_UP

SUPPORTED_CURRENCIES = {"INR", "CHF"}


class Money:
    """
    Represents a monetary amount with its currency.
    Always Decimal internally — never float.
    Every amount carries a currency code.
    """

    def __init__(self, amount: Decimal | int | str, currency: str = "INR"):
        if currency not in SUPPORTED_CURRENCIES:
            raise ValueError(
                f"Unsupported currency '{currency}'. Allowed: {SUPPORTED_CURRENCIES}"
            )
        self.amount = Decimal(str(amount)).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount} {self.currency})"

    def __add__(self, other: "Money") -> "Money":
        self._check_same_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: "Money") -> "Money":
        self._check_same_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other: "Money") -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other: "Money") -> bool:
        self._check_same_currency(other)
        return self.amount < other.amount

    def __le__(self, other: "Money") -> bool:
        self._check_same_currency(other)
        return self.amount <= other.amount

    def is_positive(self) -> bool:
        return self.amount > Decimal("0")

    def is_zero(self) -> bool:
        return self.amount == Decimal("0")

    def _check_same_currency(self, other: "Money"):
        if self.currency != other.currency:
            raise ValueError(
                f"Currency mismatch: cannot operate on {self.currency} and {other.currency}"
            )

    def to_dict(self) -> dict:
        return {"amount": str(self.amount), "currency": self.currency}
