from flask import Flask, render_template, request, redirect, session
from auth import login_web

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

        real_username, user_data = login_web(username, password)

        if real_username is None:
            return render_template("login.html", error="Invalid username or password")

        session['username'] = real_username
        return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    return f"<h1>Welcome {session['username']}!</h1><p>Bank dashboard coming soon...</p>"

if __name__ == "__main__":
    app.run(debug=True)
