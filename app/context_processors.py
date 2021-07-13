from flask_login import current_user
from flask import current_app as app
from app.blueprints.shop.models import Cart, Product
from functools import reduce

@app.context_processor
def build_cart():
    cart_dict = {}
    if current_user.is_anonymous:
        return {
            'cart_dict': cart_dict,
            'cart_size': 0,
            'cart_subtotal': 0,
            'cart_tax': 0,
            'cart_grandtotal': 0
        }



    cart = Cart.query.filter_by(user_id=current_user.id).all()
    if len(cart) > 0:
        for cart_item in cart:
            p = Product.query.get(cart_item.product_id)
            if str(p.id) not in cart_dict:
                #p = Product.query.get(cart_item.id)
                cart_dict[str(p.id)] = {
                    'id': cart_item.id,
                    'product_id': p.id,
                    'image': p.image,
                    'quantity': 1,
                    'name': p.name,
                    'description': p.description,
                    'price': f'{p.price:,.2f}',
                    'taxes': p.tax
                }
            else:
                cart_dict[str(p.id)]['quantity'] += 1
            
    return {
        'cart_dict': cart_dict,
        'cart_size': len(cart),
        'cart_subtotal': reduce(lambda x, y:x+y, [i.to_dict()['product'].price for i in cart]) if cart else 0,
        'cart_tax': reduce(lambda x, y:x+y, [i.to_dict()['product'].tax for i in cart]) if cart else 0,
        'cart_grandtotal': reduce(lambda x, y: x+y, [i.to_dict()['product'].price + i.to_dict()['product'].tax for i in cart]) if cart else 0
        }


@app.context_processor
def get_Stripe_keys():
    return{
        'STRIPE_PUBLISHABLE_KEY': app.config.get('STRIPE_PUBLISHABLE_KEY')
    }