from app import app
from flask import jsonify, render_template

"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""
@app.route("/users")
def get_users():
    return jsonify({ "message": "This works!" })

# Profile
@app.route("/profile")
def profile():
    logged_in_user = 'Eli'
    return render_template('profile.html', u=logged_in_user)
# blog
@app.route("/blog")
def blog():
    return "This is all about the app"
# Contact
@app.route("/contact")
def contact():
    return "Get in touch with the team"   