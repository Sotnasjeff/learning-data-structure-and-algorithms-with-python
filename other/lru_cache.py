class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:
    def __init__(self, capacity:int ):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.previous = self.left
    
    def remove(self, node):
        prev, _next = node.previous, node.next
        prev.next = _next
        _next.previous = prev
    
    def insert(self, node):
        prev, _next = self.left, self.left.next
        _next.previous = node
        prev.next = _next.previous
        node.next = _next
        node.previous = prev

    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    
    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.right.previous
            self.remove(lru)
            del self.cache(lru.key)