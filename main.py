from bank_func import show_balance, deposit, withdraw, add_transaction, show_transactions
from auth import login
from datetime import datetime

def main():
    if not login():
        return

    balance = 0
    is_running = True

    while is_running:
        print("\n===================")
        print("     PythonBank")
        print("===================")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("5. Transaction History")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            amount = deposit()
            if amount > 0:
                balance += amount
                add_transaction("Deposited", amount)
                time_only = datetime.now().strftime("%H:%M:%S")
                print(f"You deposited ${amount:.2f} at {time_only}")
            else:
                print("Deposit cancelled")

        elif choice == '3':
            amount = withdraw(balance)
            if amount > 0:
                balance -= amount
                add_transaction("Withdrew", amount)
                time_only = datetime.now().strftime("%H:%M:%S")
                print(f"You withdrew ${amount:.2f} at {time_only}")
            else:
                print("Withdrawal cancelled")

        elif choice == '4':
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == 'y':
                is_running = False

        elif choice == '5':
            show_transactions()

    print("Thank you! Have a nice day!")


if __name__ == "__main__":
    main()
