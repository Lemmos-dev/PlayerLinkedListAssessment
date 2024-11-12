import unittest
from app.player_hash_map import PlayerHashMap


class TestHashMap(unittest.TestCase):
    def test_initialisation(self):
        hash_map = PlayerHashMap(0)
        assert len(hash_map) == 0

    def test_insertion_and_search(self):
        self.hash_table = PlayerHashMap(10)
        self.hash_table["123"] = "John"
        player = self.hash_table["123"]
        self.assertEqual(player.name, "John")

    def test_update_using_key_value(self):
        hash_table = PlayerHashMap(10)
        hash_table["123"] = "John"
        hash_table["123"] = "Bob"
        player = hash_table["123"]
        self.assertEqual(player.name, "Bob")

    def test_deletion_and_deletion_of_nonexistent(self):
        hash_table = PlayerHashMap(10)
        hash_table["123"] = "John"
        hash_table["456"] = "Bob"

        with self.assertRaises(ValueError):
            del hash_table["789"]

        self.assertEqual(hash_table.__delitem__("123"), None)
        self.assertEqual(hash_table.__len__(), 10)

    def test_nonexistent_key_value(self):
        hash_table = PlayerHashMap(10)
        hash_table["123"] = "John"
        self.assertEqual(hash_table["456"], None)

    def test_list_size(self):
        hash_table = PlayerHashMap(10)
        self.assertEqual(hash_table.__len__(), 10)

    def test_collision_handling(self):
        #I don't think this is correctly testing collisions
        hash_table = PlayerHashMap(10)
        hash_table["key1"] = "value1"
        hash_table["key2"] = "value2"
        player = hash_table["key1"]
        player2 = hash_table["key2"]
        self.assertEqual(player.name, "value1")
        self.assertEqual(player2.name, "value2")



if __name__ == '__main__':
    unittest.main()
