class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union = {}
    llist_into_dict(llist_1, union)
    llist_into_dict(llist_2, union)
    llist = LinkedList()
    for key in union:
        llist.append(key)

    return llist

def llist_into_dict(llist, dictionary):
    node = llist.head
    while node:
        if node.value not in dictionary:
            dictionary[node.value] = True
        node = node.next
    return dictionary

def intersection(llist_1, llist_2):
    # Your Solution Here
    dict1 = {}
    dict2 = {}
    llist_into_dict(llist_1, dict1)
    llist_into_dict(llist_2, dict2)

    llist = LinkedList()
    for key in dict1:
        if key in dict2:
            llist.append(key)

    return llist


# Test case 1
# intersection and union of numbers
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# Should ouput:
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
# 4 -> 6 -> 21 ->

# Test case 2
# test empty list
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# Should ouput two empty lines

# Test case 3
# test non numerical values
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [None]
element_2 = ['string']

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# should print empty line for unions
# should print None -> string ->  for intersection
