from collections import defaultdict
from datetime import datetime

class BankUI:
    def __init__(self):
        # {user: {currency: balance}}
        self.accounts = defaultdict(lambda: defaultdict(int))
        self.history = []  # store all transactions as text

    # ---------------------------
    # USER MANAGEMENT
    # ---------------------------
    def add_user(self, name):
        """Add a new user with empty accounts."""
        if name in self.accounts:
            msg = f"⚠ User '{name}' already exists."
        else:
            self.accounts[name]  # initialize
            msg = f"✅ User '{name}' added successfully."

        self._log(msg)
        return msg

    def remove_user(self, name):
        """Remove an existing user."""
        if name not in self.accounts:
            msg = f"❌ User '{name}' not found."
        else:
            del self.accounts[name]
            msg = f"✅ User '{name}' removed successfully."

        self._log(msg)
        return msg

    # ---------------------------
    # DEPOSIT / WITHDRAW
    # ---------------------------
    def deposit(self, name, amount, currency):
        """Deposit money into a user's account."""
        if name not in self.accounts:
            msg = f"❌ User '{name}' not found."
        elif not currency:
            msg = "⚠ Please specify a currency."
        elif amount <= 0:
            msg = "⚠ Deposit amount must be positive."
        else:
            self.accounts[name][currency] += amount
            new_balance = self.accounts[name][currency]
            msg = f"💰 Deposited {amount} {currency} to '{name}'. New balance: {new_balance} {currency}"

        self._log(msg)
        return msg

    def withdraw(self, name, amount, currency):
        """Withdraw money from a user's account."""
        if name not in self.accounts:
            msg = f"❌ User '{name}' not found."
        elif not currency:
            msg = "⚠ Please specify a currency."
        elif amount <= 0:
            msg = "⚠ Withdrawal amount must be positive."
        elif self.accounts[name][currency] < amount:
            msg = f"❌ '{name}' has only {self.accounts[name][currency]} {currency}, insufficient balance."
        else:
            self.accounts[name][currency] -= amount
            new_balance = self.accounts[name][currency]
            msg = f"🏧 Withdrew {amount} {currency} from '{name}'. New balance: {new_balance} {currency}"

        self._log(msg)
        return msg

    # ---------------------------
    # TRANSFER
    # ---------------------------
    def transfer(self, from_name, to_name, amount, currency):
        """Transfer money between two users."""
        if from_name not in self.accounts:
            msg = f"❌ Sender '{from_name}' not found."
        elif to_name not in self.accounts:
            msg = f"❌ Receiver '{to_name}' not found."
        elif not currency:
            msg = "⚠ Please specify a currency."
        elif amount <= 0:
            msg = "⚠ Transfer amount must be positive."
        elif self.accounts[from_name][currency] < amount:
            msg = f"❌ '{from_name}' has only {self.accounts[from_name][currency]} {currency}."
        else:
            # Perform transfer
            self.accounts[from_name][currency] -= amount
            self.accounts[to_name][currency] += amount
            msg = (f"💸 '{from_name}' transferred {amount} {currency} to '{to_name}'.\n"
                   f"'{from_name}' new balance: {self.accounts[from_name][currency]} {currency}")

        self._log(msg)
        return msg

    # ---------------------------
    # SHOW INFO
    # ---------------------------
    def get_balance(self, name):
        """Return formatted balance for one user."""
        if name not in self.accounts:
            return f"❌ User '{name}' not found."
        balances = self.accounts[name]
        result = f"💼 Balances for '{name}':\n"
        for curr, amt in balances.items():
            result += f"   • {curr}: {amt}\n"
        return result.strip()

    def show_all_accounts(self):
        """Return a formatted list of all users and balances."""
        if not self.accounts:
            return "📭 No accounts available."

        result = "🏦 All Accounts:\n"
        for name, currencies in self.accounts.items():
            result += f"👤 {name}:\n"
            for curr, amt in currencies.items():
                result += f"   • {curr}: {amt}\n"
        return result.strip()

    def show_history(self):
        """Return all logged actions."""
        if not self.history:
            return "🕒 No transactions yet."
        return "📜 Transaction History:\n" + "\n".join(self.history)

    # ---------------------------
    # INTERNAL HELPERS
    # ---------------------------
    def _log(self, message):
        """Record message with timestamp."""
        time = datetime.now().strftime("%H:%M:%S")
        self.history.append(f'{time} {message}')
            