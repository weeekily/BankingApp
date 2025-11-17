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

    return f"""
        <h1>Welcome {session['username']}!</h1>
        <p>Bank dashboard coming soon...</p>
        <a href='/logout'>Logout</a>
    """


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
