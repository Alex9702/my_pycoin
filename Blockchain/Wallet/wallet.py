from Crypto.PublicKey import RSA
import binascii
import Crypto.Random

public_key = binascii.hexlify(RSA.generate(1024, Crypto.Random.new().read).exportKey(format='DER')).decode('ascii')


def base16_to_base58(x):
    words = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58 = ''
    total = int(x, 16)
    while True:
        b58 += words[total%len(words)]
        if total < len(words):
            b58 += words[total]
            break
        total //= len(words)
    return b58

print(base16_to_base58(public_key))
