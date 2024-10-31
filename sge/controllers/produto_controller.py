from flask import Blueprint, request, jsonify
from models import db
from models.produto import Produto
from models.categoria import Categoria

produto_bp = Blueprint('produtos', __name__)

@produto_bp.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.json
    novo_produto = Produto(
        produto_nome=data['produto_nome'],
        produto_preco=data['produto_preco'],
        categoria_id=data.get('categoria_id')
    )
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'id': novo_produto.produto_id, 'produto_nome': novo_produto.produto_nome}), 201

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{'id': p.produto_id, 'produto_nome': p.produto_nome} for p in produtos]), 200

