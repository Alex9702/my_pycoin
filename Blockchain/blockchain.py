from time import time
from .Util.hash_util import sha256, hash_block
from .Util.data_handler import load_blockchain, save_blockchain
from .Util.data_handler import load_transactions, save_transactions

MINING_REWARD = 10

def create_block(index=0, transactions=None, previous_hash='', proof=100):
    block = {
        'index': index,
        'previous_hash': previous_hash,
        'proof': proof,
        'transactions': transactions if transactions else [],
        'timestamp': time()
    }
    return block

def get_balance(t):
    blockchain = load_blockchain()
    transactions = load_transactions()
    tx_receiver = [tx['amount'] for bloco in blockchain
                   for tx in bloco['transactions']
                   if tx['receiver'] == t]
    tx_sender = [tx['amount'] for bloco in blockchain
                 for tx in bloco['transactions']
                 if tx['sender'] == t]
    tx_receiver_transactions = [tx['amount'] for tx in transactions if tx['receiver'] == t]
    tx_sender_transactions = [tx['amount'] for tx in transactions if tx['sender'] == t]
    tx_sender.extend(tx_sender_transactions)
    tx_receiver.extend(tx_receiver_transactions)
    return (sum(tx_receiver) > sum(tx_sender))

def add_transaction(sender, receiver, amount):
    if get_balance(sender):
        transactions = load_transactions()
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'signature': None
        }
        transactions.append(transaction)
        save_transactions(transactions)

def clear_transactions():
    save_transactions([])

def mine_block(hosting):
    blockchain = load_blockchain()
    if not blockchain:
        blockchain.append(create_block())
    index = len(blockchain)
    previous_hash = hash_block(blockchain[-1])
    previous_proof = blockchain[-1]['proof']
    proof = proof_of_work(previous_proof)
    transaction = {
            'sender': 'mining',
            'receiver': hosting,
            'amount': MINING_REWARD,
            'signature': None
        }
    transactions = load_transactions()
    transactions.append(transaction)
    block = create_block(index, transactions, previous_hash, proof)
    blockchain.append(block)
    save_blockchain(blockchain)
    clear_transactions()

def proof_of_work(previous_proof, difficult=4):
    proof = 1
    while True:       
        if sha256(str(proof**2 - previous_proof**2))[:difficult] == '0' * difficult:
            break
        proof += 1
    return proof

def print_blockchain_values():
    blockchain = load_blockchain()
    for block in blockchain:
        print(block)
    print(50*'-')

def is_valid_chain():
    blockchain = load_blockchain()
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        if block['proof'] != proof_of_work(blockchain[index - 1]['proof']):
            return False
    return True

