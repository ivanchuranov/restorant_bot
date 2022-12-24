class Many_To_Many:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.list = []
    def Samurai(self,id,name):
        samurai = [{id: name}]
    def BattleSamurai(self):
        pass
    def Battle(self):
        pass
    def add_user(self, many):
        if many is not None:
            foundMany = self.find_many_manyid(many.manyid)
            if foundMany == None:
                self.list.append(many)

    def find_many_manyid(self, manyid):
        index = self.find_many_index_in_list(manyid)

        if index is not None:
            return self.list[index]
        else:
            return None
    def find_many_index_in_list(self, manyid):
        for i in range(len(self.list)):
            if self.list[i].manyid == manyid:
                return i
        return None