class Order:
    def __init__(self, menu_items, user, place, id):
        self.STATUSES = ['Подтверждение заказа', 'готовится', 'готов', 'выдан курьеру', 'заказ получен']
        self.user = user
        self.menu_items = menu_items
        self.place = place
        self.status = 0
        self.id = id

    def change_status(self):
        if self.status <= 3:
            self.status += 1

    def check_sum_order(self):
        sum = 0
        for item in self.menu_items:
            sum += item.price
        return sum

    def show_order(self):
        n = 1
        for item in self.menu_items:
            print(f'{n}.{item.name} - {item.price} рублей')
            n += 1
        print(f"Итого: {self.check_sum_order()} рублей")