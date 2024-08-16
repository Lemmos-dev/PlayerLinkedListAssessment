import unittest

from app.player import Player
from app.player_list import (
    PlayerList
)


class PlayerListTest(unittest.TestCase):
    def test_count_empty_list(self):
        lst = PlayerList()
        self.assertEqual(len(lst), 0)

    def test_count_list_with_items(self):
        lst = PlayerList()
        lst.push(Player(123, "abc"))
        lst.push(Player(456, "def"))
        self.assertEqual(len(lst), 2)

    def test_pop_removes_from_end_of_list(self):
        lst = PlayerList()
        player1 = Player(123, "abc")
        player2 = Player(456, "def")
        lst.push(player1)
        lst.push(player2)
        self.assertEqual(lst.pop(), player2)

    def test_shift_removes_from_beginning_of_list(self):
        lst = PlayerList()
        player1 = Player(123, "abc")
        player2 = Player(456, "def")
        lst.push(player1)
        lst.push(player2)
        self.assertEqual(lst.shift(), player1)

    def test_delete_based_on_key(self):
        lst = PlayerList()
        player1 = Player(123, "abc")
        player2 = Player(456, "def")
        player3 = Player(789, "ghi")
        lst.push(player1)
        lst.push(player2)
        lst.push(player3)
        lst.delete(456)
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst.pop(), player3)
        self.assertEqual(lst.pop(), player1)

