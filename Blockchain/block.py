from time import time
from Blockchain.Util.to_dict import ToDict

class Block(ToDict):
    """Criação do objeto bloco, para adição na blockchain.
    Atributos:
        :index: (número) --> a indexação do bloco no blockchain.
        :previous_hash: (string) --> hash de 256 bits do bloco anterior. 
        :transactions: (lista) --> guarda as transações feitas para o bloco atual.
        :proof: (inteiro) chamado de "Proof of Work (PoW)" é um algoritmo que procura um número para os dados retornando nos 4 primeiros digitos da hash "0000".
        :timestamp:(float) é um número flutuante que conta os segundos desde 01/01/1970 00:00:00 (UTC)
    """
    def __init__(self, index, previous_hash, transactions, proof, timestamp=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof = proof
        self.timestamp = timestamp

