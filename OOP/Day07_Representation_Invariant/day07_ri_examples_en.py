# day07_ri_examples_en.py
# Super-simple examples of Representation Invariant (RI).

class Interval:
    """RI: always ensure start <= end."""
    def __init__(self, start: float, end: float):
        # Validate input so we never enter an invalid state
        if start > end:
            raise ValueError("start must be <= end")
        self._start = start
        self._end = end
        self._check_rep()

    def length(self) -> float:
        """Length = end - start (>= 0 if the RI holds)."""
        return self._end - self._start

    def move(self, delta: float) -> None:
        """Translate the interval by delta. After changing state, check RI."""
        self._start += delta
        self._end += delta
        self._check_rep()

    def _check_rep(self) -> None:
        """Enforce RI: start <= end must always hold."""
        assert self._start <= self._end, "RI violated: start <= end"


class BankAccount:
    """RI: balance >= 0 (no negative balances)."""
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("initial balance must be >= 0")
        self._owner = owner
        self._balance = float(balance)
        self._check_rep()

    def deposit(self, amount: float) -> None:
        """Deposit must be positive; check RI after update."""
        if amount <= 0:
            raise ValueError("deposit must be > 0")
        self._balance += amount
        self._check_rep()

    def withdraw(self, amount: float) -> None:
        """Withdraw must be positive and not exceed balance; check RI after update."""
        if amount <= 0:
            raise ValueError("withdraw must be > 0")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        self._check_rep()

    def balance(self) -> float:
        """Current balance (does not change state)."""
        return self._balance

    def _check_rep(self) -> None:
        """Enforce RI: balance is always >= 0."""
        assert self._balance >= 0, "RI violated: balance >= 0"


def _demo():
    print("== Demo Interval ==")
    iv = Interval(0, 10)
    print("length:", iv.length())   # 10
    iv.move(5)
    print("length after move:", iv.length())  # 10

    print("\n== Demo BankAccount ==")
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    acc.withdraw(70)
    print("balance:", acc.balance())  # 80

if __name__ == "__main__":
    _demo()