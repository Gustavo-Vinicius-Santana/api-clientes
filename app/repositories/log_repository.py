from app.extensions import mongo
from app.models.log_mongo import create_log

class LogRepository:
    @staticmethod
    def create(user_id, acao, detalhes=None):
        log = create_log(user_id, acao, detalhes)
        mongo.db.logs.insert_one(log)
        return log

    @staticmethod
    def get_all():
        return list(mongo.db.logs.find({}, {"_id": 0}))

    @staticmethod
    def collection():
        """
        Retorna a coleção do Mongo (para queries mais complexas).
        """
        return mongo.db.logs