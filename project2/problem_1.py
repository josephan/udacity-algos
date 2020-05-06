# Problem 1 Solution

class LRU_Cache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.priority = DoublyLinkedList()
        self.capacity = capacity
        self.cache_count = 0

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.priority.move_to_back(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.priority.move_to_back(node)
            return
        
        new_node = Node(key, value)
        if self.cache_count >= self.capacity:
            head = self.priority.peek()
            self.cache[key] = new_node
            self.priority.append(new_node)
            del(self.cache[head.key])
            self.priority.remove_head()
        else:
            self.priority.append(new_node)
            self.cache_count += 1
            self.cache[key] = new_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_back(self, node):
        if self.head == node:
            self.head = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def append(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def peek(self):
        return self.head
    
    def remove_head(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def __repr__(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.value)
            node = node.next
        return f'Head: {self.head.value}\nTail: {self.tail.value}\nList: {arr.__str__()}\n'
        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Node({self.value})'

# Test cases
# test get/set and removing least recently used cache
def test_case1():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("running test case 1")
test_case1()
# expects to print the following:
# 1
# 2
# -1
# -1

# test cache getting without any input
def test_case2():
    c = LRU_Cache(5)
    print(c.get(1))
    print(c.get(2))
    print(c.get(3))

print("running test case 2")
test_case2()
# expects to print the following:
# -1
# -1
# -1
    
# test cache with multiple same cache keys
def test_case3():
    c = LRU_Cache(5)
    c.set(1, "abc")
    c.set(1, "abc")
    c.set(1, "abc")
    c.set(1, "abc")
    c.set(1, "abc")
    c.set(1, "abc")
    c.set(1, "123")
    print(c.cache_count)
    print(c.get(1))

print("running test case 3")
test_case3()
# expects to print the following:
# 1
# 123

# test cache with 0 capacity
def test_case4():
    c = LRU_Cache(0)
    c.set(1, "abc")
    print(c.cache_count)
    print(c.get(1))

print("running test case 3")
test_case4()
# expects to print the following:
# 0
# -1
