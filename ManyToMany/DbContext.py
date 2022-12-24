import json

from Samurai import Samurai
from Battle import Battle
from BattleSamurai import BattleSamurai
class DbContext:
    def __init__(self, connection):
        self.connection = connection
        self.samuraies = []
        self.battles_samuraies = []
        self.battles = []
        self.LoadData()

    def Samuraies(self):
        self.LoadData()
        return self.samuraies

    def Battles(self):
        self.LoadData()
        return self.battles

    def SerializeSumaraies(self, data):
        samuraies = []
        for samurai in data:
            dict = {
                "id": samurai.id,
                "name": samurai.name,
            }
            samuraies.append(dict)
        return {"samuraies": samuraies}

    def SerializeBattleSumaraies(self,data):
        battle_samuraies = []
        for battle_samurai in data:
            dict = {
                "samurai_id": battle_samurai.samurai_id,
                "battle_id": battle_samurai.battle_id,
            }
            battle_samuraies.append(dict)
        return {"battle_samuraies": battle_samuraies}

    def SerializeBattles(self,data):
        battles = []
        for battle in data:
            dict = {
                "id": battle.id,
                "name": battle.name,
            }
            battle.append(dict)
        return {"battles": battles}

    def DeserializeSumaraies(self,data):
        list = []
        for samurai in data['samuraies']:
            samurai = Samurai(samurai["id"], samurai["name"])
            list.append(samurai)
        return list

    def DeserializeBattleSumaraies(self,data):
        list = []
        for battle_samurai in data['battle_samuraies']:
            battle_samurai = BattleSamurai(battle_samurai["samurai_id"], battle_samurai["battle_id"])

            for samurai in self.samuraies:
                if samurai.id == battle_samurai.samurai_id:
                    for battle in self.battles:
                        if battle.id == battle_samurai.battle_id:
                            samurai.battles.append(battle)
                            battle.samuraies.append(samurai)

            list.append(battle_samurai)
        return list

    def DeserializeBattles(self,data):
        list = []
        for battle in data['battles']:
            battle = Battle(battle["id"], battle["name"])
            list.append(battle)
        return list


    def LoadData(self):
        with open(f"{self.connection}/Samuraies.json", "r", encoding='windows-1251') as file:
            self.samuraies = self.DeserializeSumaraies(json.load(file))
        with open(f"{self.connection}/Battles.json", "r", encoding='windows-1251') as file:
            self.battles = self.DeserializeBattles(json.load(file))
        with open(f"{self.connection}/BattlesSamuraies.json", "r", encoding='windows-1251') as file:
            self.battles_samuraies = self.DeserializeBattleSumaraies(json.load(file))

    def SaveData(self):
        with open(f"{self.connection}/Samuraies.json", "w") as file:
            json.dump(self.SerializeSumaraies(self.samuraies), file, indent=2, ensure_ascii=False)
        with open(f"{self.connection}/BattleSamuraies.json", "w") as file:
            json.dump(self.SerializeBattleSumaraies(self.battles_samuraies), file, indent=2, ensure_ascii=False)
        with open(f"{self.connection}/Battles.json", "w") as file:
            json.dump(self.SerializeBattles(self.battles), file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    db = DbContext("data")
    print(db.Samuraies()[0].battles)
    print(db.Samuraies()[1].battles)
    print(db.Battles()[0].samuraies)