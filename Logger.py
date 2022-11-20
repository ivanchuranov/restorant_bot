from datetime import datetime

class Logger:
    def __init__(self, type):
        self.type = type

    def log(self, message):
        print(f"\t\t\t-> {message}")
        self.write(message)

    def write(self, message):
        with open('log.txt', 'a') as file:
            file.write(f'{type} : {datetime.utcnow()} : {message}\n')