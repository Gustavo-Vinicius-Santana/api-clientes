import app.repositories.produto_respository as produto_repository

class ProdutoService:
    @staticmethod
    def listar_produtos():
        return produto_repository.ProdutoRepository.get_all()

    @staticmethod
    def cadastrar_produto(data):
        return produto_repository.ProdutoRepository.create(data)