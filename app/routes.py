from flask import render_template
from app import app


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
