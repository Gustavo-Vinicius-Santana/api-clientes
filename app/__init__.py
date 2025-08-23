from flask import Flask
from .routes.main_routes import main_bp
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_bp)
    return app