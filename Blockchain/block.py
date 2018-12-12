from time import time
from Blockchain.Util.to_dict import ToDict

class Block(ToDict):
    def __init__(self, index, previous_hash, transactions, proof, timestamp=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof = proof
        self.timestamp = timestamp
