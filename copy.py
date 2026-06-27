from __future__ import annotations
from abc import ABC, abstractmethod
from tkinter import Tk, Frame, Label, Entry, Button, StringVar
import os

# File names for account storage and transaction logging
DATA_FILE = "accounts.txt"
LOG_FILE = "transactions.txt"

# In-memory account dictionary and the currently logged-in account
accounts = {}
current_account = None

# Base class for bank accounts. This uses abstraction for shared behavior.
class BankAccount(ABC):
    def __init__(self, username: str, pin: str, balance: float) -> None:
        self._username = username
        self._pin = pin
        self._balance = balance

    @property
    def username(self) -> str:
        return self._username

    @property
    def balance(self) -> float:
        return self._balance

    def check_pin(self, pin: str) -> bool:
        return self._pin == pin

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    @abstractmethod
    def account_type(self) -> str:
        ...

    @abstractmethod
    def calculate_interest(self) -> float:
        ...

# Checking account class with its own account type and interest rate
class CheckingAccount(BankAccount):
    def account_type(self) -> str:
        return "Checking"

    def calculate_interest(self) -> float:
        return self.balance * 0.001
    
class SavingsAccount(BankAccount):
    def account_type(self) -> str:
        return "Savings"

    def calculate_interest(self) -> float:
        return self.balance * 0.005

# Map text labels to account classes for loading from file
ACCOUNT_TYPES = {"checking": CheckingAccount, "savings": SavingsAccount}

# Load accounts from the text file into the accounts dictionary
def load_accounts():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("Ralph,1509,1200000.00,savings\nAfobz,1509,14.00,checking\nEkenna,1509,1230.00,savings\n")
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding = "utf-8") as f:
            f.write("Zain Bank Transaction Log\n")
    accounts.clear()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                username, pin, balance, kind = [field.strip() for field in line.strip().split(",")]
                accounts[username] = ACCOUNT_TYPES[kind.lower()](username, pin, float(balance))
            except Exception:
                continue


# Save all account data back to the accounts file
def save_accounts() -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for account in accounts.values():
            f.write(f"{account.username},{account._pin},{account.balance:.2f},{account.account_type().lower()}\n")

# Log each transaction to a text file
def log_transaction(action: str, amount: float, account: BankAccount) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{account.username},{account.account_type()},{action},{amount:.2f},{account.balance:.2f}\n")  

# Check username and PIN against loaded accounts
def validate_login(username: str, pin: str):
    account = accounts.get(username)
    return account if account and account.check_pin(pin) else None

# GUI class that builds the ATM interface and handles button actions
class ATMGui:
     def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Zain Bank ATM")
        self.root.geometry("380x280")
        self.username = StringVar()
        self.pin = StringVar()
        self.amount = StringVar()
        self.balance = StringVar()
        self.status = StringVar()
        self.main = Frame(root)
        self.main.pack(padx=10, pady=10, fill="both", expand=True)
        self.show_login()

     def clear(self) -> None:
        # Remove all widgets from the current frame before drawing a new screen
        for widget in self.main.winfo_children():
            widget.destroy()

     def show_login(self) -> None:
        # Show the login screen with username and PIN fields
        self.clear()
        Label(self.main, text="Zain Bank Login", font=("Arial", 16)).pack(pady=10)
        Label(self.main, text="Username:").pack(anchor="w")
        Entry(self.main, textvariable=self.username).pack(fill="x")
        Label(self.main, text="PIN:").pack(anchor="w")
        Entry(self.main, textvariable=self.pin, show="*").pack(fill="x")
        Button(self.main, text="Login", command=self.login).pack(pady=10)
        Label(self.main, textvariable=self.status, fg="red").pack(pady=5)

     def show_dashboard(self) -> None:
        # Show the account dashboard with balance and action buttons
        self.clear()
        Label(self.main, text="Zain Bank Dashboard", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        Label(self.main, text="Balance:").grid(row=1, column=0, sticky="e")
        Label(self.main, textvariable=self.balance).grid(row=1, column=1, sticky="w")
        Label(self.main, text="Amount:").grid(row=2, column=0, sticky="e")
        Entry(self.main, textvariable=self.amount).grid(row=2, column=1)
        Button(self.main, text="Deposit", width=12, command=lambda: self.action("deposit")).grid(row=3, column=0, pady=5)
        Button(self.main, text="Withdraw", width=12, command=lambda: self.action("withdraw")).grid(row=3, column=1, pady=5)
        Button(self.main, text="Interest", width=12, command=self.add_interest).grid(row=4, column=0, pady=5)
        Button(self.main, text="Logout", width=12, command=self.logout).grid(row=4, column=1, pady=5)
        Label(self.main, textvariable=self.status, fg="blue").grid(row=5, column=0, columnspan=2, pady=10)

     def login(self) -> None:
        # Process login and switch to dashboard on success
        global current_account
        user = self.username.get().strip()
        pin = self.pin.get().strip()
        if not user or not pin:
            self.status.set("Input username and PIN")
            return
        account = validate_login(user, pin)
        if not account:
            self.status.set("Seniorman invalid username or PIN")
            return
        current_account = account
        self.balance.set(f"${account.balance:.2f}")
        self.amount.set("")
        self.status.set("")
        self.show_dashboard()

     def logout(self) -> None:
        # Save changes and return to the login screen
        global current_account
        if current_account:
            save_accounts()
        current_account = None
        self.username.set("")
        self.pin.set("")
        self.status.set("Logged out, don't forget you card Seniorman")
        self.show_login()
   
     def action(self, kind: str) -> None:
        # Handle deposit or withdraw actions from the dashboard
        if not current_account:
            return
        try:
            amount = float(self.amount.get())
        except ValueError:
            self.status.set("Enter valid amount")
            return
        if amount <= 0:
            self.status.set("Amount must be positive")
            return
        ok = current_account.deposit(amount) if kind == "deposit" else current_account.withdraw(amount)
        if not ok:
            self.status.set("Insufficient funds, go and hustle some more Seniorman")
            return
        log_transaction(kind, amount, current_account)
        self.balance.set(f"${current_account.balance:.2f}")
        self.status.set(f"{kind.title()} ${amount:.2f}")
        self.amount.set("")
        save_accounts()

     def add_interest(self) -> None:
        # Calculate and add interest to the account balance
        if not current_account:
            return
        amount = current_account.calculate_interest()
        if amount <= 0:
            self.status.set("No interest")
            return
        current_account.deposit(amount)
        log_transaction("interest", amount, current_account)
        self.balance.set(f"${current_account.balance:.2f}")
        self.status.set(f"Interest ${amount:.2f}")
        save_accounts()

# Entry point for the application
def main() -> None:
    load_accounts()
    root = Tk()
    ATMGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()

          
    
