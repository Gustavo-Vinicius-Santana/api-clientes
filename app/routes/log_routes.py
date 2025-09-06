from flask import Blueprint, jsonify
from app.services.log_service import LogService

log_bp = Blueprint("logs", __name__)

@log_bp.route("/logs", methods=["GET"])
def listar_logs():
    return jsonify(LogService.listar_logs()), 200

@log_bp.route("/logs/top-vendidos", methods=["GET"])
def top_vendidos():
    return jsonify(LogService.produtos_mais_vendidos(limit=5)), 200

@log_bp.route("/logs/dias-mais-vendas", methods=["GET"])
def dias_mais_vendas():
    data = LogService.dias_com_mais_vendas(limit=5)
    return jsonify(data), 200