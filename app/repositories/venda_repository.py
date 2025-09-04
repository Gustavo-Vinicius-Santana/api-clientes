from app.extensions import db
from app.models.venda import Venda

class VendaRepository:
    @staticmethod
    def create(data):
        venda = Venda(**data)
        db.session.add(venda)
        db.session.commit()
        return venda
    
    @staticmethod
    def update(id, data):
        venda = Venda.query.get(id)
        for key, value in data.items():
            setattr(venda, key, value)
        db.session.commit()
        return venda
    
    @staticmethod
    def get_by_id(id):
        return Venda.query.get(id)
    
    @staticmethod
    def delete(id):
        venda = Venda.query.get(id)
        db.session.delete(venda)
        db.session.commit()
        return venda

    @staticmethod
    def get_all():
        return Venda.query.all()