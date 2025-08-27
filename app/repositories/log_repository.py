from app.extensions import mongo
from app.models.log_mongo import create_log

class LogRepository:
    @staticmethod
    def create(user_id, acao, detalhes=None):
        log = create_log(user_id, acao, detalhes)
        # Garantindo que estamos dentro do contexto do Flask
        mongo.db.logs.insert_one(log)
        return log

    @staticmethod
    def get_all():
        return list(mongo.db.logs.find({}, {"_id": 0}))