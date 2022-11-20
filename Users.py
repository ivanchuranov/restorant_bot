from User import User
class Users:
    def __init__(self):
        self.list = []

    def add_user(self, chatid, first_name, username=None, last_name=None,role='client'):
        if self.find_user(chatid) is None:
            user = User(chatid, first_name, username, last_name, role)
            self.list.append(user)
            return user
        else:
            return None

    def addUser(self, user):
        if user != None and self.find_user(user.chatid) is None:
            self.list.append(user)
            return user
        else:
            return None

    def show_users(self):
        for user in self.list:
            print(f"{user.first_name} {user.last_name}")
            print("______________________________________")
            print(f'{user.username}: {user.role}')
            print("______________________________________")
            print(f'{user.chatid}')

    def find_user(self, chatid):
        for user in self.list:
            if user.chatid == chatid:
                return user
        return None
