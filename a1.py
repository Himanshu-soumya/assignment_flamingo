class Node:
    """A node in the doubly linked list representing each cache entry."""
    def __init__(self, key, value):
        self.key = key          # The key of the cache entry
        self.value = value      # The value of the cache entry
        self.prev = None        # Pointer to the previous node
        self.next = None        # Pointer to the next node

class LRUCache:
    """A Least Recently Used (LRU) Cache implementation."""
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum capacity of the cache
        self.cache = {}           # Dictionary to store key -> Node mapping
        self.head = Node(0, 0)    # Dummy head node for the linked list
        self.tail = Node(0, 0)    # Dummy tail node for the linked list
        self.head.next = self.tail # Initialize the linked list
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node  # Bypass the node to be removed
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        """Add a node to the front of the linked list (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node  # Link the next node back to the new node
        self.head.next = node        # Link the new node to the head

    def get(self, key: int) -> int:
        """Return the value of the key if it exists in the cache, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]  # Get the node from the cache
            self._remove(node)       # Remove it from its current position
            self._add_to_front(node) # Move it to the front (most recently used)
            return node.value        # Return the value
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        """Update or insert the value. Evict the least recently used item if the cache is full."""
        if key in self.cache:
            # If the key already exists, update the value and move it to the front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Create a new node for the new key-value pair
            new_node = Node(key, value)
            self.cache[key] = new_node  # Add the new node to the cache
            self._add_to_front(new_node) # Add the new node to the front

            # Check if the cache exceeds its capacity
            if len(self.cache) > self.capacity:
                # Remove the least recently used item (the node before the tail)
                lru_node = self.tail.prev
                self._remove(lru_node)    # Remove it from the linked list
                del self.cache[lru_node.key]  # Remove it from the cache

# Example usage:
lru = LRUCache(2)  # Create an LRU Cache with a capacity of 2
lru.put(1, 1)      # Cache is {1=1}
lru.put(2, 2)      # Cache is {1=1, 2=2}
print(lru.get(1))  # Returns 1, Cache is {2=2, 1=1}
lru.put(3, 3)      # Evicts key 2, Cache is {1=1, 3=3}
print(lru.get(2))  # Returns -1 (not found)
lru.put(4, 4)      # Evicts key 1, Cache is {3=3, 4=4}
print(lru.get(1))  # Returns -1 (not found)
print(lru.get(3))  # Returns 3
print(lru.get(4))  # Returns 4
