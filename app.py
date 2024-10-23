from flask import Flask
from flask_cors import CORS
from app.routes import main  # Importar diretamente as rotas

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Registrar as rotas
    app.register_blueprint(main)

    return app

# Criar a aplicação
app = create_app()

# Executar a aplicação se o arquivo for chamado diretamente
if __name__ == "__main__":
    app.run(debug=False)
