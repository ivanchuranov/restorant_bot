import json
commands = {
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

with open("commands.json", "w") as file: # открываешь (или открываешь после создания) файл commands.json для записи и кладешь его в переменную file
    json.dump(commands,file)

with open('commands.json', 'r') as file:
    data = json.load(file)
    print(data['client'])