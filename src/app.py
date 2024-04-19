from flask_session import Session
from src.models import create_models
from flask_restful import Api


def init_app(app):
    create_models()
    api = Api(app)

    app.secret_key = 'wallet_secret_key'

    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
    app.config['SESSION_PERMANENT'] = False

    Session(app)

    register_api(api)


def register_api(api):
    from src.api import register_resources
    register_resources(api)