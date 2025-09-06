from datetime import datetime

def create_log(user_id, acao, detalhes=None):
    """
    Cria um log pronto para ser inserido no MongoDB.
    """
    return {
        "user_id": user_id,
        "acao": acao,
        "detalhes": detalhes if detalhes else "",
        "criado_em": datetime.utcnow()
    }