from flask import render_template, url_for
from app.blueprints.blog.models import Post
from .import bp as app

@app.route('/post/<int:id>')
def get_post(id):
    context = {
        'p': Post.query.get(id)
    }
    return render_template('blog-single.html', **context)

#@app.route('/profile/<int:user_id>')
#def get_own_post(id):
#    context = {
#        'p': Post.query.get(id)
#    }
#    return render_template('profile.html', **context)