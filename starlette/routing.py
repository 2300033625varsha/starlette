from flask import Blueprint, jsonify, abort
from your_app.models import Product  # Adjust the import based on your project structure
from your_app.database import db_session

# Create a Blueprint for your routes
bp = Blueprint('products', __name__)

@bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by its ID."""
    product = db_session.query(Product).filter(Product.id == product_id).first()
    
    if product is None:
        abort(404, description="Product not found")
    
    db_session.delete(product)  # Remove the product from the session
    db_session.commit()  # Commit the changes to the database
    
    return jsonify({'message': 'Product deleted successfully'}), 200

# Register the blueprint with your app in your main application file
# app.register_blueprint(bp, url_prefix='/api')
