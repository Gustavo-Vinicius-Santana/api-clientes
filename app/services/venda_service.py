import app.repositories.venda_repository as venda_repository

class VendaService:
    @staticmethod
    def listar_vendas():
        return venda_repository.VendaRepository.get_all()

    @staticmethod
    def cadastrar_venda(data):
        return venda_repository.VendaRepository.create(data)