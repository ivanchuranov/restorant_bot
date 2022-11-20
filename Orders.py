from Order import Order
class Orders:
    def __init__(self):
        self.list = []

    def add_item(self, menu_items, user, place):
        order = Order(menu_items, user, place, len(self.list) + 1)
        self.list.append(order)
        return order

    def show_orders(self):
        for order in self.list:
            print(f"{order.id}. {order.user.username}: {order.status}")