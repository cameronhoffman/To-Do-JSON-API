from peewee import *

from models import BaseModel

class ItemList(BaseModel):
    class Meta:
        table_name = 'item_list'
    name = TextField()