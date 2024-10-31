from flask import Flask
from models import db
from config import Config
from controllers.produto_controller import produto_bp
from controllers.usuario_controller import usuario_bp
from controllers.cliente_controller import cliente_bp
from controllers.pedido_controller import pedido_bp

def criar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registrar os blueprints dos controladores
    app.register_blueprint(produto_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(pedido_bp)

    app.run(debug=True)

if __name__ == '__main__':
    criar_app()
