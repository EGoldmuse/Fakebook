from flask.helpers import url_for
from .import bp as app
from flask import render_template, redirect, flash, request
from .models import Product, Cart
from flask_login import current_user

@app.route('/')
def index():
    """
    [GET] /shop
    """
    context = {
        'products': Product.query.all()
    }
    return render_template('shop/index.html', **context)

@app.route('/cart')
def cart():
    """
    [GET] /shop/cart
    """
    if not current_user.is_authenticated:
        flash('You must login to view your cart', 'warning')
        return redirect(url_for('authentication.login'))
    return render_template('shop/cart.html')

@app.route('/cart/add')
def add_to_cart():
    """
    [GET] /shop/cart/add
    """
    if not current_user.is_authenticated:
        flash('You must login to add items to your cart', 'warning')
        return redirect(url_for('authentication.login'))
        
    # Make a new product
    product = Product.query.get(request.args.get('id'))

    # Save it to their cart
    Cart(user_id=current_user.id, product_id=product.id).save()
    flash(f'You have added {product.name} to the cart', 'success')
    return redirect(url_for('shop.index'))

@app.route('/success')
def shop_success():
    pass

@app.route('/failure')
def shop_failure():
    pass

@app.route('/checkout')
def shop_checkout():
    pass

