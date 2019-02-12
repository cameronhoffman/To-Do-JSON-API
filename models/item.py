from peewee import *

from models import BaseModel, ItemList

class Item(BaseModel):
    name = TextField()
    item_list = ForeignKeyField(ItemList, backref='item_lists')
