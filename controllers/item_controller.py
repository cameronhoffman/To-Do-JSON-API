from models import Item

class ItemController():
    def get_items_by_list(self, listitem_id):
        return Item.select().where(Item.item_list == listitem_id)

    def create_item(self, body):
    	return Item.create(
                name=body['name'],
                item_list=body['item_list'],
                is_complete=body['is_complete']
    		)

item_controller = ItemController()
