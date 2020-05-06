import sys

def huffman_encoding(data):
    if len(data) == 0:
        return ('', None)

    letter_freq_dict = {}
    for c in data:
        if c in letter_freq_dict:
            letter_freq_dict[c] += 1
        else:
            letter_freq_dict[c] = 1

    letter_freq_arr = list(letter_freq_dict.items())
    letter_freq_arr.sort(key=lambda t: t[1])

    if len(letter_freq_arr) == 1:
        letter_freq_arr.append(Node(0))

    while len(letter_freq_arr) > 1:
        left = letter_freq_arr.pop(0)
        right = letter_freq_arr.pop(0)
        node = merge_to_node(right, left)
        insert_node(letter_freq_arr, node)

    root = letter_freq_arr[0]
    tree = Tree(root)
    code_cache = tree.traverse_and_assign_code()
    print(code_cache)
    encoded_data = ''
    for c in data:
        encoded_data += code_cache[c]

    return encoded_data, tree


def merge_to_node(left, right):
    if type(left) is tuple:
        t = left
        left = Node(t[1])
        left.char = t[0]
    if type(right) is tuple:
        t = right
        right = Node(t[1])
        right.char = t[0]
    freq = left.freq + right.freq
    new_node = Node(freq)
    new_node.left = left
    new_node.right = right
    return new_node

def insert_node(arr, node):
    index = 0
    while index < len(arr):
        if node.freq <= frequency(arr[index]):
            arr.insert(index, node)
            return
        index += 1
    arr.append(node)


def frequency(tuple_or_node):
    if type(tuple_or_node) is tuple:
        return tuple_or_node[1]
    else:
        return tuple_or_node.freq

def huffman_decoding(data, tree):
    if len(data) == 0:
        return ''

    decoded = ''
    node = tree.root
    for b in data:
        if b == '0':
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded += node.char
            node = tree.root

    return decoded

class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, node):
        self.arr.append(node)

    def dequeue(self):
        return self.arr.pop(0)

    def is_empty(self):
        return len(self.arr) == 0
        

class Tree:
    def __init__(self, root):
        self.root = root

    def traverse_and_assign_code(self):
        code_cache = {}
        queue = Queue()
        queue.enqueue((self.root.left, "0"))
        queue.enqueue((self.root.right, "1"))

        while not queue.is_empty(): 
            node, code = queue.dequeue()

            if node.char:
                code_cache[node.char] = code
                node.code = code
            else:
                if node.left:
                    queue.enqueue((node.left, code + "0"))
                if node.right:
                    queue.enqueue((node.right, code + "1"))

        return code_cache

class Node:
    def __init__(self, freq):
        self.freq = freq
        self.char = None
        self.code = None
        self.left = None
        self.right = None

def test1():
    print("\nRUNNING TEST 1:")
    encoded_data, tree = huffman_encoding('hello world my name is joseph an and i am learning about data structures and algorithms')
    print(encoded_data)
    print(tree.root.freq)

    decoded = huffman_decoding(encoded_data, tree)
    print(decoded)

test1()
# expects the following to be printed:
# 010011100100110011000000111111100010111001001010000010011111000000110110010011000001101101000011100110001010110011100001001000011001100001100110010100011010000110010000010011100011101100111101001111110000011111011100001000010100000101011010101100010100101101101000111010010101000101111001010000011001100101000011100111110100010111101010101001001001010
# 87
# hello world my name is joseph an and i am learning about data structures and algorithms

def test2():
    print("\nRUNNING TEST 2:")
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


test2()
# The size of the data is: 69
# 
# The content of the data is: The bird is the word
# 
# {' ': '01', 'i': '100', 'e': '101', 'd': '110', 'r': '111', 'h': '0010', 't': '00000', 's': '00001', 'o': '00010', 'w': '00011', 'b': '00110', 'T': '00111'}
# The size of the encoded data is: 36
# 
# The content of the encoded data is: 0011100101010100110100111110011000000101000000010101010001100010111110
# 
# The size of the decoded data is: 69
# 
# The content of the encoded data is: The bird is the word

def test3():
    print("\nRUNNING TEST 3:")
    codes = {}

    a_great_sentence = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

test3()
# expected result:
# The size of the data is: 69
# 
# The content of the data is: The bird is the word
# 
# {' ': '01', 'i': '100', 'e': '101', 'd': '110', 'r': '111', 'h': '0010', 't': '00000', 's': '00001', 'o': '00010', 'w': '00011', 'b': '00110', 'T': '00111'}
# The size of the encoded data is: 36
# 
# The content of the encoded data is: 0011100101010100110100111110011000000101000000010101010001100010111110
#
# The size of the decoded data is: 69
#
# The content of the encoded data is: The bird is the word

def test4():
    print("\nRUNNING TEST 4:")
    codes = {}

    a_great_sentence = ""

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)
    print(tree)
    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)

test4()
# expected result:
# empty string
# None
# empty string
