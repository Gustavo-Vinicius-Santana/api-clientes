from flask import Flask
from .routes.main_routes import main_bp
from .routes.clientes_routes import clientes_bp
from .routes.produtos_routes import produtos_bp
from .routes.vendas_routes import vendas_bp
from .routes.log_routes import log_bp
from .extensions import db, migrate, mongo

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    mongo.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(produtos_bp)
    app.register_blueprint(vendas_bp)
    app.register_blueprint(log_bp)

    return app