from datetime import datetime

transactions = []

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print("Please enter a positive amount")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input! Please enter a number.")
        return 0

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Please enter a positive amount")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input! Please enter a number.")
        return 0

def add_transaction(transaction_type, amount):
    """Dodaje transakciju u listu sa datumom i vremenom."""
    full_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions.append(f"[{full_time}] {transaction_type}: ${amount:.2f}")

def show_transactions():
    """Prikazuje sve transakcije."""
    print("\n===== Transaction History =====")
    if transactions:
        for t in transactions:
            print("-", t)
    else:
        print("No transactions yet.")
