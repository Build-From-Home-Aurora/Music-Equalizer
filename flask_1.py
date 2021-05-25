from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '3607e575902461b02264757077c5f3830a0cc06734fca75dbc29003c14be4667'



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="Home")


@app.route("/about")
def about():
    return render_template('about.html',title="About")


@app.route("/signup")
def signup():
    form = RegistrationForm()
    return render_template('signup.html',title="Home",form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title="Home",form=form)


if __name__ == '__main__':
        app.run(debug=True)