from flask import Blueprint, request, jsonify
from models import db
from models.cliente import Cliente

cliente_bp = Blueprint('clientes', __name__)

@cliente_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.json
    novo_cliente = Cliente(
        cliente_nome=data['cliente_nome'],
        cliente_email=data['cliente_email']
    )
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'id': novo_cliente.cliente_id, 'cliente_nome': novo_cliente.cliente_nome}), 201

@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{'id': c.cliente_id, 'cliente_nome': c.cliente_nome} for c in clientes]), 200
