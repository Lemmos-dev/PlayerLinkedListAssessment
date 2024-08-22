from player import Player

# https://www.geeksforgeeks.org/hash-map-in-python/
class PlayerHashMap:
    #create empty player list of given size
    def __init__(self, size):
        self.size = size
        self.hash_map = self.create_player_lists()

    def create_player_lists(self):
        return [[] for _ in range(self.size)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.size
        else:
            return Player.hash(key) % self.size

    #Insert values into hash map
    def __setitem__(self, key: str, value: Player) -> None:
        #get the index from the key using the hash function
        hashed_key = hash(key) % self.size #self.get_index(key)

        #get the player with the corresponding key
        player_list = self.hash_map[hashed_key]

        found_key = False
        index: int
        for index, record in enumerate(player_list):
            record_key, record_value = record

            # check if player has the same key that will be inserted
            if record_key == key:
                found_key = True
                break

        #update the key value if it's the same key
        #otherwise add new key and value
        if found_key:
            player_list[index] = (key, value)
        else:
            player_list.append((key, value))

    #return searched value with specific key
    def __getitem__(self, key: str) -> Player:
        ...

    #
    def __len__(self) -> int:
        return Player.size

    #remove a value with a specific key
    def __delitem__(self, key: str) -> None:
        ...
