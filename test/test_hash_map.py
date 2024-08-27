import unittest
from app.player import Player
from app.player_hash_map import PlayerHashMap


class TestHashMap(unittest.TestCase):
    def test_insertion_and_search(self):
        hash_table = PlayerHashMap(10)
        hash_table.__setitem__("123", "John")
        self.assertEqual(hash_table.__getitem__("123"), "John")

    def test_update_using_key_value(self):
        hash_table = PlayerHashMap(10)
        hash_table.__setitem__("123", "John")
        hash_table.__setitem__("123", "Bob")
        self.assertEqual(hash_table.__getitem__("123"), "Bob")

    def test_deletion(self):
        hash_table = PlayerHashMap(10)
        hash_table.__setitem__("123", "John")
        hash_table.__setitem__("456", "Bob")
        self.assertEqual(hash_table.__delitem__("456"), None)

    def test_invalid_key_value(self):
        hash_table = PlayerHashMap(10)
        hash_table.__setitem__("123", "John")
        self.assertEqual(hash_table.__getitem__("456"), "Not Found")


if __name__ == '__main__':
    unittest.main()
