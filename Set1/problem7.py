"""
AES in ECB mode
https://cryptopals.com/sets/1/challenges/7
"""


import base64
from Crypto.Cipher import AES

with open('file.txt', 'r') as f:
    data = base64.b64decode(f.read())

key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(data)

print("[+] plaintext: ", plaintext)
