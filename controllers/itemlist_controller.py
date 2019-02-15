from models import ItemList

class ItemListController():
    def get_all_itemlists(self):
    	"""Return model array of itemlists"""
        return ItemList.select() # Return model array

    def get_itemlist(self, listitem_id):
    	"""Return itemlist with given ID"""
        itemlist = ItemList.select().where(ItemList.id == listitem_id).get()
        return itemlist # Return model

    def create_itemlist(self, body):
    	"""Create itemlist model with fields from body"""
        itemlist = ItemList.create(**body)
        return itemlist # Return model

    def update_itemlist(self, listitem_id, body):
    	"""Update itemlist's name field with field from body, given ID"""
        itemlist=ItemList.select().where(ItemList.id == listitem_id).get()
        itemlist.name=body['name'] # If tests looked for more than name, an update query would be nessesary.
        itemlist.save()
        return itemlist # Return model

    def delete_itemlist(self, listitem_id):
    	"""Delete itemlist with given ID"""
        ItemList.delete().where(ItemList.id == listitem_id).execute()
        return # Return nothing

itemlist_controller = ItemListController()
