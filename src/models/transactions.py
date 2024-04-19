from peewee import *
from src.models.base import BaseModel
from src.models.wallet import Wallet
from datetime import datetime


class Transaction(BaseModel):
    id = PrimaryKeyField()
    amount = FloatField()
    type = CharField()
    wallet = ForeignKeyField(Wallet, backref='transactions')
    date = DateTimeField(default=datetime.now)