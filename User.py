class User:
    def __init__(self, chatid, first_name, username=None, last_name=None,role='client'):
        self.role = role
        self.chatid = chatid
        self.first_name = first_name
        self.username = username
        self.last_name = last_name
