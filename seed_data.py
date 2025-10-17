import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app import create_app, db
from app.models import Product, UserInteraction

def seed_database():
    app = create_app()
    with app.app_context():
        # Clean up old data
        db.drop_all()
        db.create_all()

        # --- Products ---
        products = [
            Product(name='QuantumCore Laptop', category='Electronics', description='A high-performance laptop for professionals and gamers.'),
            Product(name='StellarSound Headphones', category='Electronics', description='Noise-cancelling over-ear headphones with studio-quality audio.'),
            Product(name='SmartHome Hub Pro', category='Electronics', description='Control all your smart devices from one central hub.'),
            Product(name='The Midnight Serpent', category='Books', description='A thrilling mystery novel by a bestselling author.'),
            Product(name='Culinary Journeys', category='Books', description='A cookbook featuring recipes from around the world.'),
            Product(name='Eco-Friendly Yoga Mat', category='Sports', description='A non-slip yoga mat made from sustainable cork.'),
            Product(name='Pro-Grip Dumbbell Set', category='Sports', description='Adjustable dumbbells for a versatile home workout.'),
            Product(name='Organic Cotton T-Shirt', category='Apparel', description='A soft and breathable t-shirt made from 100% organic cotton.'),
            Product(name='All-Weather Running Jacket', category='Apparel', description='A lightweight, waterproof jacket perfect for any run.'),
        ]
        db.session.bulk_save_objects(products)

        # --- User Interactions ---
        interactions = [
            # User 1: Interested in Electronics
            UserInteraction(user_id=1, product_id=1, interaction_type='purchase'),
            UserInteraction(user_id=1, product_id=3, interaction_type='view'),
            
            # User 2: Interested in Books & Apparel
            UserInteraction(user_id=2, product_id=4, interaction_type='purchase'),
            UserInteraction(user_id=2, product_id=5, interaction_type='view'),
            UserInteraction(user_id=2, product_id=8, interaction_type='view'),

            # User 3: Interested in Sports & Electronics
            UserInteraction(user_id=3, product_id=7, interaction_type='purchase'),
            UserInteraction(user_id=3, product_id=6, interaction_type='view'),
            UserInteraction(user_id=3, product_id=2, interaction_type='view'),

            # User 4: Similar to User 1
            UserInteraction(user_id=4, product_id=1, interaction_type='view'),
            UserInteraction(user_id=4, product_id=2, interaction_type='purchase'),
        ]
        db.session.bulk_save_objects(interactions)

        db.session.commit()
        print("Database has been seeded successfully!")

if __name__ == '__main__':
    seed_database()