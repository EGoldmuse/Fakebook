from .import bp as app
from flask import render_template

posts = [
        {
            'id': 1,
            'body': 'This is the first blog post',
            'author': 'Lucas L.',
            'timestamp': '10-2-2020',
            'items': {
                'health': 10,
                'mana': 5
            }
        },
        {
            'id': 2,
            'body': 'This is the second blog post',
            'author': 'Derek H.',
            'timestamp': '10-25-2020',
            'items': {
                'health': 8,
                'mana': 3
            }
        },
        {
            'id': 3,
            'body': 'This is the third blog post',
            'author': 'Joel Carter',
            'timestamp': '11-2-2020',
            'items': {
                'health': 9,
                'mana': 9
            }
        }
    ]

@app.route('/')
def home():
    context = {
        'posts': posts
    }
    return render_template('home.html', **context)

# profile
@app.route('/profile')
def profile():
    logged_in_user = 'Derek'
    return render_template('profile.html', u=logged_in_user)

# contact
@app.route('/contact')
def contact():
    return "This is the contact page."
