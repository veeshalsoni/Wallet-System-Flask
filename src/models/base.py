from peewee import Model
from src.frameworks.db import wallet_db

class BaseModel(Model):
    class Meta:
        database = wallet_db
