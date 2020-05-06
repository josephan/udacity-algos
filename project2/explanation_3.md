# Problem 3: Huffman Coding
Joseph An - May 1, 2020

In this problem we use a binary tree to store the Huffman tree and a queue to traverse the Huffman tree with breadth first search to assign codes to the characters.

The time complexity of the `huffman_encoding` function is `O(n log n)` because there is a `sort()` method that sorts the tuple containing the character and it's frequency.
Also there are two loops over the given input. One loop to create a dictionary of the frequency of each character and another loop to encode the given data.

The space complexity of the `huffman_encoding` is `O(n)` as we create a hash of character frequency and a string of encoded data. The size of both data types are dependent on the size of the input.

The time complexity of `huffman_decoding` function is `O(n log n)` because for every encoded character in the input the tree needs to be traversed to find the decoded character.

The space complexity of `huffman_decoding` function is `O(n)` because we create a new decoded string dependent on the size of the input.
