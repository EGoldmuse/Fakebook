from flask import render_template, url_for
from app.blueprints.main.routes import posts
from .import bp as app

@app.route('/post/<int:id>')
def get_post(id):
    for p in posts:
        if p['id'] == id:
            post = p
            break
    context = {
        'p': post
    }
    return render_template('blog-single.html', **context)