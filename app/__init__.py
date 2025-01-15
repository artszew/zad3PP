from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # Initialization Flask
    app = Flask(__name__)

    # Configuration app
    app.config.from_object('app.config.Config')

    # Initialization SQLAlchemy
    db.init_app(app)

    # Blueprints
    with app.app_context():
        from app.routes.web import web_bp
        from app.routes.api import api_bp

        app.register_blueprint(web_bp)
        app.register_blueprint(api_bp)

        # Tables in database
        db.create_all()

    return app

