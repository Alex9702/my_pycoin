import json
import hashlib

def hash_string_256(s):
    return hashlib.sha256(s.encode()).hexdigest()

def hash_block(block):
    return hash_string_256(json.dumps(block, sort_keys=True))
