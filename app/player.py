class Player:
    def __init__(self, uid: int, name: str) -> None:
        self._uid = uid
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def uid(self):
        return self._uid

    def __str__(self):
        return f"{self.uid}, {self.name}"

    #https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash
    def __key(self):
        return self._uid, self._name

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.__key() == other.__key()
        return NotImplemented

