from models import ItemList

class ItemListController():
    def get_all_itemlists(self):
        return ItemList.select()

    def create_itemlist(self, body):
        return ItemList.create(
            name=body['name']
        )

    def update_itemlist(self, listitem_id, body):
        itemlist=ItemList.select().where(ItemList.id == listitem_id)
        itemlist.name=body['name']
        return itemlist

    def delete_itemlist(self, listitem_id):
        ItemList.delete().where(ItemList.id == listitem_id).execute()
        return

itemlist_controller = ItemListController()
