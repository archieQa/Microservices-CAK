# __init__.py
from flask import Flask
from .config import Config
from .extensions import db, migrate, oauth
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    oauth.init_app(app)  # Initialize OAuth with the app

    # Configure OAuth clients
    configure_oauth_clients(app)  # Register OAuth clients using settings from config.py

    # Correct way to debug registered clients
    print("Registered OAuth clients:")
    for client_name in oauth._clients:  # Access internal _clients dictionary
        print(f" - {client_name}")

    with app.app_context():
        from . import routes, auth
        db.create_all()

        # Register blueprints
        register_blueprints(app)

    return app

def configure_oauth_clients(app):
    """Register OAuth clients based on configuration settings."""
    oauth_clients = {
        'google': {
            'client_id': app.config['GOOGLE_CLIENT_ID'],
            'client_secret': app.config['GOOGLE_CLIENT_SECRET'],
            'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
            'access_token_url': 'https://oauth2.googleapis.com/token',
            'userinfo_endpoint': 'https://openidconnect.googleapis.com/v1/userinfo',
            'client_kwargs': {'scope': 'openid profile email'},
        },
        'github': {
            'client_id': app.config['GITHUB_CLIENT_ID'],
            'client_secret': app.config['GITHUB_CLIENT_SECRET'],
            'authorize_url': 'https://github.com/login/oauth/authorize',
            'access_token_url': 'https://github.com/login/oauth/access_token',
            'userinfo_endpoint': 'https://api.github.com/user',
            'client_kwargs': {'scope': 'user:email'},
        }
    }

    for name, config in oauth_clients.items():
        oauth.register(name=name, **config)

def register_blueprints(app):
    """Register Flask blueprints."""
    from .auth import auth_bp
    from .oauth import oauth_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(oauth_bp, url_prefix='/oauth')
