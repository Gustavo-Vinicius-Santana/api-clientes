import app.services.produto_service as produto_service
from flask import Blueprint, request, jsonify

produtos_bp = Blueprint("produtos", __name__, url_prefix="/produtos")

@produtos_bp.route("", methods=["GET"])
def listar_produtos():
    produtos = produto_service.ProdutoService.listar_produtos()
    resultado = []
    for p in produtos:
        resultado.append({
            "id": p.id,
            "nome": p.nome,
            "preco": p.preco
        })
    return jsonify(resultado), 200

@produtos_bp.route("", methods=["POST"])
def cadastrar_produto():
    data = request.json
    produto = produto_service.ProdutoService.cadastrar_produto(data)
    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco
    }), 201