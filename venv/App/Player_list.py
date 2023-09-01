from App.Player_node import PlayerNode
class PlayerList:
    def __init__(self):
        self.head = None # Initally there are no elements in the list
        self.tail = None

    def push_front(self, new):  # Adding an element before the first element
        new_node = PlayerNode(new)  # new node
        new_node.next = self.head

        if self.head != None:  # Checks whether list is empty or not
            self.head.prev = new_node  # old head's previous value to new player node
            self.head = new_node  # new node becomes the new head
            new_node.prev = None

        else:  # If list is blank, make new node head and tail
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

    def is_empty(self):
        return self.head is None and self.tail is None