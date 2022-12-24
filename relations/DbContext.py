from Many_To_Many import Many_To_Many
from One_To_Many import One_To_Many
from One_To_One import One_To_One

import json
class DbContext:
    def __init__(self, connection):
        self.connection = connection
        self.LoadData()
        self.many_to_many = Many_To_Many()
        self.one_to_many = One_To_Many()
        self.one_to_one = One_To_One()
    def many_to_many(self):
        self.LoadData()
        return self.many_to_many
    def many_to_one(self):
        self.LoadData()
        return self.many_to_one

    def DeserializeManyToMany(self, data):
        list = []
        for item in data['many_to_many']:
            item = Many_To_Many(item["id"],item["name"])
            list.append(item)
        return list
    def DeserializeOneToMany(self, data):
        list = []
        for item in data['many_to_one']:
            item = One_To_Many(item["user"], item["currency"], item["currency_"], item["_currency"])
            list.append(item)
        return list
    def DeserializeOneToOne(self, data):
        list = []
        for item in data['one_to_one']:
            item = One_To_One(One_To_One["user"], One_To_One["role"])
            list.append(item)
        return list
    def SerializeManyToMany(self, data):
        many = []
        for item in data:
            dict = {
                "id": Many_To_Many.id,
                "name": Many_To_Many.name,
            }
            many.append(dict)

        return {"many": many}

    def SerializeOneToMany(self, data):
        one = []
        for item in data:
            dict = {
                "user": One_To_Many.user,
                "current": One_To_Many.current,
                "_current": One_To_Many._current,
                "current_": One_To_Many.current_,
            }
            one.append(dict)

        return {"many": one}
    def SerializeOneToOne(self, data):
        one = []
        for item in data:
            dict = {
                "user": Many_To_Many.user,
                "role": Many_To_Many.role,
            }
            one.append(dict)

        return {"one": one}
    def LoadData(self):
        with open(f"{self.connection}/ManyToMany.json", "r", encoding='windows-1251') as file:
            self.many_to_many.list = self.DeserializeManyToMany(json.load(file))
        with open(f"{self.connection}/OneToMany.json", "r", encoding='windows-1251') as file:
            self.one_to_many.list = self.DeserializeOneToMany(json.load(file))
        with open(f"{self.connection}/OneToOne.json", "r", encoding='windows-1251') as file:
            self.one_to_one.list = self.DeserializeOneToOne(json.load(file))
    def SaveData(self):
        with open(f"{self.connection}/ManyToMany.json", "w") as file:
            json.dump(self.SerializeManyToMany(self.Many_To_Many().list), file, indent=2, ensure_ascii=False)
        with open(f"{self.connection}/OneToMany.json", "w") as file:
            json.dump(self.SerializeOneToMany(self.One_To_Many.list), file, indent=2, ensure_ascii=False)
        with open(f"{self.connection}/OneToOne.json", "w") as file:
            json.dump(self.SerializeOneToOne(self.One_to_One.list), file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    db = DbContext('data')
    many = db.ManyToMany()
    Many_To_Many.add_user(Many_To_Many(1,2,3,4))
    db.SaveData()

