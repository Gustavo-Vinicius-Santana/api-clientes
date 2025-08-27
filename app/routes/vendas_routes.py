from flask import Blueprint, request, jsonify
from app.services.venda_service import VendaService

vendas_bp = Blueprint("vendas", __name__, url_prefix="/vendas")

class VendasRoutes:
    @vendas_bp.route("", methods=["GET"])
    def listar_vendas():
        vendas = VendaService.listar_vendas()
        resultado = []
        for v in vendas:
            resultado.append({
                "id": v.id,
                "produto_id": v.produto_id,
                "cliente_id": v.cliente_id,
                "quantidade": v.quantidade,
            })
        return jsonify(resultado), 200

    @vendas_bp.route("", methods=["POST"])
    def cadastrar_venda():
        data = request.json
        venda = VendaService.cadastrar_venda(data)
        return jsonify({
            "id": venda.id,
            "produto_id": venda.produto_id,
            "cliente_id": venda.cliente_id,
            "quantidade": venda.quantidade,
        }), 201