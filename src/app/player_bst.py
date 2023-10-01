from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    def insert(self, player):
        self._root = self._insert_recursive(self._root, player)

    def _insert_recursive(self, node, player):
        if node is None:
            return PlayerBNode(player)

        if player.name < node.key:
            node.left = self._insert_recursive(node.left, player)
        elif player.name > node.key:
            node.right = self._insert_recursive(node.right, player)
        else:
            # Node with the same key already exists, handle accordingly
            # You can choose to update the value or handle it in a way that suits your application
            pass

        return node

