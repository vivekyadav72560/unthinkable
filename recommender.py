import pandas as pd
from sklearn.decomposition import TruncatedSVD
from .models import UserInteraction, Product

def get_recommendations(user_id, num_recommendations=5):
    """Generates product recommendations for a given user."""
    interactions = UserInteraction.query.all()
    if not interactions:
        return [], None # Not enough data

    # Create a user-item interaction matrix
    interaction_list = [{'user_id': i.user_id, 'product_id': i.product_id, 'rating': 1} for i in interactions]
    df = pd.DataFrame(interaction_list)
    user_item_matrix = df.pivot_table(index='user_id', columns='product_id', values='rating').fillna(0)

    # Decompose the matrix using SVD
    svd = TruncatedSVD(n_components=min(10, len(user_item_matrix.columns)-1), random_state=42)
    svd_matrix = svd.fit_transform(user_item_matrix)

    # Get predicted ratings
    import numpy as np
    predicted_ratings = np.dot(svd_matrix, svd.components_)
    predicted_ratings_df = pd.DataFrame(predicted_ratings, index=user_item_matrix.index, columns=user_item_matrix.columns)

    # Get recommendations for the target user
    if user_id not in predicted_ratings_df.index:
        return [], None # User has no interactions

    user_ratings = predicted_ratings_df.loc[user_id]
    
    # Filter out products the user has already interacted with
    interacted_products = user_item_matrix.loc[user_id]
    interacted_products = interacted_products[interacted_products > 0].index
    
    recommendations = user_ratings.drop(interacted_products).sort_values(ascending=False)
    
    recommended_product_ids = recommendations.head(num_recommendations).index.tolist()

    # Get user's interaction history for context
    user_history = UserInteraction.query.filter_by(user_id=user_id).all()
    history_product_ids = [h.product_id for h in user_history]
    history_products = Product.query.filter(Product.id.in_(history_product_ids)).all()

    return recommended_product_ids, history_products