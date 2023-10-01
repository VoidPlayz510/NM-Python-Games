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
            pass

        return node

    def search(self, player_name):
        return self._search_recursive(self._root, player_name)

    def _search_recursive(self, node, player_name):
        if node is None or node.key == player_name:
            return node

        if player_name < node.key:
            return self._search_recursive(node.left, player_name)
        else:
            return self._search_recursive(node.right, player_name)
