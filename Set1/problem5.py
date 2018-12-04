'''
Implement repeating-key XOR

https://cryptopals.com/sets/1/challenges/5
'''


def repeating_xor(text, key):
    '''In line 8: key[i%len(key)], this gives us the repeating
       character of the KEY.

       EX: B I
           u C
           r E
           n I
           i C
           n E
           g I
    '''
    output = b''
    for i, char in enumerate(text):
        output += bytes([char ^ key[i % len(key)]])

    return output


def main():
    plain = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = b"ICE"
    print(repeating_xor(plain, key).hex())


if __name__ == "__main__":
    main()
