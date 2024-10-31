from . import db

class DetalhePedido(db.Model):
    __tablename__ = 'detalhes_pedidos'

    dt_id = db.Column(db.Integer, primary_key=True)
    dt_pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'), nullable=False)
    dt_produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'), nullable=False)
    dt_valor = db.Column(db.Numeric(10, 2), nullable=False)
    dt_desconto = db.Column(db.Numeric(10, 2), nullable=True)

    pedido = db.relationship('Pedido', backref=db.backref('detalhes', lazy=True))
    produto = db.relationship('Produto', backref=db.backref('detalhes', lazy=True))
