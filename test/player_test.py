from app.player import (
    Player
)
import unittest


class PlayerTest(unittest.TestCase):
    def test_player_uid(self):
        player = Player(5, "abc")
        self.assertEqual(player.uid, 5)

    def test_player_name(self):
        player = Player(5, "abc")
        self.assertEqual(player.name, "abc")





