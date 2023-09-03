class PlayerNode:
    """
    Represents a node in a linked list that holds player information.
    """

    def __init__(self, player):
        """
        Initialize a PlayerNode with a player object and no links to other nodes.

        :param player: The player object to be stored in this node.
        """
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self):
        """
        Get the player object stored in this node.

        :return: The player object.
        """
        return self._player

    @player.setter
    def player(self, new_player):
        """
        Set a new player object for this node.

        :param new_player: The new player object to be stored.
        """
        self._player = new_player

    @property
    def next(self):
        """
        Get the next node linked to this node.

        :return: The next linked node.
        """
        return self._next

    @next.setter
    def next(self, new_next):
        """
        Set a new next node for this node.

        :param new_next: The new next node to be linked.
        """
        self._next = new_next

    @property
    def previous(self):
        """
        Get the previous node linked to this node.

        :return: The previous linked node.
        """
        return self._previous

    @previous.setter
    def previous(self, new_previous):
        """
        Set a new previous node for this node.

        :param new_previous: The new previous node to be linked.
        """
        self._previous = new_previous

    @property
    def key(self):
        """
        Get the key (UID) associated with the player in this node.

        :return: The UID of the player.
        """
        return self._player.uid

    def __str__(self):
        """
        Get a string representation of the PlayerNode.

        :return: A string representation of the node containing UID and player name.
        """
        return f"PlayerNode: UID: {self.key}, Name: {self._player.name}"
