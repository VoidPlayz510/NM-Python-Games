from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Player:
    """
    Represents a player with a unique identifier (uid) and a name.
    """
    _player_list = []

    def __init__(self, uid, name):
        """
        Initializes a Player instance with a unique identifier and a name.

        :param uid: Unique identifier for the player.
        :param name: Name of the player.
        """
        self._uid = uid
        self._name = name
        self._password_hash = None
        self._score = None

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

    @property
    def score(self):
        """
        Get the score of the player.

        :return: The score of the player.
        """
        return self._score

    @score.setter
    def score(self, new_score):
        """
        Set a new score for the player.

        :param new_score: The new player score to be stored.
        :raises ValueError: If the new_score is not a positive integer.
        """
        if isinstance(new_score, int) and new_score > 0:
            self._score = new_score
            self._player_list.append(new_score)
        else:
            raise ValueError("Score must be a positive integer")

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

    @staticmethod
    def clear_list():
        Player._player_list.clear()

    @staticmethod
    def sort_list(array):
        """
        Sorts the given list using the merge sort algorithm.

        :param array: The list to be sorted.

        :return: The newly sorted list.
        """
        if len(array) <= 1:
            return array

        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        left = Player.sort_list(left)
        right = Player.sort_list(right)

        return Player.merge(left, right)

    @staticmethod
    def merge(left, right):
        """
        Merges two sorted lists into a single sorted list.

        :param left: The left half of the list.
        :param right: The right half of the list.

        :return: The merged and sorted list.
        """
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def __str__(self):
        """
        Get a string representation of the Player instance.

        :return: A string containing the unique identifier and name of the player.
        """
        return f'GUID is {self.uid}, player\'s name is {self.name}'

    def __eq__(self, other):
        """
        Compare two Player instances for equality based on score.

        :param other: Another Player instance to compare.
        :return: True if the scores are equal, False otherwise.
        """
        if isinstance(other, Player):
            return self.score == other.score
        return False

    def __ge__(self, other):
        """
        Compare two Player instances for greater than or equal based on score.

        :param other: Another Player instance to compare.
        :return: True if the score is greater than or equal, False otherwise.
        """
        if isinstance(other, Player):
            return self.score >= other.score
        return False

    def __gt__(self, other):
        """
        Compare two Player instances for greater than based on score.

        :param other: Another Player instance to compare.
        :return: True if the score is greater, False otherwise.
        """
        if isinstance(other, Player):
            return self.score > other.score
        return False

    def __le__(self, other):
        """
        Compare two Player instances for less than or equal based on score.

        :param other: Another Player instance to compare.
        :return: True if the score is less than or equal, False otherwise.
        """
        if isinstance(other, Player):
            return self.score <= other.score
        return False

    def __lt__(self, other):
        """
        Compare two Player instances for less than based on score.

        :param other: Another Player instance to compare.
        :return: True if the score is less, False otherwise.
        """
        if isinstance(other, Player):
            return self.score < other.score
        return False

