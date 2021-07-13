from flask import Blueprint
# from.import routes


# from . import routes

bp = Blueprint('main', __name__, url_prefix='/')

from .import routes
