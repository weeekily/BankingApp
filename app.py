
from flask import Flask, render_template, request, redirect, session
from auth import login_web


def is_logged_in():
    return 'username' in session


app = Flask(__name__)
app.secret_key = "nikola123"


@app.route('/')
def home():
    return redirect('/login')


from flask import Flask, render_template, request, redirect, session
from auth import load_data, save_data

app = Flask(__name__)
app.secret_key = "nikola123"


@app.route('/')
def home():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        data = load_data()

        # Ako user ne postoji → kreiramo ga
        if username not in data["users"]:
            data["users"][username] = {
                "password": password,
                "balance": 0,
                "transactions": []
            }
            save_data(data)

        else:
            # Ako već postoji → proveri password
            if data["users"][username]["password"] != password:
                return render_template("login.html", error="Wrong password")

        # Snimi usera u sesiju
        session['username'] = username
        return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    return render_template("dashboard.html", username=session['username'])

@app.route('/balance')
def balance():
    if 'username' not in session:
        return redirect('/login')

    data = load_data()
    user = session['username']
    balance = data["users"][user]["balance"]

    return render_template("balance.html", balance=balance)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit_page():
    if 'username' not in session:
        return redirect('/login')

    user = session['username']
    data = load_data()

    if request.method == 'POST':
        amount = request.form.get("amount")

        try:
            amount = float(amount)
        except:
            return render_template("deposit.html", error="Amount must be a number")

        if amount <= 0:
            return render_template("deposit.html", error="Amount must be positive")

        from datetime import datetime
        full_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data["users"][user]["balance"] += amount
        data["users"][user]["transactions"].append(
            f"[{full_time}] Deposit: ${amount:.2f}"
        )

        save_data(data)

        return render_template("deposit.html", success=f"Successfully deposited ${amount:.2f}")

    return render_template("deposit.html")

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw_page():
    if 'username' not in session:
        return redirect('/login')

    user = session['username']
    data = load_data()

    if request.method == 'POST':
        amount = request.form.get("amount")

        try:
            amount = float(amount)
        except:
            return render_template("withdraw.html", error="Amount must be a number")

        if amount <= 0:
            return render_template("withdraw.html", error="Amount must be positive")

        if amount > data["users"][user]["balance"]:
            return render_template("withdraw.html", error="Insufficient funds")

        from datetime import datetime
        full_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data["users"][user]["balance"] -= amount
        data["users"][user]["transactions"].append(
            f"[{full_time}] Withdraw: ${amount:.2f}"
        )

        save_data(data)

        return render_template("withdraw.html", success=f"Successfully withdrew ${amount:.2f}")

    return render_template("withdraw.html")

@app.route('/transactions')
def transactions():
    if 'username' not in session:
        return redirect('/login')

    user = session['username']
    data = load_data()
    transactions = data["users"][user]["transactions"]

    return render_template("transactions.html", transactions=transactions)



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
