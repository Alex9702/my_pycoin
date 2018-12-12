from Blockchain.Util.to_dict import ToDict

class Transactions(ToDict):
    def __init__(self, sender, receiver, amount, signature):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
