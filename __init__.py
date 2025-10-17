from flask import Flask
from .database import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) # Enable Cross-Origin Resource Sharing

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app