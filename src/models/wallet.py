from peewee import *
from src.models.base import BaseModel
from src.models.user import User

class Wallet(BaseModel):
    class Meta:
        indexes = (
            (('user', 'name'), True),
        )
    
    id = PrimaryKeyField()
    balance = FloatField(default=0.0)
    name = CharField(max_length=100)
    user = ForeignKeyField(User, backref='wallets')
