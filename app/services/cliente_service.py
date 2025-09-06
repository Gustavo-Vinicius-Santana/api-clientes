from app.repositories.cliente_repository import ClienteRepository
from app.repositories.log_repository import LogRepository

class ClienteService:
    @staticmethod
    def cadastrar_cliente(data):
        LogRepository.create(user_id=1, acao="cadastrar_cliente", detalhes=data)
        return ClienteRepository.create(data)

    @staticmethod
    def listar_clientes():
        return ClienteRepository.get_all()

    @staticmethod
    def excluir_cliente(id):
        LogRepository.create(user_id=1, acao="excluir_cliente", detalhes={"id": id})
        return ClienteRepository.delete(id)
    
    @staticmethod
    def atualizar_cliente(id, data):
        LogRepository.create(user_id=1, acao="atualizar_cliente", detalhes={"id": id, "data": data})
        return ClienteRepository.update(id, data)

    @staticmethod
    def buscar_cliente(id):
        return ClienteRepository.get_by_id(id)