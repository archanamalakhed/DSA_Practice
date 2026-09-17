class CreditCardPayment:
    def __init__(self, card_number, holder_name, card_limit, balance=0.0):
        self.card_number = card_number
        self.holder_name = holder_name
        self.card_limit = card_limit
        self.balance = balance

    def pay(self, amount):
        fee = amount * 0.025
        total_charge = amount + fee

        if self.balance + total_charge <= self.card_limit:
            self.balance += total_charge
            print(
                f"CreditCard Success: Charged ${amount:.2f} + ${fee:.2f} fee. "
                f"Remaining Limit: ${self.card_limit - self.balance:.2f}"
            )
            return True
        else:
            print(
                f"CreditCard Rejected: Total charge ${total_charge:.2f} exceeds "
                f"available limit (${self.card_limit - self.balance:.2f})."
            )
            return False


class UPIPayment:
    def __init__(self, upi_id, daily_limit=100000.0, spent_today=0.0, linked_pin="1234"):
        self.upi_id = upi_id
        self.daily_limit = daily_limit
        self.spent_today = spent_today
        self.linked_pin = linked_pin

    def pay(self, amount, entered_pin=None):
        if "@" not in self.upi_id:
            print(f"UPI Rejected: Invalid UPI ID '{self.upi_id}'.")
            return False

        if self.spent_today + amount > self.daily_limit:
            print(
                f"UPI Rejected: Amount ${amount:.2f} exceeds remaining daily limit "
                f"(${self.daily_limit - self.spent_today:.2f})."
            )
            return False

        if entered_pin != self.linked_pin:
            print("UPI Rejected: Invalid PIN.")
            return False

        self.spent_today += amount
        print(
            f"UPI Success: Transferred ${amount:.2f}. "
            f"Daily Spent: ${self.spent_today:.2f}/{self.daily_limit:.2f}"
        )
        return True


class PaymentProcessor:
    def process_transaction(self, payment_method, amount, **kwargs):
        # Polymorphic call: relies on duck typing to execute .pay()
        return payment_method.pay(amount, **kwargs)


# Demonstration
processor = PaymentProcessor()

cc = CreditCardPayment("4111-2222-3333-4444", "John Doe", card_limit=5000.0)
upi = UPIPayment("john@upi", daily_limit=25000.0, linked_pin="4321")

# Credit card tests
processor.process_transaction(cc, 1000.0)
processor.process_transaction(cc, 4500.0)  # Exceeds limit

# UPI tests
processor.process_transaction(upi, 5000.0, entered_pin="4321")
processor.process_transaction(upi, 2000.0, entered_pin="0000")  # Wrong PIN