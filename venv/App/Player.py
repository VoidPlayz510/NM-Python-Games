from argon2 import PasswordHasher

class Player:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name
        self.__password_hash = None

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'GUID is {self.uid}, players\'s name is {self.name}'

    def add_password(self, password):
        # Initialize the PasswordHasher
        ph = PasswordHasher()

        # Hash the password
        self.__password_hash = ph.hash(password)
    def verify_password(self, password):
        # Initialize the PasswordHasher
        ph = PasswordHasher()

        # Test the provided password against the stored hash/password
        try:
            return ph.verify(self.__password_hash, password)
        except Exception: # catch an error
            return False

# player = Player(uid=123, name='Alice')
# print(player)