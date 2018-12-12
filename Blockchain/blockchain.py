from .block import Block
from .transactions import Transactions

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block()
    
    def create_block(self, previous_hash='', proof=100):
        block = Block(len(self.chain), previous_hash, self.transactions[:], proof)
        self.chain.append(block)

    def add_transaction(self, sender, receiver, amount, signature=None):
        transaction = Transactions(sender, receiver, amount, signature)
        self.transactions.append(transaction)
    
    def print_chain(self):
        for c in self.chain:
            print(c)
