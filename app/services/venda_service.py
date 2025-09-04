from app.repositories.venda_repository import VendaRepository
from app.repositories.log_repository import LogRepository

class VendaService:
    @staticmethod
    def cadastrar_venda(data):
        LogRepository.create(user_id=1, acao="cadastrar_venda", detalhes=data)
        return VendaRepository.create(data)
    
    @staticmethod
    def listar_vendas():
        return VendaRepository.get_all()
    
    @staticmethod
    def excluir_venda(id):
        LogRepository.create(user_id=1, acao="excluir_venda", detalhes={"id": id})
        return VendaRepository.delete(id)
    
    @staticmethod
    def atualizar_venda(id, data):
        LogRepository.create(user_id=1, acao="atualizar_venda", detalhes={"id": id, "data": data})
        return VendaRepository.update(id, data)
    
    @staticmethod
    def buscar_venda(id):
        return VendaRepository.get_by_id(id)