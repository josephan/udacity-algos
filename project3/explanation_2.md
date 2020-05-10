# Problem 2: Search in a Rotated Array
Joseph An - Thur, May 7, 2020

This problem can be solved using a slightly modified binary search algorithm.
Given a rotated array, if we split the array in half, there will always be a half that is sorted. We check if the target is within the upper and lower bounds of the sorted half. If it is then we continue doing a binary search in taht half. If not then we recursively call the function on the unsorted half. Again in this unsorted half there will be one half that is sorted and so on.

Because the input is always cut in half for each recursive call, the time complexity is `O(log n)`.

The solution doesn't use up memory dependant on the size of the input. However the quicksort algorithm sorts the array in place but because it uses recursion it takes up memory in the stack. The space complexity of the algorithm is `O(log n)`.
