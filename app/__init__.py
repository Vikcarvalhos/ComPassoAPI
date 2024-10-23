from flask import Flask
from flask_cors import CORS
from .routes import main  # Use relative import

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Register the routes
    app.register_blueprint(main)

    return app

# Create the application
app = create_app()

# Run the application if the file is called directly
if __name__ == "__main__":
    app.run(debug=False)