from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Player:
    """
    Represents a player with a unique identifier (uid) and a name.
    """

    def __init__(self, uid, name):
        """
        Initializes a Player instance with a unique identifier and a name.

        :param uid: Unique identifier for the player.
        :param name: Name of the player.
        """
        self._uid = uid
        self._name = name
        self._password_hash = None

    @property
    def uid(self):
        """
        Get the unique identifier of the player.

        :return: The unique identifier (uid).
        """
        return self._uid

    @property
    def name(self):
        """
        Get the name of the player.

        :return: The name of the player.
        """
        return self._name

    def __str__(self):
        """
        Get a string representation of the Player instance.

        :return: A string containing the unique identifier and name of the player.
        """
        return f'GUID is {self.uid}, player\'s name is {self.name}'

    def add_password(self, password):
        """
        Hashes and stores the player's password securely.

        :param password: The password to be hashed and stored.
        """
        ph = PasswordHasher()
        self._password_hash = ph.hash(password)

    def verify_password(self, password):
        """
        Verify if a given password matches the stored password hash.

        :param password: The password to be verified.

        :return: True if the password is verified, False otherwise.
        """
        ph = PasswordHasher()
        try:
            ph.verify(self._password_hash, password)
            return True
        except VerifyMismatchError as e:
            print(f"Password verification failed: {e}")
            return False
