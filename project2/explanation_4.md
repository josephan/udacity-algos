# Problem 4: Active Directory
Joseph An - May 2, 2020

The main data structure used in this solution is the dictionary within `UsersByGroupCache`.

Whenever we add a new user we update the cache like so:
```python
# user: Bill
# group: Micro
cache = {
    'Micro': {
        'Bill': True
    }
}
```

As you can see we use a nested dictionary so that the look up times for a group is `O(1)` and a look up time for a user within that group is also `O(1)`. So the time complexity is `O(1)`.

The space complexity is `O(n)`, as we add a new key/value pair into our dictionaryn for every input.
