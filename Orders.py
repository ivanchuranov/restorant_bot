from Order import Order
class Orders:
    def __init__(self):
        self.list = []

    def add_item_(self,order):
        self.list.append(order)
        return order
    def add_item(self, menu_items, user, place):
        order = Order(menu_items, user, place, len(self.list) + 1)
        return self.add_item_(order)

    def show_orders(self):
        for order in self.list:
            print(f"{order.id}. {order.chatid}: {order.status}")