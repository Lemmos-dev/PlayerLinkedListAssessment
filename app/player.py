class Player:
    def __init__(self, uid: int, name: str) -> None:
        self._uid = uid
        self._name = name

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, new_name):
    #     self.name = new_name

    @property
    def uid(self):
        return self._uid

    # @uid.setter
    # def uid(self, new_uid):
    #     self.uid = new_uid

    def __str__(self):
        return f"{self.uid}, {self.name}"

