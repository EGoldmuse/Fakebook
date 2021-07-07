from flask import jsonify, render_template
from .import bp as app


"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""

@app.route('/shop/products')
def shop_products():
    pass

@app.route('/shop/cart')
def shop_cart():
    pass

@app.route('/shop/success')
def shop_success():
    pass

@app.route('/shop/failure')
def shop_faiure():
    pass