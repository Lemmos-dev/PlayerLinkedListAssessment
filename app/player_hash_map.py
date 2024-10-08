from app.player import Player
from app.player_list import PlayerList


#references used:
# https://www.geeksforgeeks.org/hash-map-in-python/
# https://amiaynarayan.medium.com/hash-table-linked-list-implementation-5afcee05eafe
class PlayerHashMap:
    # create empty player list of given size
    def __init__(self, size):
        self.size = size
        self.hash_map = self.create_player_lists()

    def create_player_lists(self):
        return [[] for _ in range(self.size)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.size
        else:
            return Player.hash(key, self.size)

    # Insert values into hash map
    def __setitem__(self, key: str, value: str) -> None:
        # get the index from the key using the hash function
        # get the list with the corresponding key
        player_list = self.hash_map[self.get_index(key)]

        record_value = None
        index = None

        found_key = False
        for index, record in enumerate(player_list):
            record_key, record_value = record

            # check if the list has the same key that is searched for
            if record_key == key:
                found_key = True
                break

        # update the key value if it's the same key
        # otherwise add new key and value
        if found_key:
            player_list[index] = (key, value)
        else:
            player_list.append((key, value))

    # return searched value with specific key
    def __getitem__(self, key: str) -> str:
        # get the key and use it get the list
        player_list = self.hash_map[self.get_index(key)]

        record_value = None
        found_key = False
        for index, record in enumerate(player_list):
            record_key, record_value = record
            # check if the list has the same key that is searched for
            if record_key == key:
                found_key = True
                break
        #if the key is found in the list return the value
        if found_key:
            return record_value
        else:
            return "Not Found"


    #
    def __len__(self) -> int:
        return len(self.hash_map)

    # remove a value with a specific key
    def __delitem__(self, key: str) -> None:
        # get the key and use it get the list
        player_list = self.hash_map[self.get_index(key)]

        index = None
        found_key = False
        for index, record in enumerate(player_list):
            record_key, record_value = record
            # check if the list has the same key that is searched for
            if record_key == key:
                found_key = True
                break

        if found_key:
            player_list.pop(index)
        return

    def __str__(self) -> str:
        return "".join(str(item) for item in self.hash_map)

    def display(self) -> None:
        for key, value in enumerate(self.hash_map):
            if value:
                print(f"Key {key}: {value}")

