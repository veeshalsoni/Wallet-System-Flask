from peewee import *
from src.models.base import BaseModel

class User(BaseModel):
    phone = CharField(unique=True)
