# ============================================
# bank_func.py – funkcije za rad sa računom
# --------------------------------------------
# - prikaz balansa
# - depozit i podizanje novca
# - istorija transakcija
# - snimanje transakcija u JSON baze
# ============================================

from datetime import datetime
from auth import load_data, save_data


# ------------------------------
# Prikazuje trenutni balans korisnika
# ------------------------------
def show_balance(user_data):
    print(f"\nYour balance is ${user_data['balance']:.2f}\n")


# ------------------------------
# Deposit – dodaje novac na račun
# i snima transakciju u JSON bazu
# ------------------------------
def deposit(username, user_data):
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Please enter a positive amount")
            return

        # Ažuriranje balansa u memoriji
        user_data["balance"] += amount

        # Dodavanje transakcije
        full_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_data["transactions"].append(
            f"[{full_time}] Deposit: ${amount:.2f}"
        )

        # Snimanje izmena u JSON bazu
        data = load_data()
        data["users"][username] = user_data
        save_data(data)

        print(f"${amount:.2f} deposited successfully!")

    except ValueError:
        print("Invalid input! Please enter a number.")


# ------------------------------
# Withdraw – skida novac sa računa
# i snima transakciju u JSON bazu
# ------------------------------
def withdraw(username, user_data):
    try:
        amount = float(input("Enter amount to withdraw: "))

        # Provere validnosti
        if amount <= 0:
            print("Please enter a positive amount")
            return

        if amount > user_data["balance"]:
            print("Insufficient funds")
            return

        # Ažuriranje balansa
        user_data["balance"] -= amount

        # Snimanje transakcije
        full_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_data["transactions"].append(
            f"[{full_time}] Withdraw: ${amount:.2f}"
        )

        # Čuvanje u JSON
        data = load_data()
        data["users"][username] = user_data
        save_data(data)

        print(f"${amount:.2f} withdrawn successfully!")

    except ValueError:
        print("Invalid input! Please enter a number.")


# ------------------------------
# Prikazuje istoriju transakcija korisnika
# ------------------------------
def show_transactions(user_data):
    print("\n===== Transaction History =====")

    if user_data["transactions"]:
        for t in user_data["transactions"]:
            print("-", t)
    else:
        print("No transactions yet.")

    print("==============================\n")
