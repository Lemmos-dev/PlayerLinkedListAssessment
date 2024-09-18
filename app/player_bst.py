from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST[T]:
    def __init__(self):
        self.root: PlayerBNode[T] | None = None

    def insert(self, value: Player.name) -> None:
        # Insert a new node in the appropriate available list
        if self.root is None:
            self.root = PlayerBNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: Player.name, current_node: PlayerBNode) -> None:
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = PlayerBNode(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = PlayerBNode(value)
            else:
                self._insert(value, current_node.right)


    def search(self, name: Player.name):
        return self._search(name, self.root)

    def _search(self, name: Player.name, root: PlayerBNode) -> PlayerBNode | None:
        if root is None:
            return root
        if root.value == name:
            return root
        elif name < root.value:
            return self._search(name, root.left)
        elif name > root.value:
            return self._search(name, root.right)
