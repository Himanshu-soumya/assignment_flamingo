class Node:
    """A node in the linked list for handling collisions in the hash map."""
    def __init__(self, key, value):
        self.key = key          # The key of the entry
        self.value = value      # The value of the entry
        self.next = None        # Pointer to the next node in the linked list

class MyHashMap:
    """A simplified HashMap implementation."""
    def __init__(self):
        self.size = 1000        # Size of the hash table (array)
        self.table = [None] * self.size  # Initialize the hash table with None

    def _hash(self, key: int) -> int:
        """Compute the hash value for a given key."""
        return key % self.size  # Simple modulus operation for hashing

    def put(self, key: int, value: int) -> None:
        """Insert or update the value by key."""
        index = self._hash(key)  # Get the index for the key
        if self.table[index] is None:
            self.table[index] = Node(key, value)  # Create a new node if the slot is empty
        else:
            # Collision handling: Traverse the linked list at this index
            current = self.table[index]
            while True:
                if current.key == key:
                    current.value = value  # Update the value if the key exists
                    return
                if current.next is None:
                    break  # Reached the end of the list
                current = current.next
            # Add a new node at the end of the linked list
            current.next = Node(key, value)

    def get(self, key: int) -> int:
        """Return the value associated with the key. If not found, return -1."""
        index = self._hash(key)  # Get the index for the key
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value  # Return the value if the key is found
            current = current.next
        return -1  # Key not found

    def remove(self, key: int) -> None:
        """Remove the key from the map."""
        index = self._hash(key)  # Get the index for the key
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    # Removing the first node in the linked list
                    self.table[index] = current.next
                else:
                    # Bypass the current node
                    prev.next = current.next
                return
            prev = current
            current = current.next

# Example usage:
my_hash_map = MyHashMap()  # Create a new instance of MyHashMap
my_hash_map.put(1, 10)     # Insert key 1 with value 10
my_hash_map.put(2, 20)     # Insert key 2 with value 20
print(my_hash_map.get(1))   # Returns 10
print(my_hash_map.get(3))   # Returns -1 (not found)
my_hash_map.put(2, 30)      # Update key 2 with value 30
print(my_hash_map.get(2))   # Returns 30
my_hash_map.remove(2)       # Remove key 2
print(my_hash_map.get(2))   # Returns -1 (not found)
