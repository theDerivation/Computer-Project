from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "newton"
PASSWORD = "password"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/apparatus')
def apparatus():
    return render_template('apparatus.html')

@app.route('/chemicals')
def chemicals():
    return render_template('chemicals.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if login_is_successful(username, password):
        return redirect(url_for('inventory'))
    else:
        return redirect('/')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

def login_is_successful(username, password):
    return username == USERNAME and password == PASSWORD

if __name__ == '__main__':
    app.run(debug=True)
