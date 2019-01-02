import json


def load_blockchain():
    blockchain = []
    try:
        with open('data/blockchain.json', mode='r') as f:
            blockchain = json.loads(f.readlines()[0])
    except (FileNotFoundError, IndexError):
        save_blockchain([])
    return blockchain

def save_blockchain(blockchain):
    with open('data/blockchain.json', mode='w') as f:
        f.write(json.dumps(blockchain))

def load_transactions():
    transactions = []
    try:
        with open('data/transactions.json', mode='r') as f:
            transactions = json.loads(f.readlines()[0])
    except (FileNotFoundError, IndexError):
        save_transactions(transactions)
    return transactions

def save_transactions(transactions):
    with open('data/transactions.json', mode='w') as f:
        f.write(json.dumps(transactions))