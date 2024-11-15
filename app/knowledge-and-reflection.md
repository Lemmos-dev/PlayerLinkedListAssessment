# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> Hash functions take data of any size and transforms it to a fixed length of data. This new data cannot be reversed to its original form.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

>- SSH: 
>  - Advantages: Extremely efficient and deterministic.
>  - Disadvantages: Only ever returns 1 which means; No collision resistance, no sensitivity to input changes.

>- Sum of Ascii_values: 
>  - Advantages: Efficient, simple and deterministic.
>  - Disadvantages: It has a poor distribution rate as characters in different orders will lead to the same sum. Lacks uniformity and doesn't offer uniqueness need for security. 

>- Pearson Hash:
>  - Advantages: Simple and efficient. Collisions are unlikely in small data sets
>  - Disadvantages: Not suited for large data sets as it only generates short hash values. Lacks security

>- Built in hash:
>  - Advantages: Optimised and efficient and suited for general purpose python features such as dictionaries.
>  - Disadvantages: Lacks determinism across sessions and updates as python will change the random seed for the hash.

>- SHA256:
>  - Advantages: Deterministic, non-reversible, collision resistant, and extremely sensitive to input changes.
>  - Disadvantages: Not as efficient as other hashing methods, Large output size which will noy work if the host machine has too low bit width 

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

>- Deterministic - Hash maps rely on consistent mapping. If the same input doesn't produce the same output then you won't be able to find or store data based on keys
>- Efficiency - Hashes are used to speed up the process of finding data. If the process is too slow it would not be worth using.
>- Uniformity - Reduces the chance of clustering and collisions which in turn improves the efficiency
>
>- Collision Resistance can be handled with additional techniques. Sensitivity to input changes and security are not important for general hashing

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> SHA256 as it has the fewest drawbacks, and best advantages

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> - import random 
> random.seed(42)
>  - Randomness with a set seed in a pearson table shuffles the table but still provides deterministic outputs
>- pearson_table = list(range(256))
>  - Pearson hashing works by having a table of all byte values to cover all potential inputs of ASCII or byte characters.
>  - Which makes it efficient to use but also the byte size limits its use to small datasets
>- random.shuffle(pearson_table)
>  - Shuffling the table prevents the hash from using a sequential byte order. Improving uniformity
>- def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
>  - Defines the pearson hash function and its two inputs key and size as well as the expected types and initializes the hash value
>-  for char in key:
>  - Efficient looping for small datasets
>- hash_ = pearson_table[hash_ ^ ord(char)]
>  - Every character is XORed with the current hash value with the result being indexed the pearson table and get the next hash value 
>  - This makes it sensitive to input changes and reduces the chance of collisions.
>- return hash_ % size
>  - The hash value is reduced to fit within the specified size

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

```python
   #Function that adds a player to a playerlist in a hashmap
    function setplayer (hash_map, playerlist, player)
        #Hash the list name to get the list of playerlists
        index = hash_function(playerlist)
        
        #check if the playerlist is in the hash map
        if hash_map[index] is null
            #if it is empty create a new list
            hash_map[index] = PlayerList()

        #add the player to the new list
        hash_map[index].playerlist.push(player)
```

## Reflection

1. What was the most challenging aspect of this task?

> Explaining the pearson table

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> Change it to create a list of PlayerLists. And each function would need to be adjusted to be able to work with the list of player lists

## Sources Used
https://www.wallstreetmojo.com/hash-function/
https://kinsta.com/blog/python-hashing/
https://en.wikipedia.org/wiki/Pearson_hashing

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.


