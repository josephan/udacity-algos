The linked list data structure is used for this problem because each block needs to keep track of another block before it because it uses the previous block's hash to calculate the current blocks hash. The linked list creates a "chain" of blocks.

The lookup time for a single block is `O(n)` because we need to traverse the list to look for a block.
The insert time for a single block is `O(1)` because blocks are always added to the head.
The space complexity for this blockchain is `O(n)` because the amount of space it takes is dependent on the input size (number of blocks created).
