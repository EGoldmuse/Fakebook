from flask import jsonify, render_template, url_for
from .import bp as app
from app.blueprints.blog.routes import posts

@app.route("/")
def home():

    context = {
        'posts': posts
    }
    return render_template('home.html', **context)


@app.route("/users")
def get_users():
    return jsonify({ "message": "This works!" })

# Profile
@app.route("/profile")
def profile():
    logged_in_user = 'Eli'
    return render_template('profile.html', u=logged_in_user)
# blog
#@app.route("/blog")
#def blog():
    #return "This is all about the app"
# Contact
@app.route("/contact")
def contact():
    return "Get in touch with the team"  