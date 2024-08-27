import random

random.seed(123)

pearson_table = list(range(256))
random.shuffle(pearson_table)


class Player:
    def __init__(self, uid: str, name: str) -> None:
        self._uid = uid
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def uid(self) -> str:
        return self._uid

    def __str__(self):
        return f"{self.uid}, {self.name}"

    @staticmethod
    def hash(key: str, size: int) -> int:
        hash_ = 0
        for char in key:
            hash_ = pearson_table[hash_ ^ ord(char)]
        return hash_ % size

    # https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash
    def __key(self):
        return self._uid, self._name

    def __hash__(self):
        return self.hash(self.uid, len(Player.__key(self)))

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.uid == other.uid
        return NotImplemented

