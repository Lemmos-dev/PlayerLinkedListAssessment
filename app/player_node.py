from app.player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self.prev = None
        self.next = None

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.player}, {self.prev}, {self.next})"

