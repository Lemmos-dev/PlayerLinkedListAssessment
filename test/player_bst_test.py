import unittest

from app.player_bst import PlayerBST
from app.player import Player


class TestBST(unittest.TestCase):
    def test_initialisation(self):
        bst = PlayerBST()
        assert bst.root is None

    def test_insertion(self):
        bst = PlayerBST()
        player = Player("123", "John", 10)
        player2 = Player("456", "Bob", 5)
        player3 = Player("789", "Ryan", 15)
        bst.insert(player.name)
        bst.insert(player2.name)
        bst.insert(player3.name)
        assert bst.root.value == player.name
        assert bst.root.left.value == player2.name
        assert bst.root.right.value == player3.name

    def test_search(self):
        bst = PlayerBST()
        player = Player("123", "John", 10)
        player2 = Player("456", "Bob", 5)
        player3 = Player("789", "Ryan", 15)
        bst.insert(player.name)
        bst.insert(player2.name)
        bst.insert(player3.name)
        assert bst.search(player.name).value == player.name
        assert bst.search(player2.name).value == player2.name
        assert bst.search(player3.name).value == player3.name
        assert bst.search("test") is None

    def test_balance(self):
        bst = PlayerBST()
        player = Player("123", "John", 10)
        player2 = Player("456", "Bob", 5)
        player3 = Player("789", "Ryan", 15)
        bst.insert(player.name)
        bst.insert(player2.name)
        bst.insert(player3.name)
        #TODO: Implement function in player_bst that checks if the tree is balanced
