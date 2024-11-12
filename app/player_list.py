from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.player
            current = current.next

    def push(self, player: Player) -> None:  # add node to the end of the list
        new_node = PlayerNode(player)
        if self.tail is None:  # if empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def pop(self) -> Player:  # remove node at the end of the list and return its value
        if self.tail is None:
            raise IndexError('Popping from empty list')
        removed_player = self.tail.player
        if self.head == self.tail:  # Only one element in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return removed_player

    def shift(self) -> Player:  # remove node at the beginning of the list
        if self.head is None:
            raise IndexError('Shifting from an empty list')
        removed_player = self.head.player
        if self.head == self.tail:  # Only element in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return removed_player

    def unshift(self, player) -> None:  # Add node to beginning of the list
        new_node = PlayerNode(player)
        if self.head is None:  # if empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def delete(self, uid: str) -> Player | None:  # remove the first occurrence of a node of a specified value
        current = self.head
        while current:
            if current.player.uid == uid:
                if current == self.head:
                    return self.shift()
                elif current == self.tail:
                    return self.pop()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                return
            current = current.next
        raise ValueError(f"{uid} not found in list")

    def update(self, player: Player):
        node = self.search(player.uid)
        if node:
            node.name = player.name
            return True
        return False

    def search (self, key: str) -> Player | None:
        current = self.head
        while current is not None:
            if current.player.uid == key:
                return current.player
            current = current.next
        return None

    def display(self, forward=True):
        if forward:
            current = self.head
            while current:
                print(f"Player: {current.player.name}, UID: {current.player.uid}")
                current = current.next
        else:
            current = self.tail
            while current:
                print(f"Player: {current.player.name}, UID: {current.player.uid}")
                current = current.prev

