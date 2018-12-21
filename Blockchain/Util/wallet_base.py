def base16_to_base58(b16:str):
    letters = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58 = ''
    total = int(b16, 16)
    while True:
        if total > len(letters):
            b58 = letters[total % len(letters)] + b58
        else:
            b58 = letters[total] + b58
            break
        total //= len(letters)
    return b58

def base58_to_base16(b58:str):
    letters = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    total = letters.index(b58[0])
    for i in range(1, len(b58)):
        total = (total * 58) + letters.index(b58[i])
    return hex(total)[2:]

def test():
    assert base58_to_base16('6DfqqKExjrXMxrrqREC7gxKQv9MPEWDBaz6iFDdX') == '72f38466e6845726445556649684d4e327535437834484645513169496'
    assert base16_to_base58('3082025B02010002818100EDC54E9B6AA7946D1F4B290B3F0807F7072729FDE0F') == 'uEfofmB1Zkmrhsdptzf87CFxWPjLxTXizSnErYdmyFNN'

if __name__ == '__main__':
    test()