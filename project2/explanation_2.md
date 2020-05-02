# Problem 2: File Recursion
Joseph An - May 1, 2020

The solution relies on recursion where the base case is a path to a file and a check whether that file matches the suffix.
If the given path is a directory, then it calls the recursive function on all the paths in the directory.

The data structures used in this solution is a python list that stores the file that matches the given suffix.

The time complexity is `O(n)` because the number of operations is dependent on the size of the input, being the number of files and subdirectories within the specified path.

The space complexity is `O(n)` because a list is created containing file path names, where at the worst case can be the same size as the input.
