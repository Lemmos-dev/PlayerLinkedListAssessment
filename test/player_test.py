from app.player import (
    Player
)
import unittest


class PlayerTest(unittest.TestCase):
    def test_player_uid(self):
        player = Player("5", "abc")
        self.assertEqual(player.uid, "5")

    def test_player_name(self):
        player = Player("5", "abc")
        self.assertEqual(player.name, "abc")

    def test_equal_score_and_not_equal(self):
        player = Player("123", "John", 1234)
        player2 = Player("456", "Bob", 1234)
        self.assertEqual(player == player2, True)
        player2.score = 5678
        self.assertEqual(player == player2, False)

    def test_greater_than(self):
        player = Player("123", "John", 1235)
        player2 = Player("456", "Bob", 1234)
        self.assertEqual(player >= player2, True)
        player2.score = 5678
        self.assertEqual(player >= player2, False)
        player2.score = 1235
        self.assertEqual(player >= player2, True)

    def test_sorting_list(self):
        players = [
            Player("1", "John", 1234),
            Player("2", "Bob", 5678),
            Player("3", "Ryan", 100),
            Player("4", "Dylan", 3333),
            Player("5", "Andrew", 7),
        ]
        sorted_players = Player.quicksort(players)
        self.assertEqual(sorted_players, sorted(players, key=lambda player: player.score, reverse=True))