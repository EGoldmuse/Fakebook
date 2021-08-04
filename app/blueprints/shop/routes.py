from flask.json import jsonify
from stripe.api_resources import payment_method
from .import bp as app
from flask import render_template, flash, request, url_for, session, current_app
from .models import StripeProduct, Cart
from werkzeug.utils import redirect
from flask_login import current_user
import stripe
from app import db



@app.route('/')
def index():
    """
    [GET] /shop
    """
    stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')
    
    context = {
        'products': StripeProduct.query.all()
    }
    return render_template('shop/index.html', **context)

@app.route('/cart')
def cart():
    """
    [GET] /shop/cart
    """
    from app.context_processors import build_cart
    display_cart = build_cart()['cart_dict']
    session['session_display_cart'] = display_cart

    context = {
        'cart' : display_cart.values()
    }

    if not current_user.is_authenticated:
        flash('You must login to view your cart', 'warning')
        return redirect(url_for('authentication.login'))
    return render_template('shop/cart.html', **context)

@app.route('/cart/add')
def add_to_cart():
    """
    [GET] /shop/cart/add
    """
    if not current_user.is_authenticated:
        flash('You must login to add items to your cart', 'warning')
        return redirect(url_for('authentication.login'))

    product = StripeProduct.query.get(request.args.get('id'))

    Cart(user_id=current_user.id, product_id=product.id).save()
    flash(f'You have added {product.name} to the cart', 'success')
    return redirect(url_for('shop.index'))

@app.route('/delete/<product_id>', methods=['DELETE', 'POST'])
def delete_from_cart(product_id):
    product = StripeProduct.query.get(product_id)
    db.session.delete(Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first())
    db.session.commit()
    flash(f'{product.name} has been removed from your cart.' 'success')
    return redirect(url_for('shop.cart'))
    
#@app.route('/seed')
#def seed_stripe_products():
#    stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')

#    def seed_data():
#        list_to_store_in_db = []
#        for p in stripe.Product.list().get('data'):
#            list_to_store_in_db.append(StripeProduct(stripe_product_id=p['id'], name=p['name'], image=p['image']))
        
#        db.session.add_all(list_to_store_in_db)
#        db.session.commit()

@app.route('/products')
def shop_products():
    pass

@app.route('/success')
def shop_success():
    pass

@app.route('/failure')
def shop_failure():
    pass

@app.route('/checkout', methods=['POST'])
def checkout():
    stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')
    dc = session.get('session_display_cart')
    l_items=[]
    for product in dc.values():
        product_dict = {
            'price_data': {
                'currency':'usd',
                'product_data': {
                    'name': product['name'],
                    'images': [product['image']]
                },
                'unit_amount': int(float(product['price']) * 100),
            },
            'quantity': product['quantity'],
        }       
        l_items.append(product_dict)
    

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items = l_items,
            mode = 'payment',
            success_url = 'http://localhost:5000/shop/cart',
            cancel_url = 'http://localhost:5000/shop/cart'
        )
        print(checkout_session)
        [db.session.delete(i) for i in Cart.query.filter_by(user_id=current_user.id).all()]
        db.session.commit()

        flash('Your order was processed successfuly', 'primary')
        return jsonify({ 'session_id': checkout_session.id })
    except Exception as e:
        return jsonify(error=str(e)), 403
