from flask import Blueprint, request, jsonify
from app.services.venda_service import VendaService

vendas_bp = Blueprint("vendas", __name__, url_prefix="/vendas")

@vendas_bp.route("", methods=["POST"])
def cadastrar_venda():
    data = request.json
    venda = VendaService.cadastrar_venda(data)
    return jsonify({
        "id": venda.id,
        "produto_id": venda.produto_id,
        "cliente_id": venda.cliente_id,
        "quantidade": venda.quantidade,
        "data": venda.data,
    }), 201

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
            "data": v.data,
        }), 200
    return jsonify(resultado)

@vendas_bp.route("/<int:id>", methods=["GET"])
def buscar_venda(id):
    venda = VendaService.buscar_venda(id)
    if not venda:
        return jsonify({"erro": "venda nao encontrada"}), 404
    return jsonify({
        "id": venda.id,
        "produto_id": venda.produto_id,
        "cliente_id": venda.cliente_id,
        "quantidade": venda.quantidade,
        "data": venda.data,
    }), 200

@vendas_bp.route("/<int:id>", methods=["DELETE"])
def excluir_venda(id):
    venda = VendaService.excluir_venda(id)
    if not venda:
        return jsonify({"erro": "venda nao encontrada"}), 404
    return jsonify({
        "id": venda.id,
        "produto_id": venda.produto_id,
        "cliente_id": venda.cliente_id,
        "quantidade": venda.quantidade,
        "data": venda.data,
    }), 200

@vendas_bp.route("/<int:id>", methods=["PUT"])
def atualizar_venda(id):
    data = request.json
    venda = VendaService.atualizar_venda(id, data)
    if not venda:
        return jsonify({"erro": "venda nao encontrada"}), 404
    return jsonify({
        "id": venda.id,
        "produto_id": venda.produto_id,
        "cliente_id": venda.cliente_id,
        "quantidade": venda.quantidade,
        "data": venda.data,
    }), 200