# Problem 3: Rearrange Array Elements

This solution uses Python's built in list data structure as a stack to assemble the final result.
To sort the input list we use the Quick sort algorithm which is suitable for most cases of sorting as it has an average time complexity of `O(n log n)`. After sorting the list we iterate through the list like a stack by using the `pop` method which has the time complexity of `O(n)`. The total time complexit is `O(2n log n)` but the constant 2 factor can be dropped to `O(n log n)`.

The space complexity is `O(1)` because the quick sort algorithm doesn't create any new lists based on the input. It sorts the elements of the list in place.
