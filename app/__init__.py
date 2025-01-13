#Inicjalizuje aplikację Flask.
#Łączy aplikację z bazą danych przez SQLAlchemy.
#Rejestruje blueprinty dla ścieżek
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from app.routes.web import web_bp
        from app.routes.api import api_bp
        app.register_blueprint(web_bp)
        app.register_blueprint(api_bp)

        db.create_all()

    return app
