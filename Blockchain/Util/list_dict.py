def block_dict(block):
    transactions = [t.to_dict() for t in block.transactions]
    bl = block.to_dict()
    bl['transactions'] = transactions
    return bl