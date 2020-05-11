class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node = node.insert(char)
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        if char not in self.children:
            node = TrieNode(char)
            self.children[char] = node
        else:
            node = self.children[char]
        return node
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        node = self
        return self._suffixes(node, '')
    
    def _suffixes(self, node, chars):
        words = []

        if node.is_word:
            words.append(chars)
            
        if len(node.children) == 0:
            return words
        
        for char in node.children:
            next_node = node.children[char]
            word = self._suffixes(next_node, chars + next_node.char)
            words += word
        
        return words

# Test 1
# Test empty trie
trie1 = Trie()
node1 = trie1.find('')
print(node1.suffixes()) # => expected to print []

# Trie for test 2 and 3
trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    trie.insert(word)

# Test 2: suffixes of prefix 'an'
node2 = trie.find('an')
print(node2.suffixes()) # => expected to print ['t', 'thology', 'tagaonist', 'tonym']

# Test 3: suffixes of 'fu'
node3 = trie.find('fu')
print(node3.suffixes()) # => expected to print ['n', 'nction']
