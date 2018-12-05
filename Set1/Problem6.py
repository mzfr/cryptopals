"""
Break repeating-key XOR
https://cryptopals.com/sets/1/challenges/6

Used fixed frequency based scoring system because the one I used in
problem3 was not great and results in a wrong output :(

All the frequencies are taken from: https://en.wikipedia.org/wiki/Letter_frequency
"""
import base64
import itertools

freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}


def xor(s1, s2):
    output = b''
    for char in s1:
        output += bytes([char ^ s2])

    return output


def score(s):
    score = 0
    for i in s:
        c = chr(i).lower()
        if c in freqs:
            score += freqs[c]
    return score


def single_xor(s):
    def key(p):
        return score(p[1])
    return max([(i, xor(s, i)) for i in range(0, 256)], key=key)


def repeating_xor(text, key):
    output = b''
    for i, char in enumerate(text):
        output += bytes([char ^ key[i % len(key)]])

    return output


def hamming_distance(s1, s2):
    """Find hamming distance between two strings
    """
    distance = 0
    for i in range(len(s1)):
        diff = s1[i] ^ s2[i]
        distance += sum(1 for i in bin(diff) if i == '1')

    return distance


def Normalize(ciphertext, keysize):
    """Normalize for every keysize
    """
    chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)][:4]
    pairs = list(itertools.combinations(chunks, 2))
    scores = [hamming_distance(p[0], p[1])/int(keysize) for p in pairs][:6]

    return sum(scores)/len(scores)


def break_repeating_key_xor(x, k):
    keys = []
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    keys = [single_xor(b)[0] for b in transposedBlocks]
    return bytes(keys)


def main():
    with open('file.txt', 'r') as f:
        data = f.read()

    ciphertext = base64.b64decode(data)

    # Normalize ciphertext from keysize 2 to 41 and select the minimum
    ks = min(range(2, 41), key=lambda x: Normalize(ciphertext, x))
    print("[+] Key Size: ", ks)

    k = break_repeating_key_xor(ciphertext, ks)
    print("[+] Key is: ", k)

    print('[+] Plaintext: \n', repeating_xor(ciphertext, k))


if __name__ == '__main__':
    main()
