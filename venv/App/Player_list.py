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

    def push_end(self, new):
        # add to tail
        new_node = PlayerNode(new)
        new_node.prev = self.tail

        # is list empty
        if new_node.prev == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None # first previous has to be null now
        else:  # If list is not empty, change values accordingly
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node  # Make new node the new end tail

    def is_empty(self):
        return self.head is None and self.tail is None

    def peek_back(self):  # returns last element
        if self.tail == None:  # checks whether list is empty or not
            print("List is empty")
        else:
            return self.tail.player