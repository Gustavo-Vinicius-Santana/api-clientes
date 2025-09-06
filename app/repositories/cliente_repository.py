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
    def update(id, data):
        cliente = Cliente.query.get(id)
        for key, value in data.items():
            setattr(cliente, key, value)
        db.session.commit()
        return cliente

    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)

    @staticmethod
    def delete(id):
        cliente = Cliente.query.get(id)
        db.session.delete(cliente)
        db.session.commit()
        return cliente

    @staticmethod
    def get_all():
        return Cliente.query.all()