from __future__ import annotations

from app.player import Player

class PlayerBNode[T]:
    def __init__(self, value: T):
        self.value = value
        self._left: PlayerBNode[Player] | None = None
        self._right: PlayerBNode[Player] | None = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left_node) -> None:
        self._left = left_node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right_node) -> None:
        self._right = right_node

    def __lt__(self, other: PlayerBNode[T]) -> bool:
        return self.value < other.value

    def __eq__(self, other: PlayerBNode[T]) -> bool:
        return self.value == other.value

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.value})"

