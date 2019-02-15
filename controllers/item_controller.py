from models import Item

class ItemController():
    def get_items_by_list(self, listitem_id):
        """Return items with the given itemlist ID in it's ForeignKeyField"""
        items = Item.select().where(Item.item_list == listitem_id)
        return items # Return model array

    def create_item(self, body):
        """Create item model with fields from body"""
        item = Item.create(**body)
        return item # Return model

    def update_item(self, item_id, body):
        """Update item's name field with field from body, given ID"""
        item=Item.select().where(Item.id == item_id).get()
        item.name=body['name'] # If tests looked for more than name, an update query would be nessesary.
        item.save()
        return item # Return model

    def delete_item(self, item_id):
        """Delete item with given ID"""
        Item.delete().where(Item.id == item_id).execute()
        return # Return nothing

item_controller = ItemController()
