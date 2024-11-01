from flask import Blueprint, jsonify, request, abort
from your_app.models import Product  # Adjust the import based on your project structure
from your_app.database import db_session

# Create a Blueprint for your routes
bp = Blueprint('products', __name__)

@bp.route('/products', methods=['GET'])
def list_all_products():
    """Retrieve all products."""
    products = db_session.query(Product).all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category': product.category,
        'available': product.available
    } for product in products]), 200

@bp.route('/products/name', methods=['GET'])
def list_by_name():
    """Retrieve products by name."""
    name = request.args.get('name')
    products = db_session.query(Product).filter(Product.name.ilike(f'%{name}%')).all()
    
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category': product.category,
        'available': product.available
    } for product in products]), 200

@bp.route('/products/category', methods=['GET'])
def list_by_category():
    """Retrieve products by category."""
    category = request.args.get('category')
    products = db_session.query(Product).filter(Product.category == category).all()
    
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category': product.category,
        'available': product.available
    } for product in products]), 200

@bp.route('/products/availability', methods=['GET'])
def list_by_availability():
    """Retrieve products by availability status."""
    available = request.args.get('available', type=bool)
    products = db_session.query(Product).filter(Product.available == available).all()
    
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category': product.category,
        'available': product.available
    } for product in products]), 200

# Register the blueprint with your app in your main application file
# app.register_blueprint(bp, url_prefix='/api')
