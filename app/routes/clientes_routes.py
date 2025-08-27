from flask import Blueprint, request, jsonify
from app.services.cliente_service import ClienteService

clientes_bp = Blueprint("clientes", __name__, url_prefix="/clientes")

@clientes_bp.route("", methods=["POST"])
def cadastrar_cliente():
    data = request.json
    if not data.get("nome") or not data.get("email"):
        return jsonify({"erro": "nome e email são obrigatórios"}), 400

    cliente = ClienteService.cadastrar_cliente(data)
    return jsonify({
        "id": cliente.id,
        "nome": cliente.nome,
        "email": cliente.email,
        "telefone": cliente.telefone
    }), 201

@clientes_bp.route("", methods=["GET"])
def listar_clientes():
    clientes = ClienteService.listar_clientes()
    resultado = []
    for c in clientes:
        resultado.append({
            "id": c.id,
            "nome": c.nome,
            "email": c.email,
            "telefone": c.telefone
        })
    return jsonify(resultado)

@clientes_bp.route("/<int:id>", methods=["GET"])
def buscar_cliente(id):
    cliente = ClienteService.buscar_cliente(id)
    if not cliente:
        return jsonify({"erro": "cliente nao encontrado"}), 404
    return jsonify({
        "id": cliente.id,
        "nome": cliente.nome,
        "email": cliente.email,
        "telefone": cliente.telefone
    }), 200

@clientes_bp.route("/<int:id>", methods=["DELETE"])
def excluir_cliente(id):
    cliente = ClienteService.excluir_cliente(id)
    if not cliente:
        return jsonify({"erro": "cliente nao encontrado"}), 404
    return jsonify({
        "id": cliente.id,
        "nome": cliente.nome,
        "email": cliente.email,
        "telefone": cliente.telefone
    }), 200

@clientes_bp.route("/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    data = request.json
    cliente = ClienteService.atualizar_cliente(id, data)
    if not cliente:
        return jsonify({"erro": "cliente nao encontrado"}), 404
    return jsonify({
        "id": cliente.id,
        "nome": cliente.nome,
        "email": cliente.email,
        "telefone": cliente.telefone
    }), 200