# ============================================
# auth.py – upravlja korisnicima i login sistemom
# --------------------------------------------
# - učitava JSON bazu (users)
# - snima sve izmene u JSON
# - obavlja login i kreira nove korisnike
# - validira username i password
# ============================================

import re
import json
import os

# Lokacija JSON fajla u kojem čuvamo sve korisnike
FILE = "database.json"


# ------------------------------
# Učitavanje baze iz JSON fajla
# ------------------------------
def load_data():
    # Ako fajl ne postoji (prvo pokretanje aplikacije)
    if not os.path.exists(FILE):
        return {"users": {}}

    # Inače, učitaj podatke iz JSON-a
    with open(FILE, "r") as f:
        return json.load(f)


# ------------------------------
# Snimanje izmena u JSON fajl
# ------------------------------
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ------------------------------
# LOGIN funkcija
# - validira korisnika
# - kreira novog ako ne postoji
# - proverava password ako postoji
# - vraća username i podatke o korisniku
# ------------------------------
def login():
    print("================================")
    print("     PYTHON BANK LOGIN PAGE     ")
    print("================================")

    data = load_data()

    # Unos username-a
    username = input("Enter username: ")

    # Username sme da ima samo slova i brojeve
    if not re.match(r'^[A-Za-z0-9]{1,15}$', username):
        print("❌ Invalid username! Use only letters and numbers (max 15).")
        return None, None

    # Unos password-a
    password = input("Enter password: ")

    # Password dužina mora biti 1–15
    if len(password) == 0 or len(password) > 15:
        print("❌ Invalid password length! Must be 1-15 characters.")
        return None, None

    # Ako korisnik NE POSTOJI → kreiramo ga
    if username not in data["users"]:
        data["users"][username] = {
            "password": password,
            "balance": 0,
            "transactions": []
        }
        save_data(data)
        print("\n🆕 New user created!\n")

    else:
        # Ako postoji, proveravamo password
        if data["users"][username]["password"] != password:
            print("❌ Incorrect password!")
            return None, None

    print(f"\n✅ Welcome, {username}! Login successful.\n")
    return username, data["users"][username]
