from app.repositories.produto_respository import ProdutoRepository
from app.repositories.log_repository import LogRepository

class ProdutoService:
    @staticmethod
    def cadastrar_produto(data):
        LogRepository.create(user_id=1, acao="cadastrar_produto", detalhes=data)
        return ProdutoRepository.create(data)
    
    @staticmethod
    def listar_produtos():
        return ProdutoRepository.get_all()
    
    @staticmethod
    def excluir_produto(id):
        LogRepository.create(user_id=1, acao="excluir_produto", detalhes={"id": id})
        return ProdutoRepository.delete(id)
    
    @staticmethod
    def atualizar_produto(id, data):
        LogRepository.create(user_id=1, acao="atualizar_produto", detalhes={"id": id, "data": data})
        return ProdutoRepository.update(id, data)
    
    @staticmethod
    def buscar_produto(id):
        return ProdutoRepository.get_by_id(id)