from peewee import *

from models.base import BaseModel

class ItemList(BaseModel):
    class Meta:
        table_name = 'item_list'
    name = TextField()
