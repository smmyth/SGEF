from . import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True)
    usuario_login = db.Column(db.String(20), nullable=False)
    usuario_senha = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f'<Usuário {self.usuario_login}>'
