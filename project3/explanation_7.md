# Problem 7: Request Routing in a Web Server with a Trie

The data structure used in this problem is the Trie to keep track of words. The trie is made up of Python's built in dictionary.

The insert function of the trie and the add_handler function of the router has a time complexity of `O(n)` because we have to traverse or insert a new node into the trie for the length of the input (in our case the number of sub_paths in our path). The space complexity in the worst case is also `O(n)` because a new node needs to be created depending on the size of the input.

The find function of the trie and the lookup function of the router trie has a time complexity of `O(n)` because we traverse through each node of the trie `n` times until we reach the desired sub_path. The space complexity of the find function is `O(1)` because no new variables or data structure is created dependant on the size of `n` while traversing through the trie.
