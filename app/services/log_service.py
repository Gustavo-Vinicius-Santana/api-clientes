from app.repositories.log_repository import LogRepository

class LogService:
    @staticmethod
    def registrar_log(user_id, acao, detalhes=None):
        return LogRepository.create(user_id, acao, detalhes)

    @staticmethod
    def listar_logs():
        return LogRepository.get_all()

    @staticmethod
    def produtos_mais_vendidos(limit=5):
        pipeline = [
            {"$match": {"acao": "VENDA"}},
            {"$group": {
                "_id": "$detalhes.produto_id",
                "total": {"$sum": "$detalhes.quantidade"}
            }},
            {"$sort": {"total": -1}},
            {"$limit": limit}
        ]
        resultados = list(LogRepository.collection().aggregate(pipeline))

        from app.models.produto import Produto
        produtos_info = []
        for r in resultados:
            produto = Produto.query.get(r["_id"])
            if produto:
                produtos_info.append({
                    "produto_id": produto.id,
                    "nome": produto.nome,
                    "total_vendido": r["total"]
                })

        return produtos_info

    @staticmethod
    def dias_com_mais_vendas(limit=5):
        """
        Retorna os dias com maior quantidade de vendas (quantidade de registros de VENDA).
        """
        pipeline = [
            {"$match": {"acao": "VENDA"}},
            {
                "$group": {
                    "_id": {
                        "dia": {"$dateToString": {"format": "%Y-%m-%d", "date": "$criado_em"}}
                    },
                    "total_vendas": {"$sum": 1}
                }
            },
            {"$sort": {"total_vendas": -1}},
            {"$limit": limit}
        ]
        resultados = list(LogRepository.collection().aggregate(pipeline))

        return [
            {"dia": r["_id"]["dia"], "total_vendas": r["total_vendas"]}
            for r in resultados
        ]