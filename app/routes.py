from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yury'}
    posts = [
        {
            'author': {'username': 'Arni'},
            'body': "I'll be back!"
        },
        {
            'author': {'username': 'Sarah'},
            'body': "No, you won't !!!"
        }
    ]
    return render_template('index.html', title='Test', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
