from Crypto.PublicKey import RSA
import binascii
import Crypto.Random as rnd

pr = RSA.generate(1024, rnd.new().read)
print((binascii.hexlify(pr.exportKey()).decode('ascii')))