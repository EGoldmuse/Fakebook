from flask.helpers import flash, url_for
from .import bp as app
from flask import render_template, request, redirect
from flask_login import current_user
from app import db
from app.blueprints.authentication.models import User
from app.blueprints.blog.models import  Post
import boto3




@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        new_post = Post(body=request.form.get('body_text'), user_id=current_user.id)
        new_post.save()
        flash('Post added successfully', 'success')

    context = {
        'posts': current_user.followed_posts() if current_user.is_authenticated else []
    }
    return render_template('home.html', **context)

        
# profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    #s3 = boto3.client()

    #for bucket in s3.buckets.all():
    #    print(bucket.name)

    if request.method == 'POST':
    
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first_name')
        u.last_name = request.form.get('last_name')
        u.email = request.form.get('email')
        #u.bio = 
        
        db.session.commit()
        flash('Profile updated successfully', 'info')
        return redirect(url_for('main.profile'))

    context = {
        'posts': current_user.own_posts()
    }
    return render_template('profile.html', **context)

# contact
@app.route('/contact')
def contact():
    return "This is the contact page."
