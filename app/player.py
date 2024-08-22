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

    def hash(cls, key: str) -> int:
        #Build own hash
        return hash("asd")

    #https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash
    def __key(self):
        return self._uid, self._name

    def __hash__(self):
        return self.hash(self.uid) #hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.uid == other.uid #self.__key() == other.__key()
        return NotImplemented

