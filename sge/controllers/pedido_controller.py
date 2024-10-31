from flask import Blueprint, request, jsonify
from models import db
from models.pedido import Pedido
from models.detalhe_pedido import DetalhePedido
from datetime import datetime

pedido_bp = Blueprint('pedidos', __name__)

@pedido_bp.route('/pedidos', methods=['POST'])
def criar_pedido():
    data = request.json
    novo_pedido = Pedido(
        cliente_id=data['cliente_id'],
        data_compra=datetime.strptime(data['data_compra'], '%Y-%m-%d')
    )
    db.session.add(novo_pedido)
    db.session.commit()

    for detalhe in data.get('detalhes', []):
        novo_detalhe = DetalhePedido(
            dt_pedido_id=novo_pedido.pedido_id,
            dt_produto_id=detalhe['dt_produto_id'],
            dt_valor=detalhe['dt_valor'],
            dt_desconto=detalhe.get('dt_desconto', 0)
        )
        db.session.add(novo_detalhe)
    db.session.commit()

    return jsonify({'id': novo_pedido.pedido_id, 'cliente_id': novo_pedido.cliente_id}), 201

@pedido_bp.route('/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([{'id': p.pedido_id, 'cliente_id': p.cliente_id} for p in pedidos]), 200
