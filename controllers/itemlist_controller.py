from models import ItemList

class ItemListController():
    def get_all_itemlists(self):
        return ItemList.select()

    def create_itemlist(self, body):
        return ItemList.create(
            name=body['name']
        )

itemlist_controller = ItemListController()
