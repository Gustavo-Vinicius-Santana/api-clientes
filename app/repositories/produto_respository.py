from app.extensions import db
from app.models.produto import Produto

class ProdutoRepository:
    @staticmethod
    def create(data):
        produto = Produto(**data)
        db.session.add(produto)
        db.session.commit()
        return produto

    @staticmethod
    def get_all():
        return Produto.query.all()