from MenuItem import MenuItem
from random import choice
class Menu:
    def __init__(self, isTestMenu=False):
        self.list = []

        if isTestMenu:
            self.generate_menu()

    def generate_menu(self):
        self.add_item(500, 'ApplePie')
        self.add_item(1000, 'Cake')
        self.add_item(1500, 'Pie')

    def add_item(self, price, name):
        if self.find_item(name) is None:
            menu = MenuItem(price, name)
            self.list.append(menu)
            return menu
        else:
            return None

    def find_item(self, name):
        for menuItem in self.list:
            if menuItem.name == name:
                return menuItem
        return None

    def random_menu_item(self):
        return choice(self.list)

    def show_menu(self):
        for i in range(len(self.list)):
            print(f'{i+1}. {self.list[i].name} - {self.list[i].price}')

# Подтверждение заказа -> готовится -> готов -> выдан курьеру -> заказ получен
#          0                 1           2           3                4