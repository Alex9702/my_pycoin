import json
import hashlib

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

def hash_block(block):
    return sha256(json.dumps(block, sort_keys=True))
