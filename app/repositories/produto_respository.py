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
    def update(id, data):
        produto = Produto.query.get(id)
        for key, value in data.items():
            setattr(produto, key, value)
        db.session.commit()
        return produto
    
    @staticmethod
    def get_by_id(id):
        return Produto.query.get(id)
    
    @staticmethod
    def delete(id):
        produto = Produto.query.get(id)
        db.session.delete(produto)
        db.session.commit()
        return produto

    @staticmethod
    def get_all():
        return Produto.query.all()