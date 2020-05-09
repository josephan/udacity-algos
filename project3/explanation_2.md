# Problem 2: Search in a Rotated Array
Joseph An - Thur, May 7, 2020

This problem can be solved using a slightly modified binary search algorithm.
Given a rotated array, if we split the array in half, there will always be a half that is sorted. We check if the target is within the upper and lower bounds of the sorted half. If it is then we continue doing a binary search in taht half. If not then we recursively call the function on the unsorted half. Again in this unsorted half there will be one half that is sorted and so on.

Because the input is always cut in half for each recursive call, the time complexity is `O(log n)`.

Also the recursive function doesn't use any other data structures and operate on the input list in place, so the space complexity is `O(1)`.
