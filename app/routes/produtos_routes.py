from flask import Blueprint, request, jsonify
from app.services.produto_service import ProdutoService

produtos_bp = Blueprint("produtos", __name__, url_prefix="/produtos")

@produtos_bp.route("", methods=["POST"])
def cadastrar_produto():
    data = request.json
    produto = ProdutoService.cadastrar_produto(data)
    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco
    }), 201

@produtos_bp.route("", methods=["GET"])
def listar_produtos():
    produtos = ProdutoService.listar_produtos()
    resultado = []
    for p in produtos:
        resultado.append({
            "id": p.id,
            "nome": p.nome,
            "preco": p.preco
        }), 200
    return jsonify(resultado)

@produtos_bp.route("/<int:id>", methods=["GET"])
def buscar_produto(id):
    produto = ProdutoService.buscar_produto(id)
    if not produto:
        return jsonify({"erro": "produto nao encontrado"}), 404
    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco
    }), 200

@produtos_bp.route("/<int:id>", methods=["DELETE"])
def excluir_produto(id):
    produto = ProdutoService.excluir_produto(id)
    if not produto:
        return jsonify({"erro": "produto nao encontrado"}), 404
    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco
    }), 200

@produtos_bp.route("/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    data = request.json
    produto = ProdutoService.atualizar_produto(id, data)
    if not produto:
        return jsonify({"erro": "produto nao encontrado"}), 404
    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco
    }), 200