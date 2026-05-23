class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.head = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.map = {}
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert_at_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_from_tail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        del self.map[node.key]

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_at_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        
        node = Node(key, value)
        self.map[key] = node
        self._insert_at_head(node)

        if len(self.map) > self.capacity:
            self._remove_from_tail()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)