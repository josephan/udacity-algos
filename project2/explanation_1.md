# Problem 1: LRU Cache
Joseph An - Fri, May 1, 2020

In my solution I use a dictionary and a doubly linked list.

The dictionary's keys are the keys set by the key from `LRU_Cache#set(key, value)`. The dictionary's value points to a `Node` in the doubly linked list.

The doubly linked list has a head and a tail. The head points to the least recently used cache and the tail points to the most recently used cache (either by get or set).
Each `Node` in the list stores the key and value from the `set` method.

The dictionary is the perfect data structure to `get` and `set` key/value pairs for our cache because the time complexity is `O(1)` for both operations. Easy right? But here's the catch. We need to limit the size of the cache to some capacity and when we hit that capacity we need to remove the least recently used entry before setting another entry. In order to keep track of the least recently used entry in our cache, we need some sort of list. The elements within this list will be have the following operations that all require `O(1)` time complexity:

* remove the first element of this list (when the cache's capacity is reached and we set a new entry)
* move any element within the list to the back of the list (when a get or set operation is called on an existing key)
* append a new element to the back of this list (after a get/set operation on an entry, the entry is now the most recently used)

A doubly linked list fulfills this requirement. However, since we use a dictionary and a doubly linked list to keep track of existing key/values in our cache, the space complexity is `O(n)`.

In conclusion the time complexity is `O(1)` and the space complexity is `O(n)`.
