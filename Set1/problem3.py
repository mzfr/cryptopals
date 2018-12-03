import codecs

CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n', '\'', " ""


def xor(s1, s2):
    """Find Xor between two strings with bytes
    """
    output = b''
    for char in s1:
        output += bytes([char^s2])

    return output

def score(txt):
    """Creates a score for every string passed
    """
    count = 0
    for byte in txt.lower():
        if chr(byte) in CHARSET:
            count += 1

    return count


def main():
    string = codecs.decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", 'hex')
    cracked = ""
    best = 0
    for i in range(1, 256):
        xord = xor(string, i)
        if score(xord) > best:
            best = score(xord)
            cracked = xord

    print("Plaintext: ", cracked)

if __name__ == "__main__":
    main()
