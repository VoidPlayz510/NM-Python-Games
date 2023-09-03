
class PlayerList:
    """
    A doubly linked list to manage players.
    """

    def __init__(self):
        """
        Initialize an empty PlayerList with head and tail set to None.
        """
        self.head = None
        self.tail = None

    def push_front(self, new):
        """
        Add a player to the front of the list.

        :param new: The player to be added.
        """
        new_node = PlayerNode(new)
        new_node.next = self.head

        if self.head is not None:
            self.head.previous = new_node
            self.head = new_node
            new_node.previous = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.previous = None

    def push_end(self, new):
        """
        Add a player to the end of the list.

        :param new: The player to be added.
        """
        new_node = PlayerNode(new)
        new_node.previous = self.tail

        if new_node.previous is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    def is_empty(self):
        """
        Check if the list is empty.

        :return: True if the list is empty, False otherwise.
        """
        return self.head is None and self.tail is None

    def peek_front(self):
        """
        Get the player at the front of the list without removing them.

        :return: The player at the front of the list.
        """
        if self.head is None:
            print("List is empty")
        else:
            return self.head.player

    def peek_back(self):
        """
        Get the player at the back of the list without removing them.

        :return: The player at the back of the list.
        """
        if self.tail is None:
            print("List is empty")
        else:
            return self.tail.player

    def pop_front(self):
        """
        Remove and return the player at the front of the list.

        :return: The removed player.
        """
        if self.head is None:
            print("List is empty")
            return None

        if self.head == self.tail:
            removed_player = self.head.player
            self.head = None
            self.tail = None
            return removed_player
        else:
            temp = self.head
            temp.next.previous = None
            self.head = temp.next
            temp.next = None
            return temp.player

    def pop_end(self):
        """
        Remove and return the player at the end of the list.

        :return: The removed player.
        """
        if self.tail is None:
            print("List is empty")
        else:
            temp = self.tail
            temp.previous.next = None
            self.tail = temp.previous
            temp.previous = None
            return temp.player

    def pop_key(self, target_uid):
        """
        Remove a player with a specific UID from the list.

        :param target_uid: The UID of the player to be removed.
        """
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        while current is not None and current.player.uid != target_uid:
            previous = current
            current = current.next

        if current is not None:
            if previous is not None:
                previous.next = current.next
            else:
                self.head = current.next
            if current == self.tail:
                self.tail = previous
        else:
            print(f"Player UID {target_uid} not found in the list")

    def display_list(self, forward=True):
        """
        Display the list of players in either forward or reverse order.

        :param forward: True to display in forward order, False to display in reverse order.
        """
        if forward:
            current = self.head
            while current:
                print(f"Player ID: {current.player.uid}, Name: {current.player.name}")
                current = current.next
        else:
            current = self.tail
            while current:
                print(f"Player ID: {current.player.uid}, Name: {current.player.name}")
                current = current.previous
