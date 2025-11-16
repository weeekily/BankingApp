import re

def login():
    print("================================")
    print("     PYTHON BAN LOGIN PAGE     ")
    print("================================")

    # Username: samo slova i brojevi, do 15 karaktera
    username = input("Enter username: ")

    if not re.match(r'^[A-Za-z0-9]{1,15}$', username):
        print("❌ Invalid username! Use only letters and numbers (max 15).")
        return None

    # Password: do 15 karaktera, bilo koji simbol dozvoljen
    password = input("Enter password: ")

    if len(password) == 0 or len(password) > 15:
        print("❌ Invalid password length! Must be between 1 and 15 characters.")
        return None

    print(f"\n✅ Welcome, {username}! Login successful.\n")
    return {"username": username, "password": password}
