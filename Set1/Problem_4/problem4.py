import codecs

CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n', '\'', " ""


def xor(s1, s2):
    output = b''
    for char in s1:
        output += bytes([char ^ s2])

    return output


def score(txt):
    count = 0
    for byte in txt.lower():
        if chr(byte) in CHARSET or chr(byte) == " ":
            count += 1

    return count


def single_xor(cipher):
    cracked = ""
    best = 0
    for i in range(1, 256):
        xord = xor(cipher, i)
        if score(xord) > best:
            best = score(xord)
            cracked = xord

    return {'plain': cracked, 'score': best}


def main():
    plaintext = []
    with open('file.txt', 'r') as f:
        data = f.readlines()

    for h in data:
        ciphertext = codecs.decode(h.strip(), 'hex')
        plaintext.append(single_xor(ciphertext))

    print(max(plaintext, key=lambda x: x['score']))


if __name__ == "__main__":
    main()
