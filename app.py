from flask import Flask, jsonify, request
from Blockchain.Util.data_handler import load_blockchain, load_transactions
from Blockchain.blockchain import is_valid_chain, add_transaction, mine_block

app = Flask(__name__)

@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify(load_blockchain()), 200

@app.route('/is_valid', methods=['GET'])
def is_valid():
    valid = is_valid_chain()
    if valid:
        response = {'mensage: ': 'Blockchain válido!'}
    else:
        response = {'mensage: ': 'Blockchain inválido!'}
    return jsonify(response), 200

@app.route('/add_transactions', methods=['POST'])
def add_transactions():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return 'Preencher todos os atributos.', 400
    add_transaction(json['sender'],json['receiver'], json['amount'])
    response = {'mensagem':'Transação adiconada.', 'transações':load_transactions()}
    return jsonify(response), 201


@app.route('/miner_block', methods=['GET'])
def miner_block():
    mine_block('Alex')
    blockchain = load_blockchain()
    return jsonify(blockchain[-1])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)