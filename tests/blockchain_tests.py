import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Blockchain.blockchain import genesis_block, chain, create_block, add_transaction
from Blockchain.Util.list_dict import block_dict, transactions_dict

add_transaction('Alex','Max', 5.5)
add_transaction('John','Joe', 10.5)
create_block('123', 123)

class BlockchainTests(unittest.TestCase):
    def basic_test(self):
        assert genesis_block.index == 0
        assert genesis_block.previous_hash == ''
        assert genesis_block.transactions == []
        assert genesis_block.proof == 100
        assert chain[0] == genesis_block

    def json_testes(self):
        self.assertTrue(isinstance(block_dict(chain), dict))
        self.assertTrue(isinstance(transactions_dict(chain), int))
        print('Ok, ok')


if __name__ == '__main__':
    unittest.main()
