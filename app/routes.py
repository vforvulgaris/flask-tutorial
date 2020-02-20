from flask import render_template, flash, redirect, url_for
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
