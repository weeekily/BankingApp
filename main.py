# ============================================
# main.py – glavna kontrola aplikacije
# --------------------------------------------
# - pokreće login
# - prikazuje meni
# - poziva funkcije iz bank_func.py
# ============================================

from auth import login
from bank_func import show_balance, deposit, withdraw, show_transactions


# ------------------------------
# Glavni meni aplikacije
# ------------------------------
def main():
    # Login vraća username i podatke korisnika
    username, user_data = login()

    if username is None:
        return  # prekida program ako login ne uspe

    is_running = True

    # Petlja glavnog menija
    while is_running:
        print("\n===================")
        print("     PythonBank")
        print("===================")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Opcije menija:

        if choice == '1':
            show_balance(user_data)

        elif choice == '2':
            deposit(username, user_data)

        elif choice == '3':
            withdraw(username, user_data)

        elif choice == '4':
            show_transactions(user_data)

        elif choice == '5':
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == 'y':
                is_running = False

        else:
            print("Invalid choice, try again.")

    print("Thank you! Have a nice day!")


# Pokretanje aplikacije
if __name__ == "__main__":
    main()

