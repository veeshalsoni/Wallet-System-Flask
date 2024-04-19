from src.frameworks.db import wallet_db
from src.models.user import User
from src.models.wallet import Wallet
from src.models.transactions import Transaction


DB_MODELS = [User, Wallet, Transaction]


def create_models():
    wallet_db.create_tables(DB_MODELS, safe=True)
