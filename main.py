from flask import Blueprint, jsonify, request
from .models import Product
from .recommender import get_recommendations
from .llm_explainer import generate_explanation

main = Blueprint('main', __name__)

@main.route('/recommendations', methods=['GET'])
def recommendations():
    user_id = request.args.get('user_id', type=int)
    if user_id is None:
        return jsonify({"error": "user_id parameter is required"}), 400

    recommended_ids, user_history = get_recommendations(user_id)

    if not recommended_ids:
        return jsonify({
            "user_id": user_id,
            "recommendations": []
        })

    recommended_products = Product.query.filter(Product.id.in_(recommended_ids)).all()

    response_data = []
    for product in recommended_products:
        explanation = generate_explanation(user_history, product)
        response_data.append({
            "product": product.to_dict(),
            "explanation": explanation
        })
    
    return jsonify({
        "user_id": user_id,
        "recommendations": response_data
    })