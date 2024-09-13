from app.player import Player

class PlayerBNode[Player]:
    def __init__(self, value: Player):
        self.value = value
        self.left: PlayerBNode[Player] | None = None
        self.right: PlayerBNode[Player] | None = None

    @property
    def left(self):
        return self.left

    @left.setter
    def left(self, left_node) -> None:
        self.left = left_node

    @property
    def right(self):
        return self.right

    @right.setter
    def right(self, right_node) -> None:
        self.right = right_node

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.value})"

