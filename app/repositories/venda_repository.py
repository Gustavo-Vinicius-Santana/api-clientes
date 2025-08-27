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
    def get_all():
        return Venda.query.all()