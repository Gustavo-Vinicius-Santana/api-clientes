import os

class Config:
    # --- SQLite ---
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///db.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- MongoDB ---
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017/db-api-clientes"
    )