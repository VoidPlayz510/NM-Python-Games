from App.Player import Player

class PlayerNode:
    def __init__(self, player):
        self._player = player  # adding an element to the node
        self._next = None  # Initally this node will not be linked with any other node
        self._prev = None  # It will not be linked in either direction

    # Player Property
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        self._player = new_player

    # Next Property
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next

    # Prev Property
    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, new_prev):
        self._prev = new_prev

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"PlayerNode: UID: {self.key}, Name: {self._player.name}"
