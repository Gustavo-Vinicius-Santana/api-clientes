import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///db.sqlite"  # Arquivo SQLite chamado db.sqlite na raiz do projeto
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False