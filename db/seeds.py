from peewee import *

from models import Item, ItemList

def seed():
    # Delete the table data.
    ItemList.delete().execute()
    Item.delete().execute()

    # Create the initial item list
    item_list = ItemList(name='Main List')
    item_list.save()

    ItemList(name='Secondary List').save()

    # Create items under the item list
    Item(name='Clean the room', item_list=item_list.id).save()
    Item(name='Take out the trash', item_list=item_list.id).save()
    Item(name='Sweep the floors', item_list=item_list.id).save()

if __name__ == "__main__":
    seed()
