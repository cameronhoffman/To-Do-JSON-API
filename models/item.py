from peewee import *

from models import BaseModel, ItemList

class Item(BaseModel):
    class Meta:
        table_name = 'item'
    name = TextField()
    item_list = ForeignKeyField(ItemList, backref='item_lists') # Had to turn off 'not null' for field in db, field not passed in creation tests.
    is_complete = BooleanField(default=False)