"""
Detect AES in ECB mode
https://cryptopals.com/sets/1/challenges/8
"""

import codecs

def repetitions(cipher, block,line):
    """Calculate repeating blocks in a ciphertext
    """
    #Make chunks of the cipher with 16 as block size
    chunks = [cipher[i:i+block] for i in range(0, len(cipher), block)]
    # Finding the reapeating blocks
    repeats = len(chunks) - len(set(chunks))
    result = {'cipher': cipher, 'size': repeats, 'line': line}
    return result


def main():
    info = []
    block = 16
    with open('file.txt', 'r') as f:
        data = f.readlines()

    for ind, cipher in enumerate(data):
        cipher = codecs.decode(cipher.strip(), 'hex')
        info.append(repetitions(cipher, block, ind+1))

    print(max(info, key=lambda x: x['size']))

if __name__ == "__main__":
    main()
