__all__ = ['create_block', 'print_blockchain']
from .block import Block
from .transactions import Transactions
from .Encoding.hash_util import hash_block, hash_string_256
from .Util.list_dict import block_dict

MINNING_REWARD = 10

# Listas de blocos para formar a blockchain.
chain = []
# Lista de transações para ser adicionado no bloco, desde
transactions = []
# Primeiro bloco do Blockchain
genesis_block = Block(len(chain) + 1, '', [], 100, 0.0)
chain.append(genesis_block)

def add_transaction(sender, receiver, amount, signature=None):
    transaction = Transactions(sender, receiver, amount, signature)
    transactions.append(transaction)

def create_block(previous_hash, proof):
    block = Block(len(chain) + 1, previous_hash, transactions[:], proof)
    chain.append(block)
    return block

def proof_of_work(previous_proof, difficult=4):
    proof = 1
    while True:
        if hash_string_256(str(proof**2 - previous_proof**2))[:4] == '0' * difficult:
            return proof
        proof += 1

def get_balance():
    pass

def get_last_block():
    return chain[-1]

def mine_block(host):
    last_block = get_last_block()
    proof = proof_of_work(last_block.proof)
    reward_transaction = Transactions('MINNING', host, MINNING_REWARD, None)
    transactions.append(reward_transaction)
    previous_hash = hash_block(block_dict(last_block))
    create_block(previous_hash, proof)
    transactions.clear()

def print_blockchain():
    print('----- Printing blockchain -----')
    for block in chain:
        print(block)
        print(50*'-')