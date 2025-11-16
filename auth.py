def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "1234":
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials")
        return False
