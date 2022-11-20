from random import randint
from User import User
from Menu import Menu
from Order import Order
from Orders import Orders
from MenuItem import MenuItem
from random import choice
from DbContext import DbContext
from Logger import Logger
class Programm:
    def __init__(self):
        self.dbContext = DbContext('data')
        self.logger = Logger(__name__)

        self.commands = {
            'client': [
            {'cmd': '/help',
             'info': 'выводит информацию о всех командах'},
            {'cmd': '/surprise',
            'info': 'рандомное блюдо'},
            {'cmd': '/q',
             'info': 'выход из программы'},
            {'cmd': '/menu',
             'info': 'вывод меню'},
            {'cmd':'/order',
             'info': 'выбор заказа'}],
            'admin': [
                {'cmd': '/ban',
                 'info': 'выводит информацию о всех командах'},
                {'cmd': '/orders',
                 'info': 'выводит информацию о всех заказах'},
                {'cmd': '/add menu item',
                 'info': 'добавить предмет в меню'}
            ],
            'courier': [
                {'cmd': '/accept',
                 'info': 'принять заказ в доставку'},
                {'cmd': '/finish',
                 'info': 'завершить заказ'}],
            'manager': [
                {'cmd': '/accept',
                 'info': 'принять заказ в ресторане'}],
            'cook': [
                {'cmd': '/accept',
                 'info': 'принять заказ в готовку'}]
        }
        self.current_user = self.authorize()
        self.menu = self.dbContext.Menu()
        self.orders = Orders()

    def authorize(self):
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        chatid = randint(1, 23908)
        username = input('Введите имя пользователя: ')
        role = input('Введите роль: ')

        if role != "":
            user = User(chatid, first_name, username, last_name, role)
        else:
            user = User(chatid, first_name, username, last_name)
        return user

    def cmd_handler_help(self):
        print('Добро пожаловать в наш Restaurant Bot!')

    def cmd_handler_menu(self):
        #test
        self.menu.show_menu()

    def cmd_handler_add_menu_item(self):
        name = input('Введите название блюда: ')

        try:
            price = int(input('Введите стоимость: '))
            self.menu.add_item(price, name)
            self.dbContext.SaveData()
        except ValueError as ex:
            print('Введены не верные данные!')
            self.logger.log(ex)
            self.cmd_handler_add_menu_item()

    def cmd_handler_orders(self):
        self.orders.show_orders()

    def cmd_handler_order(self):
        menu_items = []

        while True:
            order = input('Ваш выбор: ')

            if order.lower() == 'нет':
                break

            item = self.one_handler_order(order)

            if item != None:
                menu_items.append(item)

        if len(menu_items) == 0:
            print('Вы ничего не заказали!')
            return

        self.create_order(menu_items)

    def create_order(self, menu_items):
        place = input('Введите адрес: ')

        order = self.orders.add_item(menu_items, self.current_user, place)
        self.check_sender(order)

    def one_handler_order(self, order):

        item = self.menu.find_item(order)

        if item == None:
            print('Такого блюда не сужествует! Попробуйте еще раз!')
            return None

        return item

    def check_sender(self, order):
        order.show_order()

    def cmd_handler_choice(self):
        menu_items = []
        menu_items.append(self.menu.random_menu_item())
        self.create_order(menu_items)

    def cmd_handler(self, cmd):
        cmds = self.get_users_cmds(self.current_user.role)
        result = self.check_command(cmds, cmd)

        if result:
            if cmd == '/orders':
                self.cmd_handler_orders()
            elif cmd == '/add menu item':
                self.cmd_handler_add_menu_item()

        return result
    def get_users_cmds(self, role):
        cmds = []
        cmds += self.commands['client']

        if role == 'admin':
            cmds += self.commands['admin']
            cmds += self.commands['manager']
            cmds += self.commands['cook']
            cmds += self.commands['courier']
        elif role == 'manager':
            cmds += self.commands['manager']
        elif role == 'cook':
            cmds += self.commands['cook']
        elif role == 'courier':
            cmds += self.commands['courier']

        return cmds
    def check_command(self, cmds, cmd):
        for com in cmds:
            if com["cmd"] == cmd:
                return True
        print('такой команды не существует')
        return False
    def start(self):
        while True:
            cmd = input('>>')
            if cmd == '/help':
                self.cmd_handler_help()
            elif cmd == '/q':
                break
            elif cmd == '/order':
                self.cmd_handler_order()
            elif cmd == '/surprise':
                self.cmd_handler_choice()
            elif cmd == '/menu':
                self.cmd_handler_menu()
            elif not self.cmd_handler(cmd):
                print('Такой команды не существует.')

if __name__ == '__main__':
    app = Programm()
    app.start()

