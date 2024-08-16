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

