from app.player import Player
from app.player_list import PlayerList


# References used:
# https://www.geeksforgeeks.org/hash-map-in-python/
# https://www.w3schools.com/dsa/dsa_data_hashmaps.php
class PlayerHashMap:
    # create empty player list of given size
    def __init__(self, size):
        self.size = size
        self.hash_map = self.create_player_lists()


    def create_player_lists(self):
        return [PlayerList() for _ in range(self.size)]


    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.size
        else:
            return Player.hash(key, self.size)


    # Insert values into hash map
    def __setitem__(self, key: str, name: str) -> None:
        # get the index from the key using the hash function
        # get the list with the corresponding key
        index = self.get_index(key)
        player_list = self.hash_map[index]

        #Create player, check if player exists, if not add to list, else change name
        player = Player(key, name)
        if player_list.search(player.uid) is None:
            player_list.push(player)
        else:
            player_list.update(player)


    # return searched value with specific key
    def __getitem__(self, key: str) -> Player | None:
        # get the key and use it get the list
        index = self.get_index(key)
        player_list = self.hash_map[index]
        player = player_list.search(key)

        if player:
            return player
        else:
            return None


    #
    def __len__(self) -> int:
        return len(self.hash_map)

    # remove a value with a specific key
    def __delitem__(self, key: str) -> None:
        # get the key and use it get the list
        index = self.get_index(key)
        player_list = self.hash_map[index]
        delete_success = player_list.delete(key)
        if delete_success:
            return None
        else:
            raise ValueError('Player not found')


    def __str__(self) -> str:
        return "".join(str(item) for item in self.hash_map)


    def display(self) -> None:
        for key, value in enumerate(self.hash_map):
            if value:
                print(f"Key {key}: {value}")

