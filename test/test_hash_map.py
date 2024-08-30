import unittest
from app.player import Player
from app.player_hash_map import PlayerHashMap


class TestHashMap(unittest.TestCase):
    def test_initialisation(self):
        hash_map = PlayerHashMap(0)
        assert len(hash_map) == 0

    def test_insertion_and_search(self):
        hash_table = PlayerHashMap(10)
        hash_table["123"] = "John"
        self.assertEqual(hash_table["123"], "John")

    def test_update_using_key_value(self):
        hash_table = PlayerHashMap(10)
        hash_table["123"] = "John"
        hash_table["123"] = "Bob"
        self.assertEqual(hash_table["123"], "Bob")

    def test_deletion(self):
        hash_table = PlayerHashMap(10)
        hash_table["123"] = "John"
        hash_table["456"] = "Bob"
        self.assertEqual(hash_table.__delitem__("456"), None)
        self.assertEqual(hash_table.__len__(), 10)

    def test_nonexistent_key_value(self):
        hash_table = PlayerHashMap(10)
        hash_table["123"] = "John"
        self.assertEqual(hash_table["456"], "Not Found")

    def test_list_size(self):
        hash_table = PlayerHashMap(10)
        self.assertEqual(hash_table.__len__(), 10)

    def test_collision_handling(self):
        hash_table = PlayerHashMap(10)
        hash_table["key1"] = "value1"
        hash_table["key2"] = "value2"
        assert hash_table["key1"] == "value1"
        assert hash_table["key2"] == "value2"



if __name__ == '__main__':
    unittest.main()
