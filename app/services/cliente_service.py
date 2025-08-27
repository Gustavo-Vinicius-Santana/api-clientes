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