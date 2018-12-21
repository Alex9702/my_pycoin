__all__ = ['create_keys', 'save_keys', 'read_keys']
import json
import os
import binascii
import hashlib
from Crypto.PublicKey import RSA
import Crypto.Random
from Blockchain.Util.wallet_base import base16_to_base58, base58_to_base16


def create_keys():
    ''' Criação de chaves publica e privada.'''
    _pr = RSA.generate(1024, Crypto.Random.new().read)
    _public_key = RSA.binascii.hexlify(_pr.publickey().exportKey()).decode('ascii')
    _pk_b58 = base16_to_base58(_public_key)
    _private_key = RSA.binascii.hexlify(_pr.exportKey()).decode('ascii')
    _pr_b58 = base16_to_base58(_private_key)

    return {'private_key': _pr_b58, 'public_key': _pk_b58}

_root_dir = os.path.dirname(os.path.abspath(__file__))


def save_keys(owner:str):
    with open(f'{_root_dir}\\keys\\{owner}.pem', mode='w') as f:
        f.write(json.dumps(create_keys()))

def read_keys(owner:str):
    with open(f'{_root_dir}\\keys\\{owner}.pem', mode='r') as f:
        keys = json.loads(f.read())
    return keys

def delete_wallet(owner:str):
    os.remove(f'{_root_dir}\\keys\\{owner}.pem')