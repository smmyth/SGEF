from . import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    pedido_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'), nullable=False)
    data_compra = db.Column(db.Date, nullable=False)

    cliente = db.relationship('Cliente', backref=db.backref('pedidos', lazy=True))

    def __repr__(self):
        return f'<Pedido {self.pedido_id}>'
