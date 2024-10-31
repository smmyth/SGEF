from flask import Blueprint, request, jsonify
from models import db
from models.usuario import Usuario

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    novo_usuario = Usuario(
        usuario_login=data['usuario_login'],
        usuario_senha=data['usuario_senha']
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'id': novo_usuario.usuario_id, 'usuario_login': novo_usuario.usuario_login}), 201

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.usuario_id, 'usuario_login': u.usuario_login} for u in usuarios]), 200
