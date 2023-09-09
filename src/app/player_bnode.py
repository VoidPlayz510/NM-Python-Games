from app.player import Player


class PlayerBNode:

    def __init__(self, player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, new):
        self._left = new

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, new):
        self._right = new
