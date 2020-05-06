# Problem 6: Union and Intersection
Joseph An - May 2, 2010

The data structures used in this problem is the linked list and the dictionary.
Both union and intersection traverses one list and creates a dictionary using the values of the list as the key. So when we traverse the second list we check if the value existts in the dictionary. We also create a new linked list to append the values whether they are in union or intersection, and return the newly created list at the end of the functions.

The time complexity of `union` function is `O(n)` because the function needs to iterate over given linked lists. However since we store the list values in a dictionary as a key, we can look up if the key already exists within the dictionary, thereby avoiding a loop within a loop or `O(n^2)`

The space complexity of the `union` function is also `O(n)` because the we create a dictionary and a new linked list dependent on the size of the input.

The time complexity of `intersection` function is also `O(n)` because the function needs to iterate over given linked lists. We use two dictionaries to store the values as keys in list 1 and list 2. Then we loop over the keys of one dictionary to see if it exists as a key in another dictionary. This lookup is `O(1)`, so we again avoid another loop within a loop.

The space complexity of the `intersection` function is also `O(n)` because the we create two dictionaries and a new linked list dependent on the size of the input.
