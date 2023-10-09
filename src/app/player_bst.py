from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        """
        Initialize an empty binary search tree for players.
        """
        self._root = None

    @property
    def root(self):
        """
        Get the root element of the BST.

        :return: The root node.
        """
        return self._root

    def is_empty(self):
        """
        Check if the BST is empty.

        :return: True if the BST is empty, otherwise False.
        """
        return self._root is None

    def insert(self, player):
        """
        Insert a player into the BST.

        :param player: The player object to insert.
        """
        self._root = self._insert_recursive(self._root, player)

    def _insert_recursive(self, node, player):
        """
        Recursively insert a player into the BST.

        :param node: The current node in the recursion.
        :param player: The player object to insert.
        :return: The updated node after insertion.
        """
        if node is None:
            return PlayerBNode(player)

        if player.name < node.key:
            node.left = self._insert_recursive(node.left, player)
        elif player.name > node.key:
            node.right = self._insert_recursive(node.right, player)

        return node

    def search(self, player_name):
        """
        Search for a player in the BST by name.

        :param player_name: The name of the player to search for.
        :return: The player node if found, otherwise None.
        """
        return self._search_recursive(self._root, player_name)

    def _search_recursive(self, node, player_name):
        """
        Recursively search for a player in the BST by name.

        :param node: The current node in the recursion.
        :param player_name: The name of the player to search for.
        :return: The player node if found, otherwise None.
        """
        if node is None or node.key == player_name:
            return node

        if player_name < node.key:
            return self._search_recursive(node.left, player_name)
        else:
            return self._search_recursive(node.right, player_name)

    def sorted_list_to_balanced_bst(self, sorted_list):
        """
        Convert a sorted list of players into a balanced BST.

        :param sorted_list: The sorted list of players.
        :return: The root node of the balanced BST.
        """
        if not sorted_list:
            return None

        middle_index = len(sorted_list) // 2
        middle_node = PlayerBNode(sorted_list[middle_index].player)
        middle_node.left = self.sorted_list_to_balanced_bst(sorted_list[:middle_index])
        middle_node.right = self.sorted_list_to_balanced_bst(sorted_list[middle_index + 1:])

        return middle_node

    def create_balanced_bst(self):
        """
        Create a balanced BST from the current BST.

        This method reorders the current BST to make it balanced.
        """
        sorted_elements = []
        self.inorder_traversal(self.root, sorted_elements)
        self._root = self.sorted_list_to_balanced_bst(sorted_elements)

    def inorder_traversal(self, node, result):
        """
        Perform an inorder traversal of the BST.

        :param node: The current node in the traversal.
        :param result: A list to store the traversal result.
        """
        if node is not None:
            self.inorder_traversal(node.left, result)
            result.append(node)
            self.inorder_traversal(node.right, result)

    def is_balanced(self):
        """
        Check if the BST is balanced.

        :return: True if the BST is balanced, otherwise False.
        """
        return self._is_balanced_recursive(self._root)

    def _is_balanced_recursive(self, node):
        """
        Recursively check if the BST is balanced.

        :param node: The current node in the recursion.
        :return: A tuple (balanced, height) where 'balanced' is True if the subtree is balanced,
                 and 'height' is the height of the subtree.
        """
        if node is None:
            return True, 0

        left_balanced, left_height = self._is_balanced_recursive(node.left)
        right_balanced, right_height = self._is_balanced_recursive(node.right)

        balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
        )

        height = max(left_height, right_height) + 1

        return balanced, height
