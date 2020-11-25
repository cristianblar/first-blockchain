import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data) + self.timestamp + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def set_previous_block(self, block):
        self.previous = block

    def get_previous_block(self):
        return self.previous

    def get_hash(self):
        return self.hash

    def __repr__(self):
        return ('Timestamp: ' + str(self.timestamp) + '\nData: ' +
                str(self.data) + '\nSHA256 Hash: ' + str(self.hash) +
                '\nPrev_Hash: ' + str(self.previous_hash))


class BlockChain:

    def __init__(self):
        self.tail = None

    def set_tail(self, block):
        self.tail = block

    def get_tail(self):
        return self.tail

    def append_block(self, data):
        if self.get_tail() is None:
            new_block = Block(str(datetime.datetime.utcnow()), data, 0)
            self.set_tail(new_block)
        else:
            new_block = Block(str(datetime.datetime.utcnow()), data,
                              self.get_tail().get_hash())
            new_block.set_previous_block(self.get_tail())
            self.set_tail(new_block)

    # This method will print from the most recent block to the first appended:
    def print_blockchain(self):
        current_block = self.get_tail()
        while current_block:
            print(current_block)
            print('-*-*-*-*-*-*-*-*-')
            current_block = current_block.get_previous_block()


if __name__ == '__main__':

    # TEST CASE 1:
    print('TEST CASE 1:')
    test_bc = BlockChain()

    data1 = "First Blockchain block"
    data2 = "Second Blockchain block"
    data3 = "Third Blockchain block"

    test_bc.append_block(data1)
    test_bc.append_block(data2)
    test_bc.append_block(data3)

    test_bc.print_blockchain()

    # TEST CASE 2:
    print('TEST CASE 2:')
    test_bc_2 = BlockChain()

    data1 = " "
    data2 = 123456789
    data3 = None

    test_bc_2.append_block(data1)
    test_bc_2.append_block(data2)
    test_bc_2.append_block(data3)

    test_bc_2.print_blockchain()

    # TEST CASE 3:
    print('TEST CASE 3:')
    test_bc_3 = BlockChain()
    # Repeated data with different hash
    data1 = "!$%&1234"
    data2 = '123456789'
    data3 = None
    data4 = 987456211477788547854102
    data5 = '123456789'
    data6 = 'None'
    data7 = 987456211477788547854102
    data8 = 'This will be a long string... UDACITY UDACITY UDACITY\
            UDACITY UDACITY UDACITY UDACITY UDACITY UDACITY UDACITY'

    test_bc_3.append_block(data1)
    test_bc_3.append_block(data2)
    test_bc_3.append_block(data3)
    test_bc_3.append_block(data4)
    test_bc_3.append_block(data5)
    test_bc_3.append_block(data6)
    test_bc_3.append_block(data7)
    test_bc_3.append_block(data8)

    test_bc_3.print_blockchain()
