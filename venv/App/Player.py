class Player:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'GUID is {self.uid}, players\'s name is {self.name}'



# player = Player(uid=123, name='Alice')
# print(player)