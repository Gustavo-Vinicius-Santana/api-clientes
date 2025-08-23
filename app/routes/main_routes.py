from flask import Blueprint, jsonify

# o nome do Blueprint deve ser exatamente 'main_bp'
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return jsonify({
        "mensagem": "Hello, Flask!",
        "status": "sucesso"
    })

@main_bp.route("/sobre")
def sobre():
    return jsonify({"mensagem": "Sobre a aplicação"})