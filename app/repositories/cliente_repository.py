from app.extensions import db
from app.models.cliente import Cliente

class ClienteRepository:
    @staticmethod
    def create(data):
        cliente = Cliente(**data)
        db.session.add(cliente)
        db.session.commit()
        return cliente

    @staticmethod
    def get_all():
        return Cliente.query.all()