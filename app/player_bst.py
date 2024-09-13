from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST[T]:
    def __init__(self):
        self.root: PlayerBNode[T] | None = None

    def insert(self, value: Player.name, current_node: PlayerBNode) -> None:
        # Insert a new node in the appropriate available list
        if current_node and self.root is None:
            raise ValueError("Cannot pass a node when root is not set")

        if self.root is None:
            self.root = PlayerBNode(value)
            return
        current_node = current_node or self.root

        if value < current_node.value:
            if current_node.left is None:
                current_node.left = PlayerBNode(value)
                return
            self.insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = PlayerBNode(value)
                return
            self.insert(value, current_node.right)
        else:
            # Must not have duplicate nodes
            ...

    def search(self, name: Player.name, root: PlayerBNode[T]) -> PlayerBNode | None:
        if root is None:
            return root
        if root.value == name:
            return root
        elif root.value < name:
            return self.search(name, root.left)
        elif root.value > name:
            return self.search(name, root.right)
