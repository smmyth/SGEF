from . import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column(db.Integer, primary_key=True)
    nome_categoria = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Categoria {self.nome_categoria}>'
