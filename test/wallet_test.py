import unittest
from Blockchain.Util.wallet_base import base16_to_base58, base58_to_base16
from Blockchain.Wallet.wallet import verify_transaction

class TestingWallet(unittest.TestCase):
    def test_base_58_to_base16(self):
        self.assertEqual(base58_to_base16('6DfqqKExjrXMxrrqREC7gxKQv9MPEWDBaz6iFDdX'), '72f38466e6845726445556649684d4e327535437834484645513169496')
    
    def test_basee_16_to_base_58(self):
        self.assertEqual(base16_to_base58('3082025B02010002818100EDC54E9B6AA7946D1F4B290B3F0807F7072729FDE0F'), 'uEfofmB1Zkmrhsdptzf87CFxWPjLxTXizSnErYdmyFNN')

    def test_signature(self):
        s = 'DwCuZVv2K4hvWDW3dDnzDCEWj4aL578y2GR2Qidjhgj9TBCwcKXVmbdWH9yBDYgWaU6oNLYo4dt6r9jWEZ4vCcY4kBu9bsnppaLywBWnbKkkYTyk2FX7gjrcKAcF1dGyX4CtaEa27sHYQTqUbSA1z7fNkF1YWEgGSvR1Jz2U9zN9t5M'
        self.assertTrue(verify_transaction('Alex', s))
