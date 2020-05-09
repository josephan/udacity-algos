# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        node = RouteTrieNode('')
        node.handler = root_handler
        self.root = node

    def insert(self, sub_paths, handler):
        node = self.root
        for sub_path in sub_paths:
            node = node.insert(sub_path)
        node.handler = handler
        return node

    def find(self, sub_paths):
        node = self.root
        for sub_path in sub_paths:
            if sub_path in node.children:
                node = node.children[sub_path]
            else:
                return None
        return node

class RouteTrieNode:
    def __init__(self, sub_path):
        self.sub_path = sub_path
        self.handler = None
        self.children = {}

    def insert(self, sub_path):
        if sub_path not in self.children:
            new_node = RouteTrieNode(sub_path)
            self.children[sub_path] = new_node
            return new_node
        else:
            return self.children[sub_path]

class Router:
    def __init__(self, root_handler, default_handler):
        self.route_trie = RouteTrie(root_handler)
        self.default_handler = default_handler

    def add_handler(self, path, handler):
        sub_paths = self.split_path(path)
        node = self.route_trie.insert(sub_paths, handler)

    def lookup(self, path):
        sub_paths = self.split_path(path)
        node = self.route_trie.find(sub_paths)
        if node and node.handler:
            return node.handler
        else:
            return self.default_handler

    def split_path(self, path):
        return list(filter(lambda x: x != '', path.split("/")))

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Test strange and empty urls
print(router.lookup("")) # should print 'root handler'
print(router.lookup("//////////")) # should print 'root handler'

# Test overriding existing handlers
router.add_handler("/home/about", "i like pizza")  # add a route
print(router.lookup("/home/about")) # should print 'i like pizza'

# Test adding handler in sub_path
router.add_handler("/home/about/me", "i like udacity")  # add a route
print(router.lookup("/home/about")) # should print 'i like pizza'
print(router.lookup("/home/about/me")) # should print 'i like udacity'

