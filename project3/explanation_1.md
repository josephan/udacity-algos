# Problem 1: Square Root of an Integer
Joseph An - Thu May 7, 2020

Binary search is the perfect algorithm for this problem. We know that the square root is never going to be greater than half the input number. So we keep on halving the 'guess' until we reach the closest integer solution.
The runtime of this algorithm is `O(log n)`.

In my solution I use an iterative approach to binary search and don't use any data structures. We simply store the upper and lower bounds while searching for the half. As a result the space complexity of the algorithm is `O(1)`.
