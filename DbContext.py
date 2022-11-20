import json
from User import User
from Users import Users
from Menu import Menu
from MenuItem import MenuItem
class DbContext:
    def __init__(self, connection):
        self.connection = connection
        self.menu = Menu()
        self.users = Users()

    def Menu(self):
        self.LoadData()
        return self.menu

    def Users(self):
        self.LoadData()
        return self.users

    def LoadData(self):
        with open(f"{self.connection}/Users.json", "r", encoding='windows-1251') as file: # encoding - кодировка в которой читаем ( у тебя windows-1251 - русские символы)ы
            self.DeserializeUsers(json.load(file))
        with open(f"{self.connection}/Menu.json", "r", encoding='windows-1251') as file:
            self.DeserializeMenu(json.load(file))

    def DeserializeMenu(self, data):
        for menu in data['menu']:
            self.menu.add_item(menu["price"], menu["name"])

    def SerializeMenu(self, data):
        menu = []
        for menu_item in data:
            dict = {
                "name": menu_item.name,
                "price": menu_item.price,
            }
            menu.append(dict)

        data = {"menu": menu}
        return data

    def DeserializeUsers(self, data):
        for user in data['users']:
            _user = User(user['chatid'], user['first_name'], user['username'], user['last_name'],user['role'])
            self.users.addUser(_user)

    def SerializeUsers(self, data):
        users = []

        for user in data:
            dict = {
                    "role": user.role,
                    "chatid": user.chatid,
                    "first_name": user.first_name,
                    "username": user.username,
                    "last_name": user.last_name
                  }
            users.append(dict)

        data = {"users": users}
        return data

    def SaveData(self):
        with open(f"{self.connection}/Users.json", "w") as file:
            json.dump(self.SerializeUsers(self.users.list), file, indent=2, ensure_ascii=False)  # указываем что необходимо открывать кодировкой по умолчанию на компьютереы
        with open(f"{self.connection}/Menu.json", "w") as file:
            json.dump(self.SerializeMenu(self.menu.list), file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    db = DbContext("data")
    print(db.Users().list[0].username)

    users = db.Users()
    users.addUser(User(128, "dfsf"))
    db.SaveData()

    print(db.Menu().list[0].name)

    menu = db.Menu()
    menu.add_item(500, "candle")
    db.SaveData()