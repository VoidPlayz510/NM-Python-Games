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

    def peek_front(self):
        if self.head == None:  # checks whether list is empty or not
            print("List is empty")
        else:
            return self.head.player

    def peek_back(self):  # returns last element
        if self.tail == None:  # checks whether list is empty or not
            print("List is empty")
        else:
            return self.tail.player

    def pop_front(self):
        # Check if the list is empty
        if self.head is None:
            print("List is empty")
            return None

        # Handle the case where there's only one element in the list
        if self.head == self.tail:
            removed_player = self.head.player
            self.head = None
            self.tail = None
            return removed_player
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            return temp.player

    def pop_end(self):
        # check if list is empty
        if self.tail == None:
            print("List is empty")
        else:
            temp = self.tail
            temp.prev.next = None  # next value for old tail
            self.tail = temp.prev  # make the tail previous value the new tail
            temp.prev = None  # removes previous value of new tail
            return temp.player

    def pop_key(self, target_uid):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None

        # Iterate through the list
        while current is not None and current.player.uid != target_uid:
            prev = current
            current = current.next

        # If the node with the target UID is found, remove it
        if current is not None:
            if prev is not None:
                prev.next = current._next
            else:
                self.head = current._next
            if current == self.tail:
                self.tail = prev
        else:
            print(f"Player UID {target_uid} not found in the list")

    def display_list(self, forward=True):
        if forward:
            current = self.head  # Start from the head
            while current:
                print(f"Player ID: {current.player.uid}, Name: {current.player.name}")
                current = current.next  # Move to the next node
        else:
            current = self.tail  # Start from the tail for reverse traversal
            while current:
                print(f"Player ID: {current.player.uid}, Name: {current.player.name}")
                current = current.prev  # Move to the previous node
