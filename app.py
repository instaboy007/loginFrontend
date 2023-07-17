from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def index():
    return render_template("auth/login.html")

@app.route('/register')
def registerUser():
    return render_template("auth/register.html")

