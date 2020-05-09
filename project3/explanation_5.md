# Problem 5: Autocomplete with Tries

The data structure used in this problem is the Trie to keep track of words.
To insert a new word into the trie the time complexity is `O(n)` because we have to traverse or insert a new node into the trie for the length of the input (in our case the length of the word to insert). The space complexity in the worst case is also `O(n)` because a new node needs to be created depending on the size of the input.

The find function of the trie has a time complexity of `O(n)` because we traverse through each node of the trie `n` times until we reach the size of the word. The space complexity of the find function is `O(1)` because no new variables or data structure is created dependant on the size of `n` while traversing through the trie.
