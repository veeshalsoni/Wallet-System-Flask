from flask import Flask
from src.app import init_app
from src.routes import user_bp

app = Flask(__name__)
init_app(app)

app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
