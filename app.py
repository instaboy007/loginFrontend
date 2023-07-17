from flask import *
from models.loginForm import LoginForm

app = Flask(__name__)
app.secret_key = 'instaboy\'ssupersecretkey'

@app.route('/login', methods=['GET', 'POST'])
def loginUser():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect('/home')
    elif request.method == 'POST' and not form.validate():
        return render_template("auth/login.html", form = form)
    else:
        return render_template("auth/login.html")

@app.route('/home')
def renderHome():
    return render_template('home/home.html')


