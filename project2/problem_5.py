import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(timestamp, data, previous_hash)
        self.previous_block = None

    def calc_hash(self, timestamp, data, previous_hash):
        sha = hashlib.sha256()
        hash_str = (timestamp + data + previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        s = ''
        s += 'Block(\n'
        s += f'  hash: {self.hash}\n'
        s += f'  prev: {self.previous_hash}\n'
        s += f'  data: {self.data}\n'
        s += f'  timestamp: {self.timestamp}\n'
        s += ')'
        return s

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        prev_hash = (self.head and self.head.hash) or ''
        timestamp = datetime.utcnow().__str__()
        block = Block(timestamp, data, prev_hash)
        block.previous_block = self.head
        self.head = block
    
    def __repr__(self):
        block = self.head
        while block:
            print(block)
            print('------------------')
            block = block.previous_block
        return ''

# test empty blockchain
def test1():
    bc = Blockchain()
    print(bc)

test1()
# should output nothing
        
# test single block blockchain
def test2():
    bc = Blockchain()
    bc.add_block('hello world')
    print(bc)

test2()
# should output hello world block
# Block(
#   hash: 53c5a6824ee7a8038f8d7e1174e1ee0a3fd931b64d84e7e1a6e2a31f5330c92a
#   prev: 
#   data: hello world
#   timestamp: 2020-05-02 21:12:17.855829
# )
# ------------------

# test single block blockchain
def test2():
    bc = Blockchain()
    bc.add_block('one')
    bc.add_block('two')
    bc.add_block('three')
    bc.add_block('four')
    bc.add_block('five')
    bc.add_block('six')
    print(bc)

test2()
# should six blocks
# Block(
#   hash: c44a9404e8bf774c3b44babb2b9e0ffd2fb38b79e1b9de4a5fe5d7330af83dd6
#   prev: f6e1ca4ac3fd570c1fc0195f3bb29073786a429c320853d414206eb3e61d4a61
#   data: six
#   timestamp: 2020-05-02 21:12:17.855905
# )
# ------------------
# Block(
#   hash: f6e1ca4ac3fd570c1fc0195f3bb29073786a429c320853d414206eb3e61d4a61
#   prev: 8a2298772e7d26753543ddc76aeb515fd74cbecb2f8617c9f41459a829d3f4ba
#   data: five
#   timestamp: 2020-05-02 21:12:17.855901
# )
# ------------------
# Block(
#   hash: 8a2298772e7d26753543ddc76aeb515fd74cbecb2f8617c9f41459a829d3f4ba
#   prev: be0a57078eb63d2f339e9d58bb4cb6141501477ee6fee169a005af6bf14e8b69
#   data: four
#   timestamp: 2020-05-02 21:12:17.855897
# )
# ------------------
# Block(
#   hash: be0a57078eb63d2f339e9d58bb4cb6141501477ee6fee169a005af6bf14e8b69
#   prev: cf4d58b4eb6a81f43902a894b47ff23c83502abb2144e2f70df45504a0b78168
#   data: three
#   timestamp: 2020-05-02 21:12:17.855892
# )
# ------------------
# Block(
#   hash: cf4d58b4eb6a81f43902a894b47ff23c83502abb2144e2f70df45504a0b78168
#   prev: 674534e4f92c544c2c19ffaec9152ccb8f3fcf7809f44618058abd3a21662b6c
#   data: two
#   timestamp: 2020-05-02 21:12:17.855887
# )
# ------------------
# Block(
#   hash: 674534e4f92c544c2c19ffaec9152ccb8f3fcf7809f44618058abd3a21662b6c
#   prev: 
#   data: one
#   timestamp: 2020-05-02 21:12:17.855877
# )
# ------------------
