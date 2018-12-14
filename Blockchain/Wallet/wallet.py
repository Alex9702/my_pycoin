from Crypto.PublicKey import RSA
import binascii
from os import urandom


# pr = RSA.generate(1024,  rnd.new().read)
# pk = pr.publickey()

print(urandom(256))